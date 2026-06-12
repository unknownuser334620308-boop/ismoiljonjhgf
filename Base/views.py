from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import ContactForm

from .models import (
    Item,
    Main_branch,
    Card,
    CardItem,
    Category,
    Contact
)

def home(request):
    narsalar = Item.objects.all()
    main_picture = Main_branch.objects.all()
    messages = Contact.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = ContactForm()

    return render(request, "index.html", {
        "narsalar": narsalar,
        "main_picture": main_picture,
        "form": form,
        "messages": messages
    })


def category_page(request, id):

    category = get_object_or_404(Category, id=id)

    narsalar = Item.objects.filter(category=category)

    categories = Category.objects.all()

    return render(request, "category.html", {
        "category": category,
        "narsalar": narsalar,
        "categories": categories,
    })


def navigation(request):
    return render(request, "navigation.html")


def footer(request):
    return render(request, "footer.html")


def topshirish_punkiti(request):
    return render(request, "topshirish_punkiti.html")


def Sotuvchi_bolish(request):
    return render(request, "sotuvchi_bolish.html")


def sotuvchi_bolish_login(request):
    return render(request, "sotuvchi_bolish_login.html")


def punkitni_ochish(request):
    return render(request, "punkitni_ochish.html")


def savol_javob(request):
    return render(request, "savol_javob.html")


def Mother_and_Children(request):
    return render(request, "mother_and_children.html")


def split(request):
    return render(request, "split.html")


def zamonaviy_bozor(request):
    return render(request, "zamonaviy_bozor.html")


def product_detail(request, id):

    narsalar = get_object_or_404(Item, id=id)

    categories = Category.objects.all()

    return render(request, "product_detail.html", {
        "narsalar": narsalar,
        "categories": categories,
    })


@login_required(login_url='/login/')
def add_to_card(request, item_id):

    item = get_object_or_404(Item, id=item_id)

    card, created = Card.objects.get_or_create(
        user=request.user
    )

    card_item, created = CardItem.objects.get_or_create(
        card=card,
        item=item
    )

    if not created:
        card_item.quantity += 1
        card_item.save()

    return redirect("card_page")


@login_required(login_url='/login/')
def card_page(request):

    card, created = Card.objects.get_or_create(
        user=request.user
    )

    items = card.items.all()

    return render(request, 'card.html', {
        'items': items,
        'card': card,
    })


def delete_card_item(request, id):

    if request.method == "DELETE":

        CardItem.objects.filter(id=id).delete()

        return JsonResponse({
            "message": "Deleted"
        })  

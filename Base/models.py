from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()



class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    rasm = models.ImageField(upload_to='items/')
    narxi = models.IntegerField()
    skidkasi = models.IntegerField(default=0)
    tavsifi = models.CharField(max_length=100)

    def __str__(self):
        return self.tavsifi

    def get_sale_price(self):
        return self.narxi - self.skidkasi


class Main_branch(models.Model):
    picture = models.ImageField(upload_to="banners/")
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.desc


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}ning savati"

    def get_total_price(self):
        total = sum(
            item.get_total_item_price()
            for item in self.items.all()
        )
        return total


class CardItem(models.Model):
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name='items'
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.tavsifi} (x{self.quantity})"

    def get_total_item_price(self):
        return self.item.get_sale_price() * self.quantity

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, get_user_model, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)
User = get_user_model() # django userni olish uchun
def register(request):
    if request.method == "POST":
        username = request.POST.get("username");
        email = request.POST.get("email");
        parol = request.POST.get("parol");
        confirm_parol = request.POST.get("confirm_parol");
        
        if parol != confirm_parol:
            messages.error(request, "Parollar mos kelmadi.")
            return redirect("register")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqachon ro'yxatdan o'tgan.")
            return redirect("register")
        
        user = User.objects.create_user(username=username, email=email, password=parol)
        user.save()

        user  = authenticate(request, username=username, password=parol)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Ro'yxatdan o'tish muvaffaqiyatli amalga oshirildi.")
            return redirect("home")
        
        messages.error(request, "Ro'yxatdan o'tishda xatolik yuz berdi.")
        return redirect("register")
            
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        parol = request.POST.get("parol")
        next_url = request.GET.get("next", "home") # Foydalanuvchi login bo'lgandan keyin qaytishi kerak bo'lgan URL manzilini olish
        
        if not username:
            logger.warning("Login urinishida foydalanuvchi nomi bo'sh qoldirildi.")
            messages.error(request, "Foydalanuvchi nomi kiritilishi kerak.")
            return redirect("login")

        try:
            user = User.objects.get(username=username)
            if user.is_superuser:
                auth_login(request, user)
                logger.info(f"Admin foydalanuvchi '{username}' muvaffaqiyatli login qildi.")
                return redirect(next_url)
            else:
                if not parol:
                    logger.warning(f"Foydalanuvchi '{username}' login urinishida parol bo'sh qoldirildi.")
                    return redirect("login")
                user = authenticate(request, username=username, password=parol)
                if user:
                    auth_login(request, user)
                    messages.success(request, f"Xush kelibsiz, {username}!")
                    return redirect(next_url)
                else:
                    logger.warning(f"Foydalanuvchi '{username}' login urinishida noto'g'ri parol kiritdi.")
                    return redirect("login")
        
        except User.DoesNotExist:
            logger.warning(f"Login urinishida '{username}' nomli foydalanuvchi topilmadi.")
            messages.error(request, "Foydalanuvchi nomi yoki parol noto'g'ri.")
            return redirect("login")
    
    return render(request, "login.html")



def logout(request):
    auth_logout(request)
    messages.success(request, "Siz muvaffaqiyatli chiqdingiz.")
    return redirect("home")


from django.urls import include, path
from .views import *

urlpatterns = [
    path("home/", home, name="home"),
    path("toshirish_punkiti/", topshirish_punkiti, name="topshirish_punkiti"),
    path("sotuvchi_bolish/", Sotuvchi_bolish, name="sotuvchi_bolish"),
    path("sotuvchi_bolish_login/", sotuvchi_bolish_login, name="sotuvchi_bolish_login"),
    path("punkitni_ochish/", punkitni_ochish, name="punkitni_ochish"),
    path("savol-javob/", savol_javob, name="savol_javob"),
    path("product_detail/<int:id>/", product_detail, name="product_detail"),
    path("mother_and_children/", Mother_and_Children, name="Mother"),
    path("", split, name="split"),
    path("zamonaviy_bozor/", zamonaviy_bozor, name="zamonaviy_bozor"),

    path("add-to-card/<int:item_id>/", add_to_card, name="add_to_card"),
    path("card-item/<int:id>/", delete_card_item, name="delete_card_item"),
    path("card/", card_page, name="card_page"),
    path('i18n/', include('django.conf.urls.i18n')),

    path("category/<int:id>/", category_page, name="category_page"),
]


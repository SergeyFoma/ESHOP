from django.urls import path
from . import views

app_name="goods"

urlpatterns = [
    path('search/', views.catalog, name="search"),
    path('catalog/<slug:category_slug>/', views.catalog, name="catalog"),
    #path('catalog/<slug:category_slug>/<int:page>/', views.catalog, name="catalog"),
    #path('product/<int:product_id>/', views.product, name="product"),
    path('product/<slug:product_slug>/', views.product, name="product"),

    path('home/', views.home, name='home'),
    path('catalog2/', views.catalog2, name="catalog2"),
    path('product2/<slug:product2_slug>/', views.product2, name="product2"),
]

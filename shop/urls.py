from django.urls import path
from django.views.generic.base import RedirectView


from shop.views import index, detail, checkout, confimation

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confimation, name="confirmation"), 
]

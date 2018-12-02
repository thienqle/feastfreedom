from django.conf.urls import url
from cart import views

urlpatterns = [
    url(r'^$', views.cart, name='cart'),
    url(r'^remove/(?P<id>\d+)$', views.delete_item, name='remove_item'),
    url(r'^placeorder$', views.place_order, name='place_order'),
]
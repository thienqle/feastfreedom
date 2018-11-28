from django.conf.urls import url
from regular_user import views

urlpatterns = [
    url(r'^$', views.list_all_kitchen, name='index'),
]
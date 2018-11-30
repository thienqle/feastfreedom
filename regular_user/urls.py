from django.conf.urls import url
from regular_user import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.list_all_kitchen, name='index'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^login$', auth_views.LoginView.as_view(template_name='regular_user/login_form.html'), name='login'),
    url(r'^logout$', views.log_out, name='logout')
]
from django.conf.urls import url
from service_provider import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup$', views.signup, name='signup_provider'),
    url(r'^signedup$', views.submit_kitchen, name='summitted_kitchen'),
    url(r'^signupnext/(?P<id>\d+)$', views.signup_kitchen_n, name='signup_kitchen'),
    url(r'^login$', auth_views.LoginView.as_view(template_name='service_provider/login_form.html'), name='provider_login'),
    url(r'^logout$', views.log_out, name='logout'),
    url(r'^(?P<id>\w+)$', views.kitchen_detail, name='kitchen_detail'),
]
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^sign_?up/?$',views.sign_up, name='sign_up'),
    url(r'^park/?$',views.park, name='park'),
    url(r'^unpark/?$',views.unpark, name='unpark'),
    
]

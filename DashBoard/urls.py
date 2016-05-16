from django.conf.urls import url

from DashBoard import views


urlpatterns = [
    url(r'^$', views.dashboard, name='Dashboard'),
    url(r'^logout/', views.Logout, name='Logout'),
    url(r'^profile/', views.profile, name='Profile'),
]

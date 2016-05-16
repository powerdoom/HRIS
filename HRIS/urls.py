from django.conf.urls import url, include
from django.contrib import admin
from HRIS import views

urlpatterns = [
    url(r'^$', views.home, name='Home'),
    url(r'^dashboard/', include('DashBoard.urls')),
    url(r'^admin/', admin.site.urls),
]

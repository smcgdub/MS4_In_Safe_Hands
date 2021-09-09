# from django.contrib import admin
from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.covid_numbers, name='covid_numbers')
    # path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    # path('', include('home.urls')),
]
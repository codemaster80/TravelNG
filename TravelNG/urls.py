"""TravelNG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from TravelNG import settings
from request.views import home, new_travel_request, new_travel_invoice, logout_view, delete_travel_request

urlpatterns = [
    path('request/', home, name="home"),
    path('newRequest/', new_travel_request, name="newTravelRequest"),
    path('deleteRequest/<int:item_id>', delete_travel_request, name="deleteTravelRequest"),
    path('newInvoice/', new_travel_invoice, name="newInvoice"),
    path('logout/', logout_view, {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

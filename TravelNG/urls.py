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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

import request.views
from TravelNG import settings
from request.views import home, logout_view, delete_travel_request

urlpatterns = [
    path('', home, name="home"),
    re_path(r'^Request/Add/$', request.views.travel_request_details, name="addTravelRequest"),
    re_path(r'^Request/Edit/(?P<pk>[0-9]+)/?$', request.views.travel_request_details, name="editTravelRequest"),
    path('deleteRequest/<int:item_id>', delete_travel_request, name="deleteTravelRequest"),
    re_path(r'^Invoice/Add/$', request.views.travel_invoice_details, name="addTravelInvoice"),
    re_path(r'^Invoice/Edit/(?P<pk>[0-9]+)/?$', request.views.travel_invoice_details, name="editTravelInvoice"),
    re_path(r'^Invoice/Delete/$<int:item_id>', request.views.delete_travel_invoice, name="deleteTravelInvoice"),
    path('Invoice/Delete/<int:item_id>', request.views.delete_travel_invoice, name="deleteTravelInvoice"),
    re_path(r'^Request/Auth/$', request.views.travel_auth_details, name="travelAuth"),
    re_path(r'^Auth/Edit/(?P<pk>[0-9]+)/?$', request.views.travel_auth_details, name="editTravelAuth"),
    re_path(r'^Invoice/Refund/$', request.views.travel_invoice_refund, name="travelInvoiceRefund"),
    re_path(r'^Invoice/Refund/Edit/(?P<pk>[0-9]+)/?$', request.views.travel_invoice_refund, name="editTravelRefund"),
    path('logout/', logout_view, {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

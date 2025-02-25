"""
URL configuration for data_integration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
#from data_integration.data_integration_app.views import CustomerViewSet, SalesmanViewSet, SalesMViewSet, SalesDViewSet, ItemCardViewSet, CustCardViewSet

from data_integration_app.views import (CustomerViewSet, SalesmanViewSet, SalesMViewSet, SalesDViewSet, ItemCardViewSet, CustCardViewSet)

urlpatterns = [
    path('customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'}), name='customer-list'),
    path('customers/<int:pk>/',
         CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='customer-detail'),

    path('salesmen/', SalesmanViewSet.as_view({'get': 'list', 'post': 'create'}), name='salesman-list'),
    path('salesmen/<int:pk>/',
         SalesmanViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='salesman-detail'),

    path('salesm/', SalesMViewSet.as_view({'get': 'list', 'post': 'create'}), name='salesm-list'),
    path('salesm/<int:pk>/',
         SalesMViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='salesm-detail'),

    path('salesd/', SalesDViewSet.as_view({'get': 'list', 'post': 'create'}), name='salesd-list'),
    path('salesd/<int:pk>/',
         SalesDViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='salesd-detail'),

    path('itemcard/', ItemCardViewSet.as_view({'get': 'list', 'post': 'create'}), name='itemcard-list'),
    path('itemcard/<int:pk>/',
         ItemCardViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='itemcard-detail'),

    path('custcard/', CustCardViewSet.as_view({'get': 'list', 'post': 'create'}), name='custcard-list'),
    path('custcard/<int:pk>/',
         CustCardViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='custcard-detail'),
]

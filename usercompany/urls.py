from django.conf.urls import url, include
from django.urls import path

from usercompany import views

urlpatterns = [
    path('home/', views.company_home, name='company_home'),
    path('stock/add/', views.add_stock, name='add_stock_company'),
    path('stock/view/', views.view_stocks, name='view_stock_company'),
    path('order/views/', views.view_orders, name='view_order_company'),
    path('transactions/view', views.view_transactions, name='view_transactions_company'),

    url(r'^order/(?P<pk>\d+)/accept', views.accept_order, name='accept_order_company'),
    url(r'^order/(?P<pk>\d+)/decline$', views.decline_order, name='decline_order_company'),
    url(r'^stock/(?P<pk>\d+)/edit$', views.edit_stock, name='edit_stock_company'),
    url(r'^stock/(?P<pk>\d+)/delete$', views.delete_stock, name='delete_stock_company'),
]

from django.urls import path

from . import views

urlpatterns = [
    # path('psychologues/new/', views.client_new, name='new_client_form'),
    path('client', views.ClientListView3.as_view(), name='list'),
    path('client/add/', views.ClientCreateView.as_view(), name='client_add'),
    path('client/<uuid:uuid>/', views.ClientView.as_view(), name='client_view'),
    path('client/<uuid:uuid>/detail/', views.ClientDetailView.as_view(), name='detail'),
    #path('client/<int:pk>/', views.ClientUpdateView.as_view(), name='client_change'),
    
   
]
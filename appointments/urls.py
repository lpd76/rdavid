from django.urls import path
from . import views

urlpatterns = [
    # path('psychologues/new/', views.client_new, name='new_client_form'),
    path('appointments/add/', views.AppointmentCreateView.as_view(), name='appointment_add'),
    path('psychologues/<int:pk>/appointemnts/', views.AppointmentListView.as_view(), name='psy_appointment_view'),
    path('appointments/detail/<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointments/update/<int:pk>/', views.AppointmentUpdateView.as_view(), name='appointment_update'),
    #path('client/<int:pk>/', views.ClientUpdateView.as_view(), name='client_change'),  
]

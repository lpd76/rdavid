from django.urls import path

from . import views

urlpatterns = [
    path('psychologues/home/', views.psychologues_home, name='psychologues_home'),
    path('psychologues/<int:pk>/', views.psychologues_profile, name='psychologues_profile'),
    path('psychologues/<int:pk>/update_profile/', views.PsycologueUpdateView.as_view(), name='update_profile'),
    path('psychologues/dash/', views.PsychologueDashBoard.as_view(), name='dashboard'),
]
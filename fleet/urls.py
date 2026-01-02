from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    path('<int:vehicle_id>/add_ticket/', views.add_ticket, name='add_ticket'),
    path('workshop/', views.workshop_dashboard, name='workshop_dashboard'),
    path('ticket/<int:ticket_id>/close/', views.close_ticket, name='close_ticket'),
    path('vehicle/<int:pk>/pdf/', views.create_vehicle_pdf, name='vehicle_pdf'),
]
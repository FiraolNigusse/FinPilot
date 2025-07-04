from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('budget-planner/', views.budget_planner, name='budget_planner'),
]

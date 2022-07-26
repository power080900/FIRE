from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('calculator/', views.calculator),
    path('financialledger/', views.financialledger),
    path('calculator/result/', views.result)
    ]
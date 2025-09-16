from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cart.index'),
    path('<int:id>/add/', views.add, name='cart.add'),
    path('clear/', views.clear, name='cart.clear'),
    path('purchase/', views.purchase, name='cart.purchase'),
    path('survey/', views.survey, name='survey'),
    path('survey/thankyou/', views.survey_thank_you, name='survey.thank_you'),
    path('survey/all/', views.survey_list, name='survey.list'),
]
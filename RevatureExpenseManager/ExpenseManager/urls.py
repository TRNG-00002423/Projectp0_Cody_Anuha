from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('viewExpenses/<int:id>', views.viewExpenses, name='viewExpenses'),
    path('viewAllExpenses/', views.viewAllExpenses, name='viewAllExpenses'),
    path('viewAllApprovals/', views.viewAllApprovals, name='viewAllApprovals'),
    path('addExpense/', views.addExpense, name="addExpense"),
    path('addExpense/add/', views.add, name="add"),
    path('viewAllExpenses/addExpense/', views.addExpense, name='addExpense'),
    path('viewAllExpenses/addExpense/add/', views.add, name='add'),
    path('viewExpenses/addExpense/', views.addExpense, name='addExpense'),
    path('viewExpenses/addExpense/add/', views.add, name='add'),

]
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
    path('register/', views.register, name='register'),
    path('register/addUser/', views.addUser, name='addUser'),
    path('login/', views.login, name='login'),
    path('login/signIn/', views.signIn, name='signIn'),
    path('login/signIn/viewAllExpenses/', views.viewAllExpenses, name='viewAllExpenses'),
    path('login/signIn/viewAllApprovals/', views.viewAllApprovals, name='viewAllApprovals'),
    path('login/signIn/viewExpenses/<int:id>', views.viewExpenses, name='viewExpenses'),
    path('login/signIn/viewExpenses/addExpense/', views.addExpense, name='addExpense'),
    path('login/signIn/viewExpenses/addExpense/add/', views.add, name='add'),

]
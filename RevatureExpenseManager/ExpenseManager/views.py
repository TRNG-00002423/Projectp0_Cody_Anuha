from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import User, Expense, Approval



def index(request):
    Users = User.objects.all()
    print("\n\n")
    print("Email : ")
    email = input().strip().lower()
    print("\n")
    print("Password : ")
    password = input()
    print("\n\n")
    return render(request, 'Employees.html', {'Users': Users})






def viewAllExpenses(request):
    Expenses = Expense.objects.select_related('user_id').all()

    # Need To Reformat or use tabulate library :
    
    # print("\n\n")
    # print("="*128)
    # print(f"|      Email{:<10}          |       Category{:<10}         |         Description{:<10}      |       Amount{:<10}         |      Date Of Expense{:<10}       |")

    # for x in Expenses:
    #     print("="*128)
    #     print(f"|      {x.user_id:<10}          |       {x.category:<10}         |         {x.description:<10}      |       {x.amount:<10}         |      {x.dateofExpense:<10}       |")

    # print("="*128)
    # print("\n\n")

    print("\n\n")
    print("="*128)
    print(f"|      Email          |       Category         |         Description      |       Amount         |      Date Of Expense        |")

    for x in Expenses:
        print("="*128)
        print(f"| {x.user_id.email}  |   {x.category}   |    {x.description}      |      {x.amount}     |     {x.dateofExpense}       |")

    print("="*128)
    print("\n\n")
    return render(request, 'Expenses.html', {'Expense': Expenses})




# BROKEN LOGIC : reviewer(FK to users) --> reviewer.email needs to stay empty when initalized (i.e. When a new expense is added)
# TODO : FIX --> AttributeError: 'NoneType' object has no attribute 'email'

def viewAllApprovals(request):
    approvals = Approval.objects.select_related('reviewer').all()

    print("\n\n")
    print("="*141)
    print("|   Approval Id      |    Expense Id     |       Status         |         Reviewer      |       Comment         |      Date Of Review       |")

    for x in approvals:
        print("="*141)
        email_check = x.get_status_display
        print(f"{email_check}")
        if ((email_check=="PENDING") or (email_check=="P")):
            print(f"|      {x.id}          |      {x.expense_id}          |       {x.get_status_display}         |          No Data Available.       |       {x.comment}         |      {x.date_approved}       |")
        else:
            print(f"|      {x.id}          |      {x.expense_id}          |       {x.get_status_display}         |         {x.reviewer.email}      |       {x.comment}         |      {x.date_approved}       |")
        

    print("="*141)
    print("\n\n")
    return render(request, 'Approvals.html', {'Approval': approvals})




def addExpense(request):
    template = loader.get_template('addExpense.html')
    print("\n")
    print("Email :")
    email = input().strip().lower()
    print("\n")
    print("Category :")
    category = input()
    print("\n")
    print("Descripton :")
    description = input()
    print("\n")
    print("Amount :")
    amount = input()
    print("\n")
    print("Date Of Expense :")
    DOE = input()
    print("\n")

    # Logic To Add New Expenses & Approvals, Can Add After Fixing Broken Expense & Approval Implementations :

    # findUserId = User.objects.get(email_iexact=input1)

    # if findUserId:
    #     NewExpense = Expense.objects.create(user_id=findUserId, description=input3, amount=input4, dateofExpense=input5, category=input2)
    #     expenseId = NewExpense.pk
    #     NewApproval = Approval.objects.create(expense_id=expenseId, reviewer="None")

    return HttpResponse(template.render({}, request))


def add(request):
    input1 = request.POST['email'].strip().lower()
    input2 = request.POST['category']
    input3 = request.POST['description']
    input4 = request.POST['amount']
    input5 = request.POST['dateofExpense']
    findUserId = User.objects.get(email_iexact=input1)
    if findUserId:
        NewExpense = Expense.objects.create(user_id=findUserId, description=input3, amount=input4, dateofExpense=input5, category=input2)
        expenseId = NewExpense.pk
        NewApproval = Approval.objects.create(expense_id=expenseId, reviewer="None")
    return HttpResponseRedirect(reverse('index'))



def viewExpenses(request, id):
    users = User.objects.get(id=id)
    expenses = Expense.objects.select_related('user_id').filter(user_id=users.email)
    return render(request, 'EmployeeExpenses.html', {'expenses': expenses})
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import User, Expense, Approval
from django.urls import reverse



def EmployeePortal(request):
    return render(request, 'EmployeePortal.html', {})

def register(request):
    return render(request, 'register.html', {})

def addUser(request):
    return render(request, 'register.html', {})

def login(request):
    return render(request, 'login.html', {})


def EmployeeLogin(request):
    return render(request, 'EmployeeLogin.html', {})


def ManagerLogin(request):
    return render(request, 'ManagerLogin.html', {})


def signIn(request):
    email = request.POST['email']
    password = request.POST['password']
    ifValidUser = User.objects.filter(email=email).exists()
    Users = User.objects.all()

    if ifValidUser:
        findUser = User.objects.get(email=email)
        findPassword = findUser.password
        if(findPassword==password):
            return render(request, 'Employees.html', {'Users': Users})
        

    return render(request, 'login.html', {'error_message': "Invalid Credentials. Please Try Again."})




def signInEmployee(request):
    email = request.POST['email']
    password = request.POST['password']
    ifValidUser = User.objects.filter(email=email).exists()
    Users = User.objects.all()

    if ifValidUser:
        findUser = User.objects.get(email=email)
        findPassword = findUser.password
        if(findPassword==password):
            return render(request, 'Employees.html', {'Users': Users})
        

    return render(request, 'EmployeeLogin.html', {'error_message': "Invalid Credentials. Please Try Again."})


def signInManager(request):
    email = request.POST['email']
    password = request.POST['password']
    ifValidUser = User.objects.filter(email=email).exists()
    Users = User.objects.all()

    if ifValidUser:
        findUser = User.objects.get(email=email)
        findPassword = findUser.password
        if(findPassword==password):
            return render(request, 'Employees.html', {'Users': Users})
        

    return render(request, 'ManagerLogin.html', {'error_message': "Invalid Credentials. Please Try Again."})



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
        print(f"| {x.user_id.email}  |   {x.category}   |    {x.description}      |      {x.amount:.2f}     |     {x.dateofExpense}       |")

    print("="*128)
    print("\n\n")
    return render(request, 'Expenses.html', {'Expense': Expenses})




# BROKEN LOGIC : reviewer(FK to users) --> reviewer.email needs to stay empty when initalized (i.e. When a new expense is added)
# TODO : FIX --> AttributeError: 'NoneType' object has no attribute 'email'

def viewAllApprovals(request):
    approvals = Approval.objects.select_related('reviewer').all()

    print("\n\n")
    print("="*114)
    print("| Approval Id | Expense Id |     Status      |         Reviewer      |     Comment       |    Date Of Review     |")

    for x in approvals:
        print("="*114)
        email_check = x.get_status_display
        # print(f"{email_check}")
        # if ((email_check=="PENDING") or (email_check=="P")):
        #     print(f"|      {x.id}          |      {x.expense_id}          |       {x.get_status_display}         |          No Data Available.       |       {x.comment}         |      {x.dateReviewed}       |")
        # else:
        #     print(f"|      {x.id}          |      {x.expense_id}          |       {x.get_status_display}         |         {x.reviewer.email}      |       {x.comment}         |      {x.dateReviewed}       |")
        status_longForm = x.status;
        if (status_longForm=="P"):
            status_longForm="Pending"
        elif (status_longForm=="A"):
            status_longForm="Approved"
        elif (status_longForm=="D"):
            status_longForm="Denied"
        else:
            status_longForm="Pending"
        print(f"|     {x.id}       |    {x.expense_id}   |      {status_longForm}       |    {x.reviewer.email}    |       {x.comment}        |       {x.dateReviewed}     |")
        

    print("="*114)
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
    DOExp = input()
    print("\n")

    # Logic To Add New Expenses & Approvals, Can Add After Fixing Broken Expense & Approval Implementations :

    # findUserId = User.objects.get(email_iexact=email)
    # findUserId = User.objects.get(email=email)
    ifValidUser = User.objects.filter(email=email).exists()

    if ifValidUser:
        findUserId = User.objects.get(email=email)
        NewExpense = Expense.objects.create(user_id=findUserId, description=description, amount=amount, dateofExpense=DOExp, category=category)
        expenseId = NewExpense.pk
        findReviewer = User.objects.get(email="julia.koch@revature.com")
        NewApproval = Approval.objects.create(expense_id=expenseId, status="P", reviewer=findReviewer)
        # NewApproval = Approval.objects.create(expense_id=expenseId, status="P", reviewer="julia.koch@revature.com")

    return HttpResponse(template.render({}, request))


def add(request):
    email = request.POST['email'].strip().lower()
    category = request.POST['category']
    description = request.POST['description']
    amount = request.POST['amount']
    DOExp = request.POST['dateofExpense']

    # findUserId = User.objects.get(email_iexact=email)
    ifValidUser = User.objects.filter(email=email).exists()

    if ifValidUser:
        findUserId = User.objects.get(email=email)
        NewExpense = Expense.objects.create(user_id=findUserId, description=description, amount=amount, dateofExpense=DOExp, category=category)
        expenseId = NewExpense.pk
        findReviewer = User.objects.get(email="julia.koch@revature.com")
        NewApproval = Approval.objects.create(expense_id=expenseId, status="P", reviewer=findReviewer)
    return HttpResponseRedirect(reverse('index'))



def viewExpenses(request, id):
    users = User.objects.get(id=id)
    expenses = Expense.objects.select_related('user_id').filter(user_id=users.email)
    return render(request, 'EmployeeExpenses.html', {'expenses': expenses})
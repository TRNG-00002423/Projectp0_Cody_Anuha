from django.db import models
import datetime
from django.utils import timezone


class User(models.Model):
    email = models.EmailField(max_length=45, unique=True)
    password = models.CharField(max_length=15)

    class RoleChoices(models.TextChoices):
        MANAGER = "M", "MANAGER"
        EMPLOYEE = "E", "EMPLOYEE"

    role = models.CharField(max_length=1, choices=RoleChoices.choices, default=RoleChoices.MANAGER)



class Expense(models.Model):
    user_id = models.ForeignKey(User, to_field='email', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=255)
    amount = models.FloatField(default=0)
    dateofExpense = models.DateField('Date Of Expense', default=None, null=True, blank=True)
    category = models.CharField(max_length=25)


    def was_published_recently(self):
        return self.date_approved >= timezone.now() - datetime.timedelta(days=1)
    


class Approval(models.Model):
    expense_id = models.IntegerField()

    class StatusChoices(models.TextChoices):
        PENDING = "P", "PENDING"
        APPROVED = "A", "APPROVED"
        DENIED = "D", "DENIED"

    status = models.CharField(max_length=1, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    reviewer = models.ForeignKey(User, to_field='email', on_delete=models.SET_NULL, null=True, blank=True)
    dateReviewed = models.DateField('Date Of Review', default=None, null=True, blank=True)
    comment = models.CharField(max_length=40, default=None, null=True, blank=True)

    def was_published_recently(self):
        return self.date_approved >= timezone.now() - datetime.timedelta(days=1)
    
    

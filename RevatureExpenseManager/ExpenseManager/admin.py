from django.contrib import admin

from .models import User, Expense, Approval



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role')
    list_filter = ('email', 'role')
    search_fields = ('email', 'role')




@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user_id__email', 'category', 'description', 'amount', 'dateofExpense')
    list_filter = ('user_id__email', 'category', 'description', 'amount', 'dateofExpense')
    search_fields = ('user_id__email', 'category', 'description', 'amount', 'dateofExpense')





@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    list_display = ('expense_id', 'status', 'reviewer', 'dateReviewed', 'comment')
    list_filter = ('expense_id', 'status', 'reviewer', 'dateReviewed', 'comment')
    search_fields = ('expense_id', 'status', 'reviewer', 'dateReviewed', 'comment')







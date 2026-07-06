package com.revature.controller;

import com.revature.dao.ApprovalDao;
import com.revature.dao.ExpenseDao;
import com.revature.model.Approval;
import com.revature.model.ApprovalStatus;
import com.revature.model.PendingExpenseView;

import java.util.List;

public class ExpenseController {

    private final ExpenseDao expenseDao;
    private final ApprovalDao approvalDao;

    public ExpenseController(ExpenseDao expenseDao, ApprovalDao approvalDao) {
        this.expenseDao = expenseDao;
        this.approvalDao = approvalDao;
    }

    public List<PendingExpenseView> getPendingExpenses() {
        return expenseDao.findPending();
    }

    public void decideExpense(int expenseId, int reviewerId, boolean approve, String comment) {
        Approval approval = approvalDao.findByExpenseId(expenseId)
                .orElseThrow(() -> new IllegalArgumentException(
                        "No approval record found for expense id: " + expenseId));

        if (approval.getStatus() != ApprovalStatus.PENDING) {
            throw new IllegalStateException(
                    "Expense " + expenseId + " has already been " + approval.getStatus());
        }

        if (!approve && (comment == null || comment.isBlank())) {
            throw new IllegalArgumentException("A comment is required when denying an expense");
        }

        ApprovalStatus newStatus = approve ? ApprovalStatus.APPROVED : ApprovalStatus.DENIED;
        approvalDao.recordDecision(expenseId, reviewerId, newStatus, comment);
    }
}
package com.revature.controller;

import com.revature.dao.ReportDao;
import com.revature.model.ExpenseReportView;

import java.time.LocalDate;
import java.util.List;

public class ReportController {

    private final ReportDao reportDao;

    public ReportController(ReportDao reportDao) {
        this.reportDao = reportDao;
    }

    public List<ExpenseReportView> getReportByEmployee(int userId) {
        return reportDao.findByEmployee(userId);
    }

    public List<ExpenseReportView> getReportByDateRange(LocalDate start, LocalDate end) {
        if (start.isAfter(end)) {
            throw new IllegalArgumentException("Start date must be before or equal to end date");
        }
        return reportDao.findByDateRange(start, end);
    }
}
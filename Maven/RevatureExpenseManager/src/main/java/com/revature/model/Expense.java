package com.revature.model;

public class Expense {

    private int id;
    private int  user_id;
    private float amount;
    private String description;
    private String date;

    public Expense() {
    }

    public Expense(int id, int user_id, float amount, String description, String date) {
        this.id = id;
        this.user_id = user_id;
        this.amount = amount;
        this.description = description;
        this.date = date;
    }

    public int getId() {
        return id;
    }

    // public void setId(int id) {
    //     this.id = id;
    // }

    public int getUser_id() {
        return user_id;
    }

    // public void setUser_id(int user_id) {
    //     this.user_id = user_id;
    // }

    public float getAmount() {
        return amount;
    }

    // public void setAmount(float amount) {
    //     this.amount = amount;
    // }

    public String getDescription() {
        return description;
    }

    // public void setDescription(String description) {
    //     this.description = description;
    // }

    public String getDate() {
        return date;
    }

    // public void setDate(String date) {
    //     this.date = date;
    // }

    

    

}

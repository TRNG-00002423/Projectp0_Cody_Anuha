# User Stories

## 1 : Our API should be able to process New User registrations.

As a user, I should be able to create a new Account on the endpoint POST localhost:8080/register??


The body will contain a representation of a JSON account, but will not contain an accountId.


The registration will be successful if and only if the username is not blank, the password is at least 4 characters long, and an account with that username does not already exist. If all these conditions are met, the response body should contain a JSON of the Account, including its accountId. The response status should be 200, OK, which is the default. The new account should be persisted to the database.
If the registration is not successful due to a duplicate username, the response status should be 409. (Conflict)
If the registration is not successful due for some other reason, the response status should be 400. (Client error)




## 1 : Our API should be able to process User logins.


As a user, I should be able to login on the endpoint POST localhost:8080/login ??? or 8080:home ??


The body will contain a representation of a JSON Account.


The login will be successful if and only if the username and password provided in the request body JSON match a real account existing on the database.


If successful, within the response body, the response status should be 200, ok.


However, if the login is not successful, the response status should be 401. (UNAUTHORIZED)




## 2 : Our API should be able to process the creation of new expenses.


As an employee, I should be able to submit a new expense on the endpoint POST localhost:8080/addExpense ???




. The response body will contain a JSON representation of an expense, not including the expenseId. This JSON Expense Object should be persisted to the database.


The creation of the expense will be successful if and only if the Expense description, amount, date of expenditure, and category are not blank, along with the userId referring to a real, existing user.


If successful, within the response body, the response status should be 200, ok. The new expense should be persisted to the database.


However, if the creation of the message is not successful, the response status should be 400. (Client Error)




## 3 : Our API should be able to retrieve all expenses.


As a user, I should be able to submit a GET request on the endpoint GET localhost:8080/EmployeeExpenses.


The response body should contain a JSON representation of a list containing all expenses retrieved from the database. It is expected for the list to simply be empty if there are no expenses. The response status should always be 200, which is the default.




## 4 : Our API should be able to retrieve all expenses created by a user.


As a user, I should be able to submit a GET request on the endpoint GET localhost:8080/EmployeeExpenses/{user_id}.


The response body should contain a JSON representation of an expense identified by the uesrId. It is expected for the response body to simply be empty if there are no expenses. The response status should always be 200, which is the default.




## 5 : Our API should be able to update an expense identified by an expenseId.


As a user, I should be able to submit a PATCH request on the endpoint PATCH localhost:8080/EmployeeExpenses/{expense_Id}. The request body should contain a userId, description, amount, dateofExpense, and category. The request body cannot be guaranteed to contain any other information.


The update of this expense should be successful if and only if the expenseId already exists and all of the values in the expected fields are not left empty. If the update is successful, the response body should contain the number of rows updated (1), and the response status should be 200, which is the default. The expense existing on the database should have the updated the userId, description, amount, dateofExpense, and category.






## 6 : Our API should be able to process the creation of new approvals.


As an employee, I should be able to submit a new approval on the endpoint POST localhost:8080/addApproval ???




. The response body will contain a JSON representation of an approval, not including the approvalId. This JSON Approval Object should be persisted to the database.


The creation of the approval will be successful if and only if the Approval status, reviewer, date reviewed, comment and the expenseId it refers to are not left blank, along with the userId of the reviewer referring to a real, existing user.


If successful, within the response body, the response status should be 200, ok. The new approval should be persisted to the database.


However, if the creation of the approval is not successful, the response status should be 400. (Client Error)




## 7 : Our API should be able to retrieve all approvals.


As a user, I should be able to submit a GET request on the endpoint GET localhost:8080/EmployeeApprovals.


The response body should contain a JSON representation of a list containing all approvals retrieved from the database. It is expected for the list to simply be empty if there are no approvals. The response status should always be 200, which is the default.




## 8 : Our API should be able to retrieve all approvals created by a user.


As a user, I should be able to submit a GET request on the endpoint GET localhost:8080/EmployeeApprovals/{user_id}.


The response body should contain a JSON representation of an approval identified by the uesrId. It is expected for the response body to simply be empty if there are no expenses. The response status should always be 200, which is the default.




## 9 : Our API should be able to update an approval identified by an approvalId.


As a user, I should be able to submit a PATCH request on the endpoint PATCH localhost:8080/EmployeeApprovals/{approvalId}. The request body should contain an expenseId, status, reviewer, the date reviewed, and comment. The request body cannot be guaranteed to contain any other information.


The update of this approval should be successful if and only if the approvalId already exists and all of the values in the expected fields are not left empty. If the update is successful, the response body should contain the number of rows updated (1), and the response status should be 200, which is the default. The approval existing on the database should have the updated the expense_id, status, review, date reviewed, and comment.

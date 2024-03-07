CREATE DATABASE BANK;

USE BANK;

CREATE TABLE customers(
customer_id int primary key,
first_name varchar(15),
last_name varchar(15),
DOB date,
email varchar(30) UNIQUE,
phone_number varchar(20),
address varchar(50)
);

CREATE TABLE accounts(
account_id int primary key,
customer_id int foreign key references customers(customer_id),
account_type varchar(50),
balance decimal(18, 2),
);


CREATE TABLE transactions(
transaction_id varchar(10) PRIMARY KEY,
account_id int foreign key references accounts(account_id),
transaction_type varchar(50),
amount int,
transaction_date date
);

INSERT INTO Customers (customer_id, first_name, last_name, DOB, email, phone_number, address)
VALUES
    (1, 'Aarav', 'Gupta', '1990-05-15', 'aaravgupta@example.com', '9876543210', 'Bangalore'),
    (2, 'Aaradhya', 'Patel', '1985-09-20', 'aaradhyapatel@example.com', '9876543211', 'Mumbai'),
    (3, 'Aryan', 'Sharma', '1988-11-12', 'aryansharma@example.com', '9876543212', 'Delhi'),
    (4, 'Ananya', 'Singh', '1992-03-25', 'ananyasingh@example.com', '9876543213', 'Kolkata'),
    (5, 'Advik', 'Kumar', '1995-07-08', 'advikkumar@example.com', '9876543214', 'Chennai'),
    (6, 'Ishaan', 'Jain', '1983-12-30', 'ishaanjain@example.com', '9876543215', 'Hyderabad'),
    (7, 'Mira', 'Pandey', '1987-02-14', 'mirapandey@example.com', '9876543216', 'Pune'),
    (8, 'Zoya', 'Verma', '1998-06-18', 'zoyaverma@example.com', '9876543217', 'Ahmedabad'),
    (9, 'Vivaan', 'Chopra', '1982-10-03', 'vivaanchopra@example.com', '9876543218', 'Jaipur'),
    (10, 'Vihaan', 'Gandhi', '1993-04-17', 'vihaangandhi@example.com', '9876543219', 'Lucknow');

INSERT INTO Accounts (account_id, customer_id, account_type, balance)
VALUES
    (101, 1, 'savings', 50000.00),
    (102, 2, 'current', 75000.00),
    (103, 3, 'savings', 100000.00),
    (104, 4, 'zero_balance', 0.00),
    (105, 5, 'savings', 25000.00),
    (106, 6, 'current', 35000.00),
    (107, 7, 'savings', 80000.00),
    (108, 8, 'current', 60000.00),
    (109, 9, 'savings', 45000.00),
    (110, 10, 'zero_balance', 0.00),
	(111, 1, 'current', 5000.00);

INSERT INTO transactions (transaction_id, account_id, transaction_type, amount, transaction_date)
VALUES
    ('1001', 101, 'deposit', 10000.00, '2024-03-01'),
    ('1002', 102, 'withdrawal', 5000.00, '2024-03-02'),
    ('1003', 103, 'deposit', 20000.00, '2024-03-03'),
    ('1004', 104, 'deposit', 5000.00, '2024-03-04'),
    ('1005', 105, 'withdrawal', 10000.00, '2024-03-05'),
    ('1006', 106, 'deposit', 15000.00, '2024-03-06'),
	('1007', 111, 'deposit',5000.00, '2024-03-02'),
    ('1008', 108, 'deposit', 25000.00, '2024-03-08'),
    ('1009', 109, 'withdrawal', 7000.00, '2024-03-09'),
    ('1010', 110, 'deposit', 1000.00, '2024-03-10'),
	('1011', 101, 'deposit', 10000.00, '2024-04-01'),
	('1012', 102, 'deposit', 5000.00, '2024-05-02'),
	('1013', 103, 'deposit', 20000.00, '2024-06-03'),
	('1014', 110, 'deposit', 1000.00, '2024-03-10');
	
select * from customers;
select * from accounts;
select * from transactions;

-- TASK - 2: Write SQL queries for the following tasks:

--1. Write a SQL query to retrieve the name, account type and email of all customers.
SELECT c.first_name, c.last_name, account_type, c.email
FROM Customers c
INNER JOIN Accounts a ON c.customer_id = a.customer_id;

--2. Write a SQL query to list all transaction corresponding customer.
SELECT c.customer_id,t.transaction_id,a.account_id,t.transaction_type,t.amount,t.transaction_date,a.balance  FROM Transactions t
LEFT JOIN Accounts a ON t.account_id = a.account_id
RIGHT JOIN Customers c ON a.customer_id = c.customer_id
order by customer_id;

--3. Write a SQL query to increase the balance of a specific account by a certain amount.
UPDATE Accounts
SET balance = balance + 20000.00
WHERE account_id = 102;

--4. Write a SQL query to Combine first and last names of customers as a full_name.
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM Customers;

--5. Write a SQL query to remove accounts with a balance of zero where the account type is savings.
DELETE FROM transactions
WHERE account_id IN (SELECT account_id FROM accounts WHERE balance = 0.00 or account_type = 'savings');
DELETE FROM accounts
WHERE balance = 0 OR account_type = 'savings';

--6. Write a SQL query to Find customers living in a specific city.
SELECT * FROM Customers WHERE address='Chennai';

--7. Write a SQL query to Get the account balance for a specific account.
SELECT account_id,balance FROM Accounts WHERE customer_id = 2;

--8. Write a SQL query to List all current accounts with a balance greater than $1,000.
SELECT * FROM Accounts
WHERE account_type = 'current' AND balance > 1000;

--9. Write a SQL query to Retrieve all transactions for a specific account.
SELECT * FROM Transactions
WHERE account_id = 106;

--10. Write a SQL query to Calculate the interest accrued on savings accounts based on a given interest rate.
SELECT account_id, (balance*10)/100 AS interest_accrued FROM Accounts
WHERE account_type = 'savings';

--11. Write a SQL query to Identify accounts where the balance is less than a specified overdraft limit = 1000.
SELECT * FROM accounts
WHERE balance < 1000;

--12. Write a SQL query to Find customers not living in a specific city.
SELECT *FROM customers
WHERE address not like 'kolkata';

--Tasks 3: Aggregate functions, Having, Order By, GroupBy and Joins:

--1. Write a SQL query to Find the average account balance for all customers.
SELECT AVG(balance) AS average_balance FROM accounts;

--2. Write a SQL query to Retrieve the top 10 highest account balances.
SELECT TOP (10) * FROM accounts
ORDER BY balance DESC;

--3. Write a SQL query to Calculate Total Deposits for All Customers in specific date.
SELECT SUM(amount) AS total_deposits FROM transactions
WHERE transaction_type = 'deposit' AND transaction_date = '2024-03-01';

--4. Write a SQL query to Find the Oldest and Newest Customers.
SELECT top(1) customer_id as oldest,first_name,last_name,DOB FROM customers
ORDER BY DOB ASC;
SELECT top(1) customer_id as newest,first_name,last_name,DOB FROM customers
ORDER BY DOB DESC;

--5. Write a SQL query to Retrieve transaction details along with the account type.
SELECT t.*, a.account_type FROM transactions t
INNER JOIN accounts a ON t.account_id = a.account_id;

--6. Write a SQL query to Get a list of customers along with their account details.
SELECT c.*, a.account_id, a.account_type, a.balance FROM customers c
LEFT JOIN accounts a ON c.customer_id = a.customer_id;

--7. Write a SQL query to Retrieve transaction details along with customer information for a specific account.
SELECT t.*, c.* FROM transactions t
INNER JOIN accounts a ON t.account_id = a.account_id
INNER JOIN customers c ON a.customer_id = c.customer_id
WHERE t.account_id = 101;

--8. Write a SQL query to Identify customers who have more than one account.
SELECT customer_id, COUNT(*) AS num_accounts FROM accounts
GROUP BY customer_id
HAVING COUNT(*) > 1;

--9. Write a SQL query to Calculate the difference in transaction amounts between deposits and withdrawals.
SELECT 
    (SELECT SUM(amount) FROM transactions WHERE transaction_type = 'deposit') AS total_deposits,
    (SELECT SUM(amount) FROM transactions WHERE transaction_type = 'withdrawal') AS total_withdrawals,
    (SELECT SUM(amount) FROM transactions WHERE transaction_type = 'deposit') -
    (SELECT SUM(amount) FROM transactions WHERE transaction_type = 'withdrawal') AS transaction_difference;

--10. Write a SQL query to Calculate the average daily balance for each account over a specified period.
SELECT account_id,AVG(balance) AS average_daily_balance FROM accounts
GROUP BY account_id;

--11. Calculate the total balance for each account type.
SELECT account_type,SUM(balance) AS total_balance FROM accounts
GROUP BY account_type;

--12. Identify accounts with the highest number of transactions order by descending order.
SELECT account_id,COUNT(*) AS num_transactions FROM transactions
GROUP BY account_id
ORDER BY num_transactions DESC;

--13. List customers with high aggregate account balances, along with their account types.
SELECT c.customer_id,c.first_name,c.last_name,a.account_type,SUM(a.balance) AS total_balance
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id
GROUP BY c.customer_id,c.first_name,c.last_name,a.account_type,c.address
ORDER BY total_balance DESC;

--14. Identify and list duplicate transactions based on transaction amount, date, and account.
SELECT account_id,transaction_date,amount,COUNT(*) AS num_duplicates FROM transactions
GROUP BY account_id, transaction_date, amount
HAVING COUNT(*) > 1;

--Tasks 4: Subquery and its type:

--1. Retrieve the customer(s) with the highest account balance.
SELECT TOP(1) c.customer_id, c.first_name, c.last_name,a.balance FROM customers c
INNER JOIN accounts a ON c.customer_id = a.customer_id
ORDER BY a.balance DESC;

--2. Calculate the average account balance for customers who have more than one account.
SELECT customer_id,COUNT(*) AS num_accounts,SUM(balance) AS total_balance,sum(balance)/count(*) as total_average FROM accounts
GROUP BY customer_id
HAVING COUNT(*) > 1;

--3. Retrieve accounts with transactions whose amounts exceed the average transaction amount.
SELECT * FROM accounts a
WHERE EXISTS (SELECT * FROM transactions t WHERE t.account_id = a.account_id
GROUP BY t.account_id
HAVING AVG(t.amount) > (SELECT AVG(amount) FROM transactions));

--4. Identify customers who have no recorded transactions.
SELECT c.* FROM customers c
LEFT JOIN accounts a ON c.customer_id = a.customer_id
LEFT JOIN transactions t ON a.account_id = t.account_id
WHERE t.transaction_id IS NULL;

--5. Calculate the total balance of accounts with no recorded transactions.
SELECT customer_id,account_id,SUM(balance) AS balance_with_no_transactions
FROM accounts
WHERE account_id NOT IN (SELECT DISTINCT account_id FROM transactions)
group by customer_id,account_id;

--6. Retrieve transactions for accounts with the lowest balance.
SELECT * FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
WHERE a.balance = (SELECT MIN(balance) FROM accounts);

--7. Identify customers who have accounts of multiple types.
SELECT DISTINCT a1.customer_id,a1.account_id,a1.account_type,a1.balance FROM accounts a1
WHERE EXISTS (SELECT * FROM accounts a2 WHERE a1.customer_id = a2.customer_id AND a1.account_type <> a2.account_type);

--8. Calculate the percentage of each account type out of the total number of accounts.
SELECT account_type,COUNT(account_type) AS num_accounts, 
(COUNT(account_type) * 100 / (SELECT COUNT(account_type) FROM accounts)) AS percentage FROM accounts
GROUP BY account_type;

--9. Retrieve all transactions for a customer with a given customer_id.
SELECT t.* FROM transactions t
INNER JOIN accounts a ON t.account_id = a.account_id
WHERE a.customer_id = 1;

--10. Calculate the total balance for each account type, including a subquery within the SELECT clause.
SELECT account_type,(select SUM(balance) AS total_balance) FROM accounts
GROUP BY account_type;

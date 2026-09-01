🏧 ATM Machine Project
A simple ATM simulation built using Python. 
This mini project is designed for beginners to practice Python concepts such as loops, 
conditional statements, user input, variables, and basic validation.
📌 Features
🔐 Create a 4-digit PIN
✅ Validate that the PIN contains exactly 4 digits
💰 Check account balance
💵 Deposit money
🏧 Withdraw money
⚠️ Check for insufficient balance
❌ Handle invalid menu choices
🚪 Exit the ATM program

🛠️ Technologies Used
Python 3
input()
if / elif / else
while loop
Variables
String methods such as .isdigit()
⚙️ How It Works
When the program starts, the user is asked to create a 4-digit PIN.
CREATE YOUR 4-DIGIT PIN: 1234
PIN created successfully!

The program then displays the ATM menu:
1. CHECK BALANCE
2. DEPOSIT
3. WITHDRAW
4. EXIT

Before operating, the user must enter the correct PIN.
PIN Validation
The program uses:
if len(pin) == 4 and pin.isdigit():

This checks that:
The PIN contains exactly 4 characters
All characters are digits
For example:
1234  → Valid ✅
5678  → Valid ✅
123   → Invalid ❌
12345 → Invalid ❌
12a4  → Invalid ❌

💳 ATM Operations
1. Check Balance
The user can check their current account balance.
BALANCE: 1000

2. Deposit
The user can enter an amount to deposit.
Enter deposit amount: 500
After deposit amount: 1500

3. Withdraw
The user can withdraw money if they have enough balance.
Enter withdrawal amount: 300
Remaining balance after withdrawal: 1200

If the withdrawal amount is greater than the available balance:
Insufficient balance. You have only: 1200

4. Exit
The user can exit the ATM by selecting option 4.
THANK YOU FOR CHOOSING THIS ATM

▶️ How to Run
Step 1: Install Python
Make sure Python 3 is installed on your computer.
Check the installation using:

python --version

Step 2: Clone the Repository
git clone YOUR_REPOSITORY_URL

Step 3: Go to the Project Folder
cd ATM-Machine

Step 4: Run the Program
python atm.py

📂 Project Structure
ATM-Machine/
│
├── atm.py
└── README.md

🧠 Python Concepts Practised
This project helped practice:
Variables
while loops
if, elif, and else
User input
Type conversion
String methods
.isdigit()
len()
Basic error validation
Arithmetic operations
🚀 Future Improvements
Some features that could be added in the future:
🔢 Limit the number of incorrect PIN attempts
💳 Account number/card number
📜 Transaction history
💰 Multiple bank accounts
🔒 Hide the PIN while entering it
💾 Save balance and transactions to a file
🏦 Add multiple users
🧾 Generate a transaction receipt
👨‍💻 Author
BEEDHA RAJESH
If you found this project useful, feel free to ⭐ the repository!

📄 License
This project is created for learning and educational purposes

-----------------VERSION 2.0----------------
## 🚀 Version 2 – Updates

Version 2 improves the original ATM project by adding authentication, transaction tracking, fast cash withdrawal, PIN management, and card type selection.

### 🆕 New Features Added

#### 💳 1. Domestic / International Card Selection

The ATM now asks the user to select their card type before accessing the ATM.

```text
------ ATM CARD ------
1. DOMESTIC
2. INTERNATIONAL
```

The program displays a different welcome message depending on the selected card type.

---

#### 🔐 2. PIN Authentication with 3 Attempts

Version 2 now allows the user a maximum of **3 PIN attempts**.

```text
ENTER YOUR 4 DIGIT PIN: 1111
WRONG PIN!
Attempts remaining: 2
```

If all three attempts are incorrect:

```text
TOO MANY WRONG ATTEMPTS!
YOUR ACCOUNT IS LOCKED.
```

This improves the basic security of the ATM simulation.

---

#### 🔢 3. Improved PIN Validation

The PIN is validated using:

```python
if len(pin) == 4 and pin.isdigit():
```

This ensures that:

* PIN contains exactly 4 digits
* Only numbers are accepted
* Invalid PIN formats are rejected

Examples:

```text
1234  → Valid ✅
123   → Invalid ❌
12345 → Invalid ❌
12a4  → Invalid ❌
```

---

#### ⚡ 4. Fast Cash Withdrawal

A new **Fast Cash** option has been added.

```text
====== FAST WITHDRAW ======

1. ₹500
2. ₹1000
3. ₹2000
4. ₹5000
```

The user can quickly select a predefined withdrawal amount instead of entering the amount manually.

The selected transaction is also recorded in the transaction history.

---

#### 🔑 5. Change PIN

Users can now change their existing PIN.

The program asks for:

```text
ENTER CURRENT PIN:
ENTER NEW 4 DIGIT PIN:
CONFIRM NEW PIN:
```

The program checks that:

* Current PIN is correct
* New PIN contains exactly 4 digits
* New PIN and confirmation PIN match
* New PIN is different from the current PIN

If everything is correct:

```text
PIN CHANGED SUCCESSFULLY!
```

---

#### 📜 6. Transaction History / Mini Statement

Version 2 introduces transaction tracking using a Python list:

```python
transactions = []
```

Transactions are added using:

```python
transactions.append()
```

For example:

```python
transactions.append("deposite:" + str(amount))
transactions.append("Withdraw:" + str(Withdraw_amount))
transactions.append("Fast Withdraw ₹" + str(amount))
```

The user can view the transaction history through **Mini Statement**.

Example:

```text
========== MINI STATEMENT ==========

deposite:500
Withdraw:200
Fast Withdraw ₹500

------------------------------------
CURRENT BALANCE: ₹800
====================================
```

---

#### 🛡️ 7. Improved Deposit Validation

The program now checks whether the deposit amount is greater than zero.

```python
if amount > 0:
    balance += amount
else:
    print("Please enter valid amount !")
```

This prevents invalid deposits such as:

```text
0      ❌
-500   ❌
500    ✅
```

---

#### 🛡️ 8. Improved Withdrawal Validation

The withdrawal feature now checks the available balance before completing the transaction.

```python
if balance >= Withdraw_amount:
    balance -= Withdraw_amount
```

If the user tries to withdraw more money than available:

```text
INSUFFICIENT BALANCE
YOU HAVE ONLY: ₹1000
```

---

## 📋 Version 2 ATM Menu

The original ATM menu has been expanded.

### Version 1

```text
1. CHECK BALANCE
2. DEPOSIT
3. WITHDRAW
4. EXIT
```

### Version 2

```text
-------- ATM MENU ----------

1. CHECK BALANCE
2. DEPOSIT
3. WITHDRAW
4. FAST CASH
5. PIN CHANGE
6. MINI STATEMENT
7. EXIT
```

---

## 🧠 New Python Concepts Practised in Version 2

In addition to the concepts learned in Version 1, Version 2 introduces:

* Lists
* `.append()`
* Multiple validation conditions
* PIN authentication
* Attempt counters
* `continue`
* Transaction tracking
* Nested `if` statements
* Dynamic variable updates
* String concatenation
* Basic authentication logic

---

## 🔄 Version 1 vs Version 2

| Feature                       | Version 1 | Version 2 |
| ----------------------------- | :-------: | :-------: |
| PIN validation                |     ✅     |     ✅     |
| Balance checking              |     ✅     |     ✅     |
| Deposit                       |     ✅     |     ✅     |
| Withdrawal                    |     ✅     |     ✅     |
| Insufficient balance check    |     ✅     |     ✅     |
| 3 PIN attempts                |     ❌     |     ✅     |
| Domestic / International card |     ❌     |     ✅     |
| Fast Cash                     |     ❌     |     ✅     |
| PIN Change                    |     ❌     |     ✅     |
| Transaction History           |     ❌     |     ✅     |
| Mini Statement                |     ❌     |     ✅     |
| Deposit validation            |   Basic   |  Improved |
| Withdrawal validation         |   Basic   |  Improved |

---

## 📌 Version 2 Project Status

**Current Version:** `v2.0`

The ATM simulation now provides a more complete banking experience while continuing to use beginner-level Python concepts.

### 🔮 Future Improvements – Version 3

Possible future features:

* 💳 Account number / card number
* 👥 Multiple users
* 🏦 Multiple bank accounts
* 💾 Save account data using files
* 📂 Permanent transaction history
* 🕐 Add date and time to transactions
* 🧾 Generate ATM receipts
* 🔒 Hide PIN while entering
* 💸 Money transfer between accounts
* 💰 Daily withdrawal limits
* 🏧 ATM cash availability
* 🛡️ Better error handling using `try-except`
* 🧩 Convert the project into functions
* 🏗️ Implement Object-Oriented Programming (OOP)
* 🗄️ Connect the project to MySQL

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
This project is created for learning and educational purposes.




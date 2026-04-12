# x = input("Enter number 1: ")
# y = input("Enter number 2: ")

# d = 0

# try:
#     d = int(x)/int(y)
#     a = 'baby yoda' + 56
# # except ZeroDivisionError as ze:
# #     print("Exception ocurred",  ze)
# #     d = -1
# # except TypeError as te:
# #     print("Exception ocurred: ", te)
# #     d = -1
# except Exception as e:
#     print("Generic Exception:", e)

# print("Division is: ", d)

# file = None

# try:
#     file = open("example.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("Error: The file was not found")
# finally:
#     if file:
#         file.close()
#     print("File closed.")

class InsufficientFunds(Exception):
    pass

balance = 0

def deposit(amount):
    global balance
    if amount <= 0:
        raise ValueError("Amount must be positive")
    balance += amount

def withdraw(amount):
    global balance
    if amount > balance:
        raise InsufficientFunds(f"Not enough funds. Current balance {balance}")
    balance -= amount

deposit(10)
deposit(7)
withdraw(50)
print(balance)
import csv

# Creating a complex bank account 
class BankAccount:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.balance = 0.0

  def deposit (self, amount: float):
    self.balance += amount 
    print(f"You deposited {amount} /nBalance: {self.balance:.2f}")

  def withdraw (self, amount: float):
    if self.balance < amount:
      print(f"insufficient funds")
    else:
      self.balance -= amount
      print(f"You withdrew {amount} /nBalance: {self.balance:.2f}")
    
  def transfer (self, recipient_acct, amount: float):
    if self.balance < amount:
     print(f"insufficient funds")
    else:
      self.balance -= amount 
      recipient_acct.balance += amount
      print(f"You successfully transferred {amount:.2f} to {recipient_acct.username}")

  def checkBalance (self):
   print(f"Your account balance is {self.balance:.2f}")



# bob = BankAccount("bob","1234")
# bob.checkBalance()

# Entry platform for the console Bank Application 

class BankApp:
  def __init__(self):
    # These are class attributes
    self.users = self.load_file()
    self.current_user = None

  def save_to_File (self, filename="bank_details.csv"):
    with open(filename, mode='w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([ "username", "password", "balance"]) # for the header\\\\\\\\\\\\

      for username, data in self.users.items():
       writer.writerow( [data.username, data.password, data.balance]) 

  def load_file (self, filename='bank_details.csv'):
    users = {}
    try:
      with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
          account = BankAccount(
             row['username'], row['password'])
          
          account.balance = float(row['balance'])
          users[row['username']] = account
    except FileNotFoundError:
       print(f"{filename} not found. Starting with an empty user list.")
    return users
    

  def register(self):
    username = input(f"Enter your preferred username: ")
    if username in self.users:
      print(f"This username has been used")
      return
    password = input(f"Enter a password: ")
    self.users[username] = BankAccount(username, password)
    self.save_to_File()
    print(f"your account has successfully registered")
  
  def login(self):
    username = input(f"Enter your username: ")
    password = input(f"Enter your password: ")
    user = self.users.get(username)
    print(user.password)
    if user and user.password == password:
      self.current_user = user

      print(f"{self.current_user.username} has successfully logged in")

      while(True):
        print("1. deposit")
        print("2. withdraw")
        print("3. make a transfer")
        print("4. check balance")
        print("0. logout")
        print("Enter a number from 1 to 6 to perform an operation") 
        choice = input("")

        if choice == "1":
          self.deposit()
        elif choice == "2":
          self.withdraw()
        elif choice == "3":
          self.transfer()
        elif choice == "4":
          self.checkBalance()
        elif choice == "0":
          break
        else:
          print("Please enter a number from 0 to 3")
      
    else:
      print(f"invalid credentials")
  

  def deposit(self):
    amount = float(input("enter the amount to be deposited "))
    self.current_user.deposit(amount)
    self.save_to_File()
  

  def withdraw(self):
    amount = float(input("Enter the amount to be withdrawn "))
    self.current_user.withdraw(amount)
    self.save_to_File()

  def transfer(self):
    amount = float(input("Enter the amount you want to transfer "))
    recipient = input("Enter the recipient_name you want to transfer ")
    recipient_acct = self.users.get(recipient)
    self.current_user.transfer(recipient_acct, amount )
    self.save_to_File()

  def checkBalance(self):
    balance = self.current_user.balance
    print(f"Your balance is {balance}")
  
  def logout(self):
    print(f"logged out ")

  def run(self):
    
    while (True):
      print("*********Bank App********")
      print()
      print("1. register a bank account")
      print("2. login in to your bank account")
      print("0. exit")
      print("Enter a number from 1 to 6 to perform an operation")
      choice = input("")

      if choice == "1":
        self.register()
      elif choice == "2":
        self.login() 
      elif choice == "0":
        break
      else:
        print(f"please enter a valid menu number")

if __name__ == "__main__":
  menu = BankApp()
  menu.run()
  
  

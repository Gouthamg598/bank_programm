#Code for IBS ATM Process 


print("WELCOME TO SBI ATM")
print("=====================")
print('''Select your Language 
    1.English 
    2.Hindi
    3.Telugu''')

z=1
t=[]
min=5000
ac_min=5000
t.append(ac_min)
a=int(input("Choose your option:"))
for i in range(z):
    if(a==1):
        print("You are selected English")
        pass
    elif(a==2):
        print("You are selected Hindi")
    elif(a==3):
        print("You are selected Telugu")
    else:
        print("Warning:Select correct option")
        print("Transaction Failed")
        print("=====================")
        print("Thanks for visiting")
        break 
    b=int(input("Enter your PIN:"))
    if(b>=1000 and b<=9999):
        print("Log in Successful")
        pass
    else:
        print("Incorrect PIN")
        print("Transaction Failed")
        print("=====================")
        print("Thanks for visiting")
        break
    print('''Select account Type 
    1.savings account
    2.current account
    ''')
    c=int(input("Choose your option:"))
    if(c==1):
        print("Welcome to Savings Account")
    elif(c==2):
        print("Welcome to Current Account")
    else:
        print("Transaction Failed")
        print("=====================")
        print("Thanks for visiting")
        print("----------------------")
        break
    for i in range(6):
        print('''Particulars
        1.Diposit 
        2.Withdraw
        3.Balence Enquiry
        4. To cancel the transaction''')
        d=int(input("Choose your option:"))
        if(d==1):
            dip=int(input("Enter amount to deposit:"))
            x=t[0]+dip
            print("Available Amount is:",x)
            print("Transaction Successful")
            print("=====================")
            print("Thanks for visiting")
            print("----------------------")
            ac_min=x
            t.insert(0,ac_min)
        elif(d==2):
            wit=int(input("Enter amount to Withdraw:"))
            if 5000<=abs(wit-ac_min):
                print("Recived amount:",wit)
                y=t[0]-wit
                t.insert(0,y)
                print("Available Amount is:",y)
                print("Transaction Successful")
                print("=====================")
                print("Thanks for visiting")
                print("----------------------")
            else:
                print("No sufficient balance\nmin balance should be maintain 5000\nyour balance is ",t[0])
        elif(d==3):
            print("Available Amount is:",t[0])
            print("Transaction Successful")
            print("=====================")
            print("Thanks for visiting")
            print("----------------------")
        else:
            print('press ctrl+c to terminate the transaction')
            cancel=input('press ctrl+c')
    
    
    
    
    

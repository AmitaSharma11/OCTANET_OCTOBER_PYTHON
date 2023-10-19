# ATM INTERFACE

n=input("Enter your User-Id please:")
p=int(input("Enter your 4 digit PIN please:"))

def atm():
    names=["Anish_Kumar","Priya_Singh","Rahul_Singhania","Rohan_Oberai","Jiya_Kapoor"]
    pin=[1234,4567,6789,9012,2345]

    for i in range (len(names)):
        if(n==names[i] and p==pin[i]):
            print("Successful login.")

            balance = [1000,1200,1500,800,3000]
            
            def transactionHistory():
                account_number=["XXXXXX8907","XXXXXX2045","XXXXXX9754","XXXXXX1340","XXXXXX0975"]
                date=[ "01.10.2023","05.10.2023","02.10.2023","03.10.2023","08.10.2023" ]
                time=[ "10:00 AM","15:00 PM","12:00 NOON","18:00 PM","11:00 AM" ]
                available_balance=[ 800,2500,1500,500,3500]
                print("Your transaction history is as follow:")
                print("Account holder name:",names[i])
                print("Account number:",account_number[i])
                print("Last transaction date:",date[i])
                print("Last transaction time:",time[i])
                print("Available Balance now:",available_balance[i])

            def withdraw():
                amount_withdraw=int(input("Enter the amount you want to withdraw:"))
                if balance[i]<amount_withdraw:
                    print("Low Balance !!! Money can't be withdraw")
                    print("Do you want to deposit money then withdraw:")
                    choice0=int(input("1.Yes \n 2.No \n Enter your choice:"))
                    if(choice0==1):
                        deposit()
                        withdraw()
                    else:
                        print("You chose not to deposit money and continue !!!")
                        exit
                else:
                    balance[i]=balance[i]-amount_withdraw
                    print("Money Successfully withdraw")
                    print("Now,the available balance is:",balance[i])

            def deposit():
                amount=int(input("Enter the amount you want to deposit:"))
                balance[i]=balance[i]+amount
                print("Congrates,amount deposited !!!")
                print("The balance now is:",balance[i])

            def transfer():
                reciever_name=input("Enter the account holder name for money tranfer:")
                reciever_account=input("Enter the account number for money tranfer:")
                amount_transfer=int(input("Enter the amount to transfer:"))
                if balance[i]<amount_transfer:
                    print("Low Balance !!! Money can't be tranferred")
                    choice0=int(input("1.Yes \n 2.No \n Enter your choice:"))
                    if(choice0==1):
                        deposit()
                        transfer()
                    else:
                        print("You chose not to deposit money and continue !!!")
                        exit
                else:
                    balance[i]=balance[i]-amount_transfer
                    print("Congrates,money transferred")
                    print("Available Balance now:",balance[i])

            while(1):
                choice=int(input(" 1.Transaction History \n 2.Withdraw \n 3.Deposit \n 4.Transfer \n 5.Quit \n Enter your choice:"))
                if(choice==1):
                    transactionHistory()
                elif(choice==2):
                    withdraw()
                elif(choice==3):
                    deposit()
                elif(choice==4):
                    transfer()
                elif(choice==5):
                    exit(0)
                else:
                    print("Invalid Input")
                    break
            
    else:
        print("Authentication failed.Please check your input.")

ATM=atm()
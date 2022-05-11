principal = int(input("Enter Principal? "))
rate = int(input("Enter rate of interest? "))
time = int(input("Enter Time? "))

def simple_interest(principal,rate,time):
    print("Simple Interest",(principal*time*rate)/100)

simple_interest(principal, rate,time)
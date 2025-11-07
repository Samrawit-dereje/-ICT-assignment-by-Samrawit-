net_income= float(input("enter your income:"))
if net_income<=2000:
    print((net_income) - (net_income * 0))
elif 2001<=net_income<=4000:
    print((net_income) - (net_income *0.15))
elif 4001<=net_income<=7000:
    print((net_income) - (net_income * 0.2))
elif 7001<=net_income <=10000:
    print((net_income) - (net_income * 0.25))
    
elif 10001 <=net_income <= 14000:
    print((net_income) - (net_income * 0.3))
elif net_income>= 14001:
    print((net_income) - (net_income * 0.35))
else: 
    print("invalid")



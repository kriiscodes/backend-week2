print("Bill splitter")
total = float(input("Total bill in Naira: "))
people = int(input("Number of people: "))
share = total / people
if people <= 0:
    print("The number of people must be more than 0")
else:
    print(f'Each person pays \u20a6{share:,.2f}')
    

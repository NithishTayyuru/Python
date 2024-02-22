print("Welcome to the tip Calculator")
total_bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10,12 or 15?"))
persons=int(input("How many persons bill to be shared?"))
pay=round((total_bill+(total_bill*(tip/100)))/persons,2)
print(f"Each person should pay: ${pay}")
            

## What you should you have to take a input from User
## Total Rent 
## Total Electric Bill
# Charge per Unit

rent = int(input("Enter the Total Rent of the Hostel = "))
food = int(input("Enter the Total price for food Orderd =")) 
electricity_spend =int(input("Electricity Meter Reading  ="))
Charge_per_Unit = int(input("Enter the Charge per Unit ="))
Number_Persion= int(input(" Enter the Number of Persion in the Hostal = "))

Total_Rent = (rent + food + (electricity_spend*Charge_per_Unit))/(Number_Persion)
print(f'The Rent of Each Persion :,{Total_Rent}')
import time
'''Define Menue of Products'''

Menu ={
    "Chai":7,
    "Sammosa": 9,
    "Burger" : 15,
    "Momo" :18,
    "Panner Roll":50,
    "Chat":30
}

# Then Great The Coustomer



print("Welcome to Maysoor Cafa,We Have")
time.sleep(1)


for key in Menu:
    print(f'{key} :   {"\u20B9"}{Menu[key]}')
    time.sleep(1)

#  Assigning value to the total value items
OrderTotal = 0

Item_1 =input("What you like to Have ,Sir/Mam :")
for i in Item_1.split(","):
        if i in Menu:
            OrderTotal+=Menu[i]
        else:
            print(f'Sorry Sir {i} is Not in Menu')
    
Item_2 = input("Any thin Else Sir  ")

if Item_2 in Menu:
    OrderTotal +=Menu[Item_2]
elif Item_2 == "No"or Item_2=="NO":
    print("Sure Sir")
else:
    print(f'Sorry Sir, {Item_2} in Menu')

    
    
print(f'Thank You ,Sir Your Order in just 10 Min.Order Price {"\u20B9"}{OrderTotal}')

 







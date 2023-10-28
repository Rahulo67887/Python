foods=[]
prices=[]
total=0

while(1):
    food=input(f"Enter a food you want to buy(enter q to quit):");
    if(food.lower()=='q'):
        break
    else:
        foods.append(food)
        price=float(input(f"Enter the price of {food}:₹"))
        prices.append(price)
        
print("------YOUR CART------")

for food in foods:
    print(food, end=" ")
    
print()

for price in prices:
    total+=price
    
print(f"Total Price:₹{total}")
        
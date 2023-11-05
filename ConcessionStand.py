menu={"pizza":460,
      "chips":30,
      "coke":60,
      "burger":100,
      "aaloo patties":50,
}

cart=[]
total=0

print("--------MENU--------")
for key, value in menu.items():
    print(f"{key:15}:₹{value}")
print("--------------------")

while(1):
    food=input("Select an item(enter q to quit):").lower()
    if food=='q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
    
for food in cart:
    total+=menu.get(food)
    print(food, end=" ")
    
print(f"Total is ₹{total:.2f}")


total = 0
print("GROCERY STORE BILLING SYSTEM")
for i in range(1, 6):
    print(f"\nItem {i}")
    
    
    price = float(input("Enter price of item: "))
    
   
    quantity = int(input("Enter quantity of item: "))
    
   
    item_total = price * quantity
    
    
    total += item_total


print(f"Original Total Amount: Rs. {total:.2f}")


if total > 100:
    discount = total * 0.10
    final_amount = total - discount
    print(f"Discount Applied (10%): Rs. {discount:.2f}")
else:
    discount = 0
    final_amount = total
    print("No Discount Applied.")


print(f"Final Payable Amount: Rs. {final_amount:.2f}")

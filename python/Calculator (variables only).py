price    =  1500
quantity =  3
discount =  0.10
tax      =  0.18

#Calculate total before discount
before_discount = price * quantity 

#before tax
before_tax = before_discount - (before_discount * discount)

#after discount 
after_discount  = before_discount - (before_discount * discount)

#after tax
all_apply = after_discount + (after_discount * tax)

print(f"Price : {price}\nQuantity : {quantity}\nTax apply : {tax}\nDiscount : {discount}")

print("Calculate total before discount :",before_discount)
print("Calculate total before Tax :",before_tax)
print("Calculate total after Apply discount :",after_discount)
print("Calculate total after Apply Tax :",all_apply)
print("Your final total bill :",all_apply)

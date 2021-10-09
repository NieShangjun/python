items = int(input("Number of items: "))
while items<0:
    if items<0:
          print("Invalid number of items!")
          items = int(input("Number of items: "))
total_i = 0
for i in range(1,4,1):
 i = float(input("Price of item:"))
 total_i += i
if total_i > 100:
         total_i = 0.9 * total_i
         total_i1 = round(total_i,2)
         print(f"Total price for 3 items is ${total_i1}")
elif 0<total_i<=100:
         print(f"Total price for 3 items is ${total_i}")




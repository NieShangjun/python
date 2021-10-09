finished = False
result = 0
while not finished:
    try:
        result = int(input("Please input an integer: "))
    except ValueError:
        print("Please enter a valid integer.")

print("Valid result is:", result)
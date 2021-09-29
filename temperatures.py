def main():
    MENU = """C - Convert Celsius to Fahrenheit
            F - Convert Fahrenheit to Celsius
            Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def Celsius_to_Fahrenheit():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32


def Fahrenheit_to_Celsius():
    global celsius
    celsius = 5 / 9 * (fahrenheit - 32)


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        Fahrenheit_to_Celsius()
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit:"))
        Fahrenheit_to_Celsius()
        print("Result: {:.2f} F".format(celsius))
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

main()

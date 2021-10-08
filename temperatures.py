def Celsius_to_Fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def Fahrenheit_to_Celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius
def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
             celsius = float(input("Celsius: "))
             C=Celsius_to_Fahrenheit(celsius)
             print("Result:{:.2f} F".format(C))
        elif choice == "F":
             fahrenheit = float(input("Fahrenheit:"))
             F=Fahrenheit_to_Celsius(fahrenheit)
             print("Result:{:.2f} C".format(F))
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()

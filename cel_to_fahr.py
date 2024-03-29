print("\t\tWelcome to PyTemp!")
print("\t\tCreated by Logan Tolbert\n")

def main():
    while True:
        choice = input("""\tWhat temperature would you like to convert:\n
        1) Celsius to fahrenheit\n
        2) Fahrenheit to celsius\n
        Q) Quit\n
        >>> """)
        if choice == "1":
            c = (float(input("Enter your temperature(C):\n>>> ")))
            print(f"\nCelsius: {c}C\nFahreheit: {convertToFahrenheit(c)} F\n")

        elif choice == "2":
            f = (float(input("Enter your temperature(F):\n>>> ")))
            print(f"\nFahrenheit: {f} F\nCelsius: {convertToCelsius(f)} C\n")
        elif choice.lower() == "q":
            exit()

def convertToFahrenheit(celsius):
    return("{:.2f}".format((celsius * (9 / 5) + 32)))
    

def convertToCelsius(fahrenheit):
    return("{:.2f}".format((fahrenheit - 32) * (5 / 9)))


main()
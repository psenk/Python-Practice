c_temp, f_temp = 0, 0 
user_input = ""
loop = True

print("""
Which temperature would you like to convert?
1. Fahrenheit to Celsius
2. Celsius to Fahrenheit
""")

while loop:
    user_input = int(input("Select one: "))

    if user_input == 1:
        f_temp = float(input("Input temperature in Fahrenheit: "))
        c_temp = (f_temp - 32) * (5 / 9)
        print(f"{f_temp} is {c_temp} degrees in Celsius.")
        loop = False

    elif user_input == 2:
        c_temp = float(input("Input temperature in Celsius: "))
        f_temp = (c_temp * (9 / 5) + 32)
        print(f"{c_temp} is {f_temp} degrees in Fahrenheit.")
        loop = False

    else:
        print("Invalid choice.")

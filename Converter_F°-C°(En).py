#Convertisseur degrés Farenheit en degrés Celsuis

run = True

while run == True: 
    temp_F = float(input("Enter a temperature in Fahrenheit degres (no need to write the symbol)"))
    temp_C = ( ((temp_F) - 32)/1.8 )
    print(f"The temperature in Celsius of {temp_F}°F is {temp_C}°C.")
    print("")
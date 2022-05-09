def gramsToTablespoons():
    tablespoon = 0.08
    validation = True
    while validation == True:
        try:
            convert = input("\nHow many grams do you want to convert to tablespoons? (Without decimals): ")
            convert = int(convert)
            print(f"\n{convert} grams means {convert * tablespoon} tablespoons")
            validation = False
        except ValueError:
            print("\n***Invalid input, it must be a number, try again!***")    


# -------------------------------------------------------------------------------------------------------


def metersToKilometers():
    validation = True
    while validation == True:
        try:
            convert = input("\nHow many meters do you want to convert to kilometers? (Without decimals): ")
            convert = int(convert)
            print(f"\n{convert} meters means {convert / 1000} kilometers")
            validation = False
        except ValueError:
            print("\n***Invalid input, it must be a number, try again!***")   


# -------------------------------------------------------------------------------------------------------


def kilometersToMeters():
    validation = True
    while validation == True:
        try:
            convert = input("\nHow many kilometers do you want to convert to meters? (Without decimals): ")
            convert = int(convert)
            print(f"\n{convert} kilometers means {convert * 1000} meters")
            validation = False
        except ValueError:
            print("\n***Invalid input, it must be a number, try again!***")


# -------------------------------------------------------------------------------------------------------


def kilogramsToTonnes():
    validation = True
    while validation == True:
        try:
            convert = input("\nHow many kilograms do you want to convert to tonnes? (Without decimals): ")
            convert = int(convert)
            print(f"\n{convert} kilograms means {convert / 1000} tonnes")
            validation = False
        except ValueError:
            print("\n***Invalid input, it must be a number, try again!***")    


# -------------------------------------------------------------------------------------------------------


def tonnesToKilograms():
    validation = True
    while validation == True:
        try:
            convert = input("\nHow many tonnes do you want to convert to kilograms? (Without decimals): ")
            convert = int(convert)
            print(f"\n{convert} tonnes means {convert * 1000} kilograms")
            validation = False
        except ValueError:
            print("\n***Invalid input, it must be a number, try again!***")


# -------------------------------------------------------------------------------------------------------


def monthsToYears():
    validation = True
    while validation == True:
        try:
            convert = input("\nHow many months do you want to convert to years? (Without decimals): ")
            convert = int(convert)
            print(f"\n{convert} months means {int(convert / 12)} year(s)")
            validation = False
        except ValueError:
            print("\n***Invalid input, it must be a number, try again!***")


# -------------------------------------------------------------------------------------------------------


def yearsToMonths():
    validation = True
    while validation == True:
        try:
            convert = input("\nHow many years do you want to convert to months? (Without decimals): ")
            convert = int(convert)
            print(f"\n{convert} years means {convert * 12} months")
            validation = False
        except ValueError:
            print("\n***Invalid input, it must be a number, try again!***")


# -------------------------------------------------------------------------------------------------------


def fahrenheitToCelsius():
    validation = True
    while validation == True:
        try:
            convert = input("\nConvert Fahrenheit to Celsius (Without decimals): ")
            convert = int(convert)
            print(f"\n{convert} °F means {str(round((convert - 32) * 5 / 9, 1))} °C")
            validation = False
        except ValueError:
            print("\n***Invalid input, it must be a number, try again!***")


# -------------------------------------------------------------------------------------------------------


def celsiusToFahrenheit():
    validation = True
    while validation == True:
        try:
            convert = input("\nConvert Celsius to Fahrenheit (Without decimals): ")
            convert = int(convert)
            print(f"\n{convert} °C means {str(round((convert * 9 / 5) + 32, 1))} °F")
            validation = False
        except ValueError:
            print("\n***Invalid input, it must be a number, try again!***")


# -------------------------------------------------------------------------------------------------------


def centimetersToMeters():
    validation = True
    while validation == True:
        try:
            convert = input("\nHow many centimeters do you want to convert to meters? (Without decimals): ")
            convert = int(convert)
            print(f"\n{convert} centimeters means {convert / 100} meters")
            validation = False
        except ValueError:
            print("\n***Invalid input, it must be a number, try again!***")    


# -------------------------------------------------------------------------------------------------------


def metersToCentimeters():
    validation = True
    while validation == True:
        try:
            convert = input("\nHow many meters do you want to convert to centimeters? (Without decimals): ")
            convert = int(convert)
            print(f"\n{convert} meters means {convert * 100} centimeters")
            validation = False
        except ValueError:
            print("\n***Invalid input, it must be a number, try again!***")


# -------------------------------------------------------------------------------------------------------

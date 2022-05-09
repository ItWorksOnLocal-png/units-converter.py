# Importing functions
import time
import os
from title import title
from goodbye_message import goodbye
from conversions import gramsToTablespoons
from conversions import metersToKilometers
from conversions import kilometersToMeters
from conversions import kilogramsToTonnes
from conversions import tonnesToKilograms
from conversions import monthsToYears
from conversions import yearsToMonths
from conversions import fahrenheitToCelsius
from conversions import celsiusToFahrenheit
from conversions import centimetersToMeters
from conversions import metersToCentimeters


# Main Function
def main():
    title()

    print('''
    (1) Convert Grams to Tablespoons
    (2) Convert Meters to Kilometers
    (3) Convert Centimeters to Meters
    (4) Convert Meters To Centimeters
    (5) Convert Kilometers to Meters
    (6) Convert Kilograms to Tonnes
    (7) Convert Tonnes to Kilograms
    (8) Convert Months to Years
    (9) Convert Years To Months
    (10) Convert Fahrenheit to Celsius
    (11) Convert Celsius To Fahrenheit
    (0) Quit Program
    ''')

    validation = True
    while validation:
        try:
            choose_option = input("\nChoose your option: ")  # User input
            print("\n-------------------------------------------------------------------------------------------------------")
            choose_option = int(choose_option)

            if choose_option > 11:  # Checks if choice is out of range
                print("\n***That option is invalid, try again!***")
                print("\n-------------------------------------------------------------------------------------------------------")

            if choose_option == 0:
                # print("\n***Goodbye!***")
                os.system('cls')
                goodbye()
                time.sleep(1)
                quit()

            elif choose_option == 1:
                os.system('cls')
                gramsToTablespoons()
                validation = False
                print("\nPress any key to exit...")
                os.system("pause >nul")

            elif choose_option == 10:
                os.system('cls')
                fahrenheitToCelsius()
                validation = False
                print("\nPress any key to exit...")
                os.system("pause >nul")

            elif choose_option == 11:
                os.system('cls')
                celsiusToFahrenheit()
                validation = False
                print("\nPress any key to exit...")
                os.system("pause >nul")

            elif choose_option == 2:
                os.system('cls')
                metersToKilometers()
                validation = False
                print("\nPress any key to exit...")
                os.system("pause >nul")

            elif choose_option == 3:
                os.system('cls')
                centimetersToMeters()
                validation = False
                print("\nPress any key to exit...")
                os.system("pause >nul")

            elif choose_option == 4:
                os.system('cls')
                metersToCentimeters()
                validation = False
                print("\nPress any key to exit...")
                os.system("pause >nul")

            elif choose_option == 5:
                os.system('cls')
                kilometersToMeters()
                validation = False
                print("\nPress any key to exit...")
                os.system("pause >nul")

            elif choose_option == 6:
                os.system('cls')
                kilogramsToTonnes()
                validation = False
                print("\nPress any key to exit...")
                os.system("pause >nul")

            elif choose_option == 7:
                os.system('cls')
                tonnesToKilograms()
                validation = False
                print("\nPress any key to exit...")
                os.system("pause >nul")

            elif choose_option == 8:
                os.system('cls')
                monthsToYears()
                validation = False
                print("\nPress any key to exit...")
                os.system("pause >nul")

            elif choose_option == 9:
                os.system('cls')
                yearsToMonths()
                validation = False
                print("\nPress any key to exit...")
                os.system("pause >nul")

        except ValueError:  # Checks if the user input is an integer
            print("***That's not a valid choice, try again!***")

        except KeyboardInterrupt: # If the user triggered a KeyboardInterrupt Exception, the application exits
            os.system('cls')
            print("KeyboardInterrupt exception caught, exiting...")
            time.sleep(2)
            quit()


if __name__ == "__main__":
    main()

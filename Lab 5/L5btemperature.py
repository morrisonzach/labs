#
#   purpose: make temperature conversions between F and C
#   author: zachary morrison
#   date written: 10/22/2020
#   Version: 1.0.0
#

#   constants
FREEZE = 32

#   functions


def toCelcius(temp):
    return (temp - FREEZE) * (5 / 9)


def toFahrenheit(temp):
    return (temp * 9 / 5) + FREEZE

#   main function


def main():
    print("This program can convert temperatures between Fahrenheit and Celcius!")
    print("=====================================================================")
    going = True
    while (going):
        conv = str(input(
            "\nEnter whether you're gonna be starting with Celcius or Fahrenheit [C, F, or exit]: "))
        if (conv.lower() == 'exit'):
            going = False
            print("\nexiting...")
        if (conv.lower() != 'c' and conv.lower() != 'f'):
            going = False
            print("\ninvalid input!!!")
        temp = float(
            input("\nEnter the temperature that you'd like to convert: "))
        if (conv.lower() == 'c'):
            print("\nconverting " + str(temp) +
                  "°C to °F...\nis equal to " + format(toFahrenheit(temp), ".1f") + "°F")
        else:
            print("\nconverting " + str(temp) +
                  "°F to °C...\nis equal to " + format(toCelcius(temp), ".1f") + "°C")

        print("-----------------------------------------------------")
        again = str(
            input("would you like to convert another temperature? [y, n] "))
        if (again != 'y' and again != 'n'):
            going = False
        if (again == 'n'):
            going = False


main()

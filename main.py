"""
Made by: Muhammad Ali
"""

import sys
import time

while True:
    # Dangerous Code
    try:
        number = int(input("Num: "))
    except ValueError:
        print("Please enter a valid number")
        time.sleep(2)
        sys.exit()
    except Exception as e:
        print("Error: "+str(e))
        time.sleep(2)
        sys.exit()
    try:
        times = int(input("Times: "))
    except ValueError:
        print("Please enter a valid number")
        time.sleep(2)
        sys.exit()
    except Exception as e:
        print("Error: "+str(e))
        time.sleep(2)
        sys.exit()

    # Safety

    if number == 0:
        print("Number can not be 0")
        time.sleep(2)
        sys.exit()
    elif times == 0:
        print("Times can not be 0")
        time.sleep(2)
        sys.exit()


    def display_table(num, tms):
        print("Table of "+str(num))
        for i in range(num, num*tms+1, num):
            print(str(num)+"x"+str(int(i/num))+"="+str(i))
            time.sleep(1)


    display_table(number, times)

    try:
        again = input("Run again? (y,n) ")
    except ValueError:
        print("Please enter y or n")
        time.sleep(2)
        print("Program will still close")
        time.sleep(2)
        sys.exit()

    again.lower()


    # Infinite repeat code
    if again == 'y':
        continue
    elif again == 'n':
        break
    else:
        print("Please enter y or n")
        time.sleep(1)
        print("The program will however still close.")
        time.sleep(1)
        break
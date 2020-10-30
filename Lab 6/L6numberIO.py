#
#   purpose: average numbers from input file
#   author: zachary morrison
#   date written: 10/29/2020
#   Version: 1.0.0
#

#   imports
import sys

#   file being read


def readNumbers():
    nums = []
    try:
        f = open("numbers10.txt", "rt")
        lines = f.readlines()
        f.close()
        for line in lines:
            nums.append(int(line.rstrip()))
    except IOError as e:
        print(e)
    except ValueError as e:
        print("No valid integer in line:", e)
    except:
        print("unexpected error:", sys.exc_info()[0])
    return nums

#   finding the avg of a number array


def findAvg(numArray: [int]):
    avg = 0
    for num in numArray:
        avg += num
    avg /= len(numArray)
    return avg


#   printing the avg of the number array gotten from the input file
print(findAvg(readNumbers()))

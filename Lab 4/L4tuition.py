#
#   purpose: to calculate the
#   author: zachary morrison
#   date written: 09/20/2020
#   Version: 1.0.0
#

#   background
print("The current tuition cost per semester is $8,000.00.\n")

#   constants
TUITION = 8000
APR = 0.03  # 3%

#   processing and output
print("========================================================")
for x in range(1, 6):
    TUITION *= (1 + APR)
    print("On the", x, "year, the tuition per semester will be $" +
          format(TUITION, "4.2f"))

#
#   purpose: to but and sell shares of stock
#   author: zachary morrison
#   date written: 09/10/2020
#   Version: 1.0.0
#

# named constants
COMMISSION_RATE = 0.03

# input
numShares = int(input('Please enter the number of shares:\t\t'))
purchasePrice = float(
    input('Please enter the price per share at purchase:\t'))
salesPrice = float(
    input('Please enter the price per share after selling:\t'))

# processing
subtotalPurchase = numShares * purchasePrice
commissionPurchase = subtotalPurchase * COMMISSION_RATE
totalPurchase = subtotalPurchase + commissionPurchase

subtotalSales = numShares * salesPrice
commissionSales = subtotalSales * COMMISSION_RATE
totalSales = subtotalSales - commissionSales

netProfit = totalSales - totalPurchase

# output
print('\n==================================================================================')
print('|\tYou purchased ' + str(numShares) + ' shares of stock for $' +
      format(purchasePrice, ',.2f') + ' per share.')
print('|\tThe total purchase was $' + totalPurchase + ' including $' +
      format(commissionPurchase, ',.2f') + ' commission fee.')

print('|\tYou sold ' + str(numShares) + ' shares of stock for $' +
      format(salesPrice, ',.2f') + ' per share.')
print('|\tThe total sold was $' + format(totalSales, ',.2f') +
      ' minus the $' + format(commissionSales, ',.2f') + ' commission fee.')

print('|\tThe profis is $' + format(netProfit, ',.2f'))

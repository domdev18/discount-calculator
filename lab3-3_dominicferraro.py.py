#Dominic Ferraro; Lab 3-3; 9-10-22
#This program does the following:
#determines the discount an order should receive based on the quatity the customer ordered. 
#prompts the user to enter the number of software subscriptions sold
#the program uses a series of if/elif statments to determine what the discount is
#prints the quantity purchased, the cost without the discount, the discount and the final cost
#=============================================================variables declared
lLimit01 = 11
uLimit01 = 18
discountTier01 = 6.5
lLimit02 = 19
uLimit02 = 26
discountTier02 = 9.3
lLimit03 = 27
uLimit03 = 39
discountTier03 = 14.5
lLimit04 = 40
discountTier04 = 19.5
quantPurchased = discountAquired = cost = costDiscounted = 0
software = 69.95


#==============================================================input statements
quantPurchased = int(input('How many units of software was sold? '))
#============================================================calculation statements
if quantPurchased < 0:
    print('invalid quantity entered!')
else:
    if quantPurchased < lLimit01:
        discountAquired = 0
    elif quantPurchased >= lLimit01 and quantPurchased <= uLimit01:
        discountAquired = discountTier01
    elif quantPurchased >= lLimit02 and quantPurchased <= uLimit02:
        discountAquired = discountTier02
    elif quantPurchased >= lLimit03 and quantPurchased <= uLimit03:
        discountAquired = discountTier03
    elif quantPurchased >= lLimit04:
        discountAquired = discountTier04
#==============================================================output statements
    costDiscounted = (quantPurchased * software) * (1 - (discountAquired/100))
#===================================69.95 (price per software subscription) is the contant variable
    cost = quantPurchased * 69.95
    print('Quantity purchased =',quantPurchased)
    print('The discount percentage is:',discountAquired,'%')
    print('The price prior to discount: $'+format(cost,'.2f'))
    print('The discounted amount is: $'+format(cost - costDiscounted,'.2f'))
    print('The final price is: $'+format(costDiscounted,'.2f'))


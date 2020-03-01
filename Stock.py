originalStockPrice=40
sharesPurchased=2000
commissionUpFront=0.03

soldStockPrice=42.75
commissionBackEnd=0.03

amount_paid=originalStockPrice * sharesPurchased
originalCommission=sharesPurchased * commissionUpFront
soldStockValue=soldStockPrice*sharesPurchased
finalCommission=commissionBackEnd*sharesPurchased

commissionOverall=originalCommission+finalCommission
net=soldStockValue-commissionOverall

print(float(net))

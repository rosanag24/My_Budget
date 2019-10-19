def start_budget():
 print "Note: This is a budget for 5 items."
 print ""
 items = ["","","","","","",""]
 price = ["","","","","","",""]

 # Insert Income items and Price.
 moneyEarned = float(input("Type your montly INCOME and hit 'Enter':"))

 tithe = moneyEarned*.10
 items[0] = "TITHE"
 price[0] = tithe

 items[1] = "FAST OFFERING"
 price[1] = float(input("Input the amount of fast offering you would like to pay and hit 'Enter':")) 

 print
 print "INSTRUCTIONS: First you will be asked to input 5 services, necessities or items you want to add to your budget. Following each Service you must indicate its monthly price. Finishing this your budget will be displayed."
 print

 items[2] = raw_input("Type the item/service 1 and hit 'Enter':").upper()
 price[2] = float(input("Type the price and hit 'Enter':"))

 items[3] = raw_input("Type the item/service 2 and hit 'Enter':").upper()
 price[3] = float(input("Type the price and hit 'Enter':"))

 items[4] = raw_input("Type the item/service 3 and hit 'Enter':").upper()
 price[4] = float(input("Type the price and hit 'Enter':"))

 items[5] = raw_input("Type the item/service 4 and hit 'Enter':").upper()
 price[5] = float(input("Type the price and hit 'Enter':"))

 items[6] = raw_input("Type the item/service 5 and hit 'Enter':")
 price[6] = float(input("Type the price and hit 'Enter':"))
 show_budget(items, price, moneyEarned)

 # FUNCTION show_budget: print the budget in console. 
 
def show_budget(items, price, moneyEarned):
  sum = price[0]+price[1]+price[2]+price[3]+price[4]+price[5]+price[6]
  print

  print "--------------------------------------------------"
  print '{:^12}'.format('Montly Income') +'{:>8}'.format("$"+str(moneyEarned)) +'{:>18}'.format('Annual Income')+'{:>10}'.format("$"+str(moneyEarned*12))

  print "--------------------------------------------------"
  print "--------------------------------------------------"
  print '{:<12}'.format('Service') +'{:>14}'.format('Month') +'{:>20}'.format('Year')

  print "--------------------------------------------------"
  print '{:<12}'.format(items[0]) +'{:>14}'.format("$"+str(price[0])) +'{:>20}'.format("$"+str(price[0]*12))
  print

  print '{:<12}'.format(items[1]) +'{:>13}'.format("$"+str(price[1])) +'{:>20}'.format("$"+str(price[1]*12))
  print

  print '{:<12}'.format(items[2]) +'{:>14}'.format("$"+str(price[2])) +'{:>20}'.format("$"+str(price[2]*12))
  print

  print '{:<12}'.format(items[3]) +'{:>14}'.format("$"+str(price[3])) +'{:>20}'.format("$"+str(price[3]*12))
  print

  print '{:<12}'.format(items[4]) +'{:>14}'.format("$"+str(price[4])) +'{:>20}'.format("$"+str(price[4]*12))
  print

  print '{:<12}'.format(items[5]) +'{:>14}'.format("$"+str(price[5])) +'{:>20}'.format("$"+str(price[5]*12))
  print

  print '{:<12}'.format(items[6]) +'{:>14}'.format("$"+str(price[6])) +'{:>20}'.format("$"+str(price[6]*12))
  print

  print "--------------------------------------------------"
  print '{:<7}'.format('TOTAL') +'{:>20}'.format("$"+str(sum)) +'{:>19}'.format("$"+str(sum*12))

  print "--------------------------------------------------"
  if (sum > moneyEarned):
    print "LOSSES: "+'{:>14}'.format("Month: $"+str(moneyEarned - sum)) +'{:>20}'.format("Year: $"+str((moneyEarned-sum)*12))
  else:
    print "SAVINGS: "+'{:>18}'.format("$"+str(sum)) +'{:>19}'.format("$"+str(sum*12)) 
  print "--------------------------------------------------"

# Calling the budget.
start_budget()

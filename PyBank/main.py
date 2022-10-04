from operator import index
import os
import csv

#Declare List/Variable
tot_month = []
tot_pl = []
change = []

#locate budget data csv file
budgetdata_csv = os.path.join('..','PyBank','Resources','budget_data.csv')

#open/read csv file
with open(budgetdata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)#advance next row, stores header

#start of loop
    for row in csvreader:

#Determing amount of months
        months=row[0]
        tot_month.append(months)
        month_v = len(tot_month) #length of data = months

#The net total amount of "Profit/Losses" over the entire period
        Total=row[1]
        tot_pl.append(int(Total))

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for next in range(1,month_v):
        change.append(int(tot_pl[next] - int(tot_pl[next-1])))
    average = sum(change)/(month_v-1)


#The greatest increase in profits (date and amount) over the entire period
    great_i = max(change)
    great_im = tot_month[change.index(max(change))+1]

# The greatest decrease in profits (date and amount) over the entire period
    great_d = min(change)
    great_dm= tot_month[change.index(min(change))+1]

#output through terminal
    print('Financial Analysis')
    print('....................................................................................')
    print('Total Months: '+str(month_v))
    print('Total:' + '$'+ str(sum(tot_pl)))
    print("Average Change:" + '$' + str(round(average,2)))# rounding to the hundreths place
    print("Greatest Increase in Profit:" + str(great_im) + ' $' + str(great_i))
    print('Greatest Decrease in Profit:' + '$' + str(great_dm + ' $' + str(great_d)))

#output through external txt file
file = open("PyBank Results.txt",'w')
file.write("Financial Analysis")
file.write('\n')
file.write('....................................................................................')
file.write('\n')
file.write('Total Months: '+str(month_v))
file.write('\n')
file.write('Total:' + '$'+ str(sum(tot_pl)))
file.write('\n')
file.write("Average Change:" + '$' + str(round(average,2)))
file.write('\n')
file.write("Greatest Increase in Profit:" + str(great_im) + ' $' + str(great_i))
file.write('\n')
file.write('Greatest Decrease in Profit:' + str(great_dm) + ' $'+ str(great_d))
file.close

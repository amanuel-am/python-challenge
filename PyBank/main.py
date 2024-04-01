# start here

#import libraries
import csv

# create Variables
file_path=r'PyBank\Resources\budget_data.csv'
number_of_rows=0
unique_dates= set()
dates=[]
profit_losses=[]
total_changes=[]
total_profit_loss=0

with open (file_path) as budget_file:
    csv_file= csv.reader(budget_file)


    header=next(csv_file)
    print(header)

    for row in csv_file:
        number_of_rows+=1
        dates.append(row[0])
        profit_losses.append(int(row[1]))
        total_profit_loss+=int(row[1])


    for i in range(len(profit_losses)-1):
        change=profit_losses[i+1]-profit_losses[i]
        total_changes.append(change)

    average_change= sum(total_changes)/len(total_changes)
    greatest_increase=max(total_changes)
    greatest_decrease=min(total_changes)
    greatest_increase_date=dates[total_changes.index(greatest_increase)+1]
    greatest_decrease_date=dates[total_changes.index(greatest_decrease)+1]
        

    print("xxxxxxxxxxxxxxxx",total_changes)
    number_of_dates=len(dates)
    print('---------------------------------')
    print ('Total number of rows: ',number_of_rows)
    print('---------------------------------')
    print('Number of distinict dates: ',number_of_dates)
    print('---------------------------------')
    print(f'Total amount of profit/losses: ${total_profit_loss}')
    print('---------------------------------')
    print('the average change: $', round(average_change,2))
    print('---------------------------------')
    print(f'Greatest Increase in profits: {greatest_increase_date} (${greatest_increase})')
    print('---------------------------------')
    print(f'Greatest decrease in profits: {greatest_decrease_date} (${greatest_decrease})')
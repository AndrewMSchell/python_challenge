import os
import csv
path = os.path.join("Resources", "budget_data.csv")
with open(path, newline='') as file:
    csvreader = csv.reader(file, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    month = [0]
    revenue = [0]
    revenue_change = [0]
    monthly_change = [0]
    print(f"Header: {csv_header}")
    for row in csvreader:
         month.append(row[0])
         revenue.append(row[1])
    print(len(month))
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    monthly_change = Total / len(revenue_change)
    print(monthly_change)
    profit_increase = max(revenue_change)
    print(profit_increase)
    u = revenue_change.index(profit_increase)
    month_increase = month[u+1]
    profit_decrease = min(revenue_change)
    print(profit_decrease)
    d = revenue_change.index(profit_decrease)
    month_decrease = month[d+1]
print(f'Financial Analysis'+'/n')
print(f'------------------'+'/n')
print("Total number of months: " + str(len(month)))
print("Total revenue in period: $ " + str(total_revenue))
print("Average monthly change to revenue: $ " + str(monthly_change))
print(f"Greatest increase in profits: {month_increase} (${profit_increase})")
print(f"Greatest decrease in profits: {month_decrease} (${profit_decrease})")
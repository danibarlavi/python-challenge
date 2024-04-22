# %%
# Modules
import os
import csv
import pathlib
import pandas as pd

#Set path for file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = pd.read_csv(csvfile)

#Count number of lines in the dataset to find the total number of months in the dataset
total_months = len(csvreader)
#print("Total Months:", total_months)

# %%
#Find the sum of profit/loss in the data set
profitloss_sum = csvreader["Profit/Losses"].sum()
#print("Total: $", profitloss_sum)

# %%
# Find change in Profit/Loss over entire period
profitloss_differences = csvreader["Profit/Losses"].diff()

#Find mean of these difference, rounding to the nearest whole cent
profitloss_averagechange = round((profitloss_differences.mean(skipna= True)), 2)
#print("Average Change: $", profitloss_averagechange)

# %%
#Add differences as a column to the imported dataframe to reference easily in next step
csvreader['Change from last month'] = profitloss_differences
#print(csvreader)

# %%
# Find greatest and greatest decrease in profits over entire period
greatest_increase = profitloss_differences.max()
greatest_decrease = profitloss_differences.min()

# Find the index of the greatest increase and decrease in profits
index_of_greatest_increase = profitloss_differences.idxmax()
index_of_greatest_decrease = profitloss_differences.idxmin()

# Get the dates corresponding to the greatest increase and decrease using index
increase_date = csvreader.loc[index_of_greatest_increase, 'Date']
decrease_date = csvreader.loc[index_of_greatest_decrease, 'Date']

#print("Greatest Increase in Profits:", increase_date, "$", greatest_increase)
#print("Greatest Decrease in Profits:", decrease_date, "$", greatest_decrease)

# %%
#Print to terminal:

print('Financial Analaysis')
print('--------------------')
print("Total Months:", total_months)
print("Total: $", profitloss_sum)
print("Average Change: $", profitloss_averagechange)
print("Greatest Increase in Profits:", increase_date, "$(", greatest_increase, ")")
print("Greatest Decrease in Profits:", decrease_date, "$(", greatest_decrease, ")")

#Save as text file
filepath = '../analysis/output.txt'
with open(filepath, 'w') as f:
    f.write("Financial Analysis:\n"
            "Total Months: " + str(total_months) + "\n"
            "Total: $" + str(profitloss_sum) + "\n"
            "Average Change: $" + str(profitloss_averagechange) + "\n"
            "Greatest Increase in Profits: " + increase_date + " $(" + str(greatest_increase) + ")\n"
            "Greatest Decrease in Profits: " + decrease_date + " $(" + str(greatest_decrease) + ")")

print(f"Output saved to {filepath}")



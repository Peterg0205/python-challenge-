import os 
import csv







csv_path = os.path.join('Resources','budget_data.csv')
    

overall = []
row = 0 
total_months = []
total_profits = []
profit_change = 0 
month_count = 0 
  
#open csv

with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    next(csv_reader)
    for line in csv_reader:
        overall.append(line)
#print(overall) 

        for row in overall:
        

            total_months.append(row[0])
            total_profits.append(row[1])


        print(len(total_months))

#net total of profit/losses 

        monthly_changes= []

        total_profits=[int(x) for x in total_profits] 
        total_profits_sum=sum(total_profits) 
        print (total_profits_sum) 

        for i in range(len(total_profits)-1):
            monthly_changes.append(total_profits[i+1]-total_profits[i])

  


# # for row in csv_reader
#         month_count+= 1 
        






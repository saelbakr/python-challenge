import os
import csv

csvpath = os.path.join("Finances.csv")


Date = []
Profits_Losses = []

with open(csvpath, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        Date.append(row[1])
        Profits_Losses.append(int(row[0]))

## Sum of all the Profits/Losses in the file:      
    total = sum(Profits_Losses)
    #print(f' ${sum(Profits_Losses)}')

## Total of all the months included in the file:
    Month_Year = (list(set(Date)))
    total_months = len(Month_Year)
    #print(total_months)


#print(range(len(Profits_Losses)))
total_diff = 0
range_of_differences = []
for i in range(len(Profits_Losses)-1):
    #print(i)
    diff = Profits_Losses[i+1]-Profits_Losses[i] 
    total_diff = total_diff + diff
    range_of_differences.append(diff)



## Here I am finding the Max and Min of the range in differences and using their indexes locate there dates' locations:
##Index of the max and min first
index_increase = range_of_differences.index(max(range_of_differences))
index_decrease = range_of_differences.index(min(range_of_differences))

## Corresponding name with each value found prior:
Greatest_Decrease_In_Profits = Date[index_decrease+1]
Greatest_Increase_In_Profits = Date[index_increase+1]
#print(range_of_differences)

average_change = total_diff/(len(Profits_Losses)-1)
#print(round(average_change,2))


## Now to add all of these values into their own csv file with titles, etc.
output_path = os.path.join("Financial_Analysis_Summary.csv")
with open(output_path, 'w') as datafile:

    # Initialize csv.writer
    csvwriter = csv.writer(datafile, delimiter=",")

    
    csvwriter.writerow(["FINANCIAL ANALYSIS:"])
    csvwriter.writerow(["-----------------------------------------------"])

    csvwriter.writerow(["TOTAL MONTHS: "f'${total_months}'])

    csvwriter.writerow(["TOTAL AMOUNT OF PROFITS/LOSSES: "f'${total}'])

    csvwriter.writerow(["AVERAGE CHANGE: "f'${round(average_change,2)}'])

    csvwriter.writerow(["GREATEST INCREASE IN PROFITS: "f'{Greatest_Increase_In_Profits} (${max(range_of_differences)})'])

    csvwriter.writerow(["GREATEST DECREASE IN PROFITS: "f'{Greatest_Decrease_In_Profits} (${min(range_of_differences)})'])  
        

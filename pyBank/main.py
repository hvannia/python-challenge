import os
import csv


# return the average values in a list formated with two decimals
def getAverage(listOValues):
    return "{:.2f}".format(sum(listOValues)/len(listOValues))

def checkIfGreatest(dict, value, month):
    if value > dict["gvalue"]:
        dict["gmonth"] = month
        dict["gvalue"] = value
    if value < dict["lvalue"]:
        dict["lmonth"] = month
        dict["lvalue"] = value

#Open dataset for calculations
fileName= "budget_data.csv"
outFileName="budget_data_pr.csv"

with open(fileName) as f:
    csvreader = csv.reader(f, delimiter=',')
    try:
        csv_header = next(csvreader)  # skip header
        #initialize
        numOfMonths = 0
        total =0
        valueChanges=[]
        avgChange = 0.0
        previousValue = 0.0
        greatests={"gmonth":"", "gvalue":0 , "lmonth":"", "lvalue":0}
        #go over data
        for row in csvreader:
            numOfMonths+=1
            thisValue=float(row[1])
            total= total + thisValue  # add up ammounts

            checkIfGreatest(greatests, thisValue,row[0])

            if numOfMonths >=2:
                valueChanges.append(thisValue-previousValue)
            previousValue = thisValue

        # Print outcome
        print (f'Total months :{numOfMonths} \nTotal :{int(total)}\nC=Average Change :{getAverage(valueChanges)}')
        print(f'Greatest Increase in profits :{greatests["gmonth"]} ({greatests["gvalue"]}) ')
        print(f'Greatest Decrease in profits :{greatests["lmonth"]} ({greatests["lvalue"]}) ')

        # Export as CSV
        with open(outFileName, 'w') as csvfile:
            csvwriter = csv.writer(csvfile,delimiter=',')
            csvwriter.writerow(['Calculation','Value'])
            csvwriter.writerow(['Total Months',numOfMonths])
            csvwriter.writerow(['Net Amount',total])
            csvwriter.writerow(['Average Change',getAverage(valueChanges)])
            csvwriter.writerow(['Greatest Increase in profits :',greatests["gmonth"]+' ('+str(greatests["gvalue"])+')'])
            csvwriter.writerow(['Greatest Decrease in profits :', greatests["lmonth"] + ' (' + str(greatests["lvalue"]) + ')'])


    #catch file error
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


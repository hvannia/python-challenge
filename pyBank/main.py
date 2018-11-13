import os
import csv


def getAverage(listOValues):
    x=0
    for i in listOValues :
        x+=i
        print(i)
    return i/len(listOValues)


#Open dataset for calculations
fileName= "budget_data.csv"
with open(fileName) as f:
    csvreader = csv.reader(f, delimiter=',')
    try:
        csv_header = next(csvreader)  # skip header
        # do calculations for all rows after header
        numOfMonths = 0
        total =0

        greatestIncrease =0.0
        greatestDecrease = 0.0
        valueChanges=[]
        avgChange = 0.0
        previousValue = 0.0

        for row in csvreader:
            numOfMonths+=1
            thisValue=float(row[1])
            total= total + thisValue  # add up ammounts
            if numOfMonths >=2:
                valueChanges.append(thisValue-previousValue)

        # send print to fun
        print (f'Total months :{numOfMonths} \nTotal :{int(total)}\nC=Average Change{getAverage(valueChanges)}')

    #catch file error
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


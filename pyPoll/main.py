import os
import csv


#Open dataset for calculations
fileName= "budget_data.csv"
with open(fileName) as f:
    #pass
    csvreader = csv.reader(f, delimiter=',')
    try:

        csv_header = next(csvreader)  # skip header

        # do calculations for all rows after header
        numOfMonths = 0
        total =0

        greatestIncrease =0.0
        greatestDecrease = 0.0

        avgChange = 0.0
        previousValue = 0.0

        for row in csvreader:
            #print(row)
            numOfMonths+=1
            thisValue=float(row[1])
            total= total + thisValue  # add up ammounts
            if numOfMonths >=2:
                avgChange = avgChange+ ( thisValue - previousValue )
            previousValue = thisValue
        avgChange = avgChange + ( thisValue - previousValue ) # last   <--- fix this
ß
        # send print to fun
        print (f'Total months :{numOfMonths} \nTotal :{int(total)}')
        print(f'averageChange :{avgChange/numOfMonths}')

    #catch file error
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


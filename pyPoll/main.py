import os
import csv
import sys

def printPollData(pollData):
    totalVotes=0
    winner=""
    totalVotes= sum(pollData.values())
    print('Election Results /n -------------------------')
    print(f'Total Votes: {totalVotes}')
    print('-------------------------')
    for i in pollData:
      # FIX THIS   print(f'{pollData.keys(i)} :  { pollData.values(i)/totalVotes} ({ pollData.values(i)})')




#read poll  CSV file
fileName= "election_data.csv"
pollData ={}
with open(fileName) as f:
    dReader = csv.DictReader(f)
    #read data, create new dict with new single candidate
    try:
        for row in dReader:
            if row['Candidate'] in pollData:
                pollData[row['Candidate']]= pollData[row['Candidate']]+1
            else:
                pollData[row['Candidate']]=1
        #print(pollData)
        printPollData(pollData)

        # send print to fun


    #catch file error
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (fileName, dReader.line_num, e))


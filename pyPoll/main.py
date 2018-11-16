import os
import csv
import sys

def printPollStat(pollData):
    totalVotes=sum(pollData.values())
    winner=max(pollData, key=pollData.get)
    outFileName="poll_results.txt"
    #save all to be printed in list
    items=["Election Results\n", "-------------------------\n","Total Votes: "+str(totalVotes)+"\n" ,"-------------------------\n"]
    for i in pollData:
        #itemDesc= key(Candidate+ percentage + tital votes)
        keyItem=i+" "
        percentItem="{:.3f}".format((pollData[i]/totalVotes)*100)
        votesItem =  str(pollData[i])
        items.append(keyItem + str(percentItem)+'% ('+votesItem+')\n')
    items.append("-------------------------")
    items.append("WINNER "+winner)
    with open(outFileName, 'w') as outFile:
        for i in items:
            print(i)
            outFile.write(i)
# End Of Function



#read poll  CSV file
fileName= "election_data.csv"
pollData ={}
with open(fileName) as f:
    dReader = csv.DictReader(f)
    try:
        for row in dReader:
            if row['Candidate'] in pollData:
                pollData[row['Candidate']]= pollData[row['Candidate']]+1
            else:
                pollData[row['Candidate']]=1
        printPollStat(pollData)
    #catch file error
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (fileName, dReader.line_num, e))


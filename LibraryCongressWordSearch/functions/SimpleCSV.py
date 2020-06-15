import csv
import sys

##open csv file and read handler link, store in a list
# @param    csvIn
#           input file name and a boolean for search mode
# @return   dataList
#           a list contain names/subject that need to be scraped
def readCSV(csvIn):
    dataList = []

    try:
        inFile = open(csvIn, 'r')
        csvReader = csv.reader(inFile, delimiter=',')
        for row in csvReader:
            dataList.append(row[0])
        # del the header name read in first line and check which mode do we search
        mode = dataList.pop(0)
        if ("subject" in mode or "Subject" in mode):
            dataList.insert(0, False)
        else:
            dataList.insert(0, True)
        print ("\nOpen input CSV success.")
    except:
        print("Fail to open input CSV. Press enter to exit.")
        key = input()
        sys.exit()
        
    return dataList

##write category and data into csv file
# @param    dataList
#           a list contains data
# @param    outputFile
#           output File pointed by user, opened
def writeCSV(dataList, outputFile):
    try:
        csvWriter = csv.writer(outputFile)
        csvWriter.writerow(dataList)
        print("Write this row into CSV success.")
    except:
        print("Fail to write into CSV!")

##get input CSV file name
# @return       fileIn
#               Input CSV file
def getCSVInput():
    print("Please enter csv file name with .csv. \nThe file must in the same folder with your main.py program: ")
    fileIn = input()
    #add typo protection
    while ".csv" not in fileIn:
        print("No .csv detected in fileName. Do you want to type the name again?")
        print("If you want to exit please press enter.")
        print("File Name: ", end = '')
        fileIn = input()
        if len(fileIn) == 0:
            sys.exit()

    return fileIn

##get output CSV file name
# @return       fileOut
#               Output CSV file
def getCSVOutput():
    print("Please enter output file name (with .csv): ")
    fileOut = input()
    while ".csv" not in fileOut:
        print("No .csv detected in fileName. Do you want to type the name again?")
        print("If you want to exit please press enter.")
        print("File Name: ", end = '')
        fileOut = input()
        if len(fileOut) == 0:
            sys.exit()

    return fileOut
    

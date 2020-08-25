from bs4 import BeautifulSoup
from functions import DataSeperation
from functions import PreciseSearch
import urllib.request
import sys

nameSearchUrl = "http://id.loc.gov/search/?q=banana&q=cs%3Ahttp%3A%2F%2Fid.loc.gov%2Fauthorities%2Fnames"
#change first q= to search
subjectSearch = "http://id.loc.gov/search/?q=test&q=cs%3Ahttp%3A%2F%2Fid.loc.gov%2Fauthorities%2Fsubjects"

def getNameSearchUrlPrefix():
    nameSearchPrefix = "http://id.loc.gov/search/?q="
    return nameSearchPrefix

def getNameSearchUrlSuffix():
    nameSearchSuffix = "&q=cs%3Ahttp%3A%2F%2Fid.loc.gov%2Fauthorities%2Fnames"
    return nameSearchSuffix

def getSubjectSearchUrlPrefix():
    subjectSearchPrefix = "http://id.loc.gov/search/?q="
    return subjectSearchPrefix

def getSubjectSearchUrlSuffix():
    subjectSearchSuffix = "&q=cs%3Ahttp%3A%2F%2Fid.loc.gov%2Fauthorities%2Fsubjects"
    return subjectSearchSuffix

## Enter keywords in LOC's search page and pull first 10 results back
#  @param   *names
#           an *arg, typically contain a list of keywords
#  @return  nameData
#           a list contain lists which have raw name, correct name, url and perferred label
def fuzzyNameSearch(*names):
    userChoice = 0
    i = 0
    # A list store several term dataclass
    nameUrlList = []
    htmlList = []
    termList = []
    # This is a list conatins list!
    dataList = []
    containerCluster = []
    nameData = []
    errName = []
    
    print("\nSearch name terms in fuzzy mode...")
    for name in names[0]:
        processedName = PreciseSearch.URI_escape(name)
        nameUrlList.append(getNameSearchUrlPrefix() + processedName + getNameSearchUrlSuffix())
    #can be optimized using multi-thread
    for url in nameUrlList:
        print("Opening Url: ", url)
        try:
            htmlList.append(urllib.request.urlopen(url))
        except:
            print("Fail to oprn: ", name)
            errName.append(name)
    for html in htmlList:
        soup = BeautifulSoup(html, 'html.parser', from_encoding = 'utf-8')
        dataList.append(soup.find_all('tbody', attrs={'class': 'tbody-group'}))
    for data in dataList:
        if data == []:
            print("\nSorry, there is no result comes back from LOC's general search.")
            print("Term with no result: ", names[0][i])
        else:
            containerCluster = DataSeperation.seperate(data)
            print("\n\nCurrent term: ", names[0][i])
            userChoice = displayOption(containerCluster)
            #load list of data into a list
            nameData.insert(0, [names[0][i], containerCluster[userChoice - 1].title, containerCluster[userChoice - 1].LC_URI, containerCluster[userChoice - 1].title])
            containerCluster = []
        i = i + 1
    if(len(errName) > 0):
        errName.insert("Name")
        errorOut = open("FuzzyErr.csv", 'w', encoding = 'utf-8', newline = '')
        SimpleCSV.writeCSV(errName, errorOut)
        errorOut
        print("Name that cause error is put into FuzzyErr.csv")
    return nameData

## Enter keywords in LOC's search page and pull first 10 results back
#  @param   *subjects
#           an *arg, typically contain a list of keywords
#  @return  subjectData
#           a list contain lists which have raw subject, correct subject, url and perferred label
def fuzzySubjectSearch(*subjects):
    userChoice = 0
    i = 0
    # A list store several term dataclass
    subjectUrlList = []
    htmlList = []
    termList = []
    # This is a list conatins list!
    dataList = []
    #termContainer = []
    containerCluster = []
    subjectData = []
    errSubject = []
    
    print("\nSearch subject terms in fuzzy mode...")
    for subject in subjects[0]:
        processedSubject = PreciseSearch.URI_escape(subject)
        subjectUrlList.append(getSubjectSearchUrlPrefix() + processedSubject + getSubjectSearchUrlSuffix())
    #can be optimized using multi-thread
    for url in subjectUrlList:
        print("Opening Url: ", url)
        try:
            openedUrl = urllib.request.urlopen(url)
        except:
            print("Fail to open: ", subject)
        htmlList.append(openedUrl)
    for html in htmlList:
        soup = BeautifulSoup(html, 'html.parser', from_encoding = 'utf-8')
        dataList.append(soup.find_all('tbody', attrs={'class': 'tbody-group'}))
    for data in dataList:
        if data == []:
            print("\nSorry, there is no result comes back from LOC's general search.")
            print("Term with no result: ", subjects[0][i])
        else:
            containerCluster = DataSeperation.seperate(data)
            print("\n\nCurrent term: ", subjects[0][i])
            userChoice = displayOption(containerCluster)
            #load list of data into a list
            subjectData.insert(0, [subjects[0][i], containerCluster[userChoice - 1].title, containerCluster[userChoice - 1].LC_URI, containerCluster[userChoice - 1].title])
            containerCluster = []
        i = i + 1
    if(len(errSubject) > 0):
        errSubject.insert("Subject")
        errorOut = open("FuzzyErr.csv", 'w', encoding = 'utf-8', newline = '')
        SimpleCSV.writeCSV(errSubject, errorOut)
        errorOut.close()
        print("Subject that cause error is put into FuzzyErr.csv")
    return subjectData

## Display terms to let client choose
#  @param   cluster
#           A list of term data class
#  @return  choice
#           which num they choose
def displayOption(cluster):
    choice = 0

    print("\nPlease choose from following result: \n")
    for term in cluster:
        print(term.num, term.title, "    ", term.vocabulary, "   ", term.concept, "\n")
    print("Enter the number before each term: ", end = "")
    #empty input protection
    rawInput = input()
    #invalid input protection
    while len(rawInput) == 0 or int(rawInput) < 1 or int(rawInput) > len(cluster):
        print("The number you selected is invalid. Please type in number displayed.")
        print("If you want to exit the program press ctrl+c.")
        print("Enter the number before each term: ", end = "")
        rawInput = input()
    choice = int(rawInput)
    
    return choice


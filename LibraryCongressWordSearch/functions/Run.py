import urllib.request
import concurrent.futures
from bs4 import BeautifulSoup
from functions import PreciseSearch
from functions import FuzzySearch

def loadUrl(url):
    html = urllib.request.urlopen(url)
    return html

##main process of the metadata scrapper
# @param    url
#           the url that wait to be scrapped
# @param    liTagList
#           A list contain all the <li> tag we need
# @param    outputFile
#           a CSV file for output
# @param    numOfUrl
#           How many url need to be scraped
def runProcessParallel(urlList, liTagList, outputFile, numOfUrl):
    # iterator to show program progress
    categoryValue = []
    i = 1
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(loadUrl, url): url for url in urlList}
        for future in concurrent.futures.as_completed(future_to_url):
            # original url link
            url = future_to_url[future]
            # opened url
            html = future.result()
            # load target digital collection in html parser
            soup = BeautifulSoup(html, 'html.parser', from_encoding = 'utf-8')
            # find collection title
            FindObjectTitle.findObjectTitle(soup, categoryValue)
            # find original url link
            categoryValue.append(url)
            # find attributes value
            FindCategoryValue.findCategoryValue(soup, liTagList, categoryValue, outputFile)
            print("We have successfully web-scraped ", i, " / ", numOfUrl, " records")
            # reset categoryValue for next collection
            categoryValue = []
            i = i + 1

##main process of search in two mode
# @param    *argv
#           parameters, first is suppoose to be a list conatin search keyword
#           second is suppose to be a boolean value of search mode
#           True for name search, False for subject search
# @return   resultList
#           a list of correct name
def processSerial(*argv):
    preciseResult = []
    fuzzyResult = []
    resultList = []
    failedResult = []
    printOption = True
    
    #name search mode
    if argv[1] == True:
        print("\nSearch name terms in precise mode...")
        #preciseResult is a list contain list!
        preciseResult = PreciseSearch.preciseNameSearch(argv[0])
        failedResult = checkFailure(preciseResult, argv[0], printOption)
        if len(failedResult) == len(argv[0]):
            print("\nNo name precise result find!")
            #fuzzyResult is a list contain list!
            fuzzyResult = FuzzySearch.fuzzyNameSearch(argv[0])
            resultList = fuzzyResult
        elif len(failedResult) == 0:
            resultList = preciseResult
        else:
            fuzzyResult = FuzzySearch.fuzzyNameSearch(failedResult)
            resultList = mergeResult(preciseResult, fuzzyResult)
    #subject search mode
    elif argv[1] == False:
        print("\nSearch subject terms in precise mode...")
        preciseResult = PreciseSearch.preciseSubjectSearch(argv[0])
        failedResult = checkFailure(preciseResult, argv[0])
        if len(failedResult) == len(argv[0]):
            print("\nNo subject precise result find!")
            fuzzyResult = FuzzySearch.fuzzySubjectSearch(argv[0])
            resultList = fuzzyResult
        elif len(failedResult) == 0:
            resultList = preciseResult
        else:
            fuzzyResult = FuzzySearch.fuzzySubjectSearch(failedResult)
            resultList = mergeResult(preciseResult, fuzzyResult)
    
    print("\nkeyword search complete!")
    return resultList

## Check if any precise search result is null.
## If true,delete it from search result and add to another list for fuzzySearch
## If isPrint is true, print user-friendly message
# @param    result
#           a list come from precise search, which have name/subject, url and perferred label
# @param    *terms
#           parameters, first is suppoose to be a list conatin search keyword
#           second is suppose to be a boolean value of search mode
#           True for name search, False for subject search
# @return   failed
#           a list contains all failed terms
def checkFailure(result, *terms):
    failed = []
    i = 0

    print("\nCheck null results...", end = "")
    for element in result:
        if "null" in element:
            failed.append(terms[0][i])
            i = i + 1     
    print("Done!")
    print("\nFailed: ")
    for element in failed:
        print(element)
         
    return failed

## merge results from two search mode together
# @param    precise
#           a list contain lists which have name/subject, url and perferred label
# @param    fuzzy
#           a list contain lists which have name/subject, url and perferred label
# @return   combinedResult
#           a list contain list which none of them are null
def mergeResult(precise, fuzzy):
    combinedResult = []
    length = len(fuzzy)
    isMatched = False
    
    #need re-design this 6/8
    for element in precise:
        isMatched = False
        term = element[0]
        if "null" in element:
            for item in fuzzy:
                if item[0] == term:
                    combinedResult.append(item)
                    isMatched = True
                    break
            if isMatched == False:
                combinedResult.append(element)
        else:
            combinedResult.append(element)
    return combinedResult

## ask user what search mode they perfer to run
# @return   searchMode
#           A boolean value, true for name search, falsefor subject search
def askSearchMode():
    print("Which search mode you perfer?")
    print("1. Name search (LCNAF)        2. Subject search (LCSH)")
    print("Enter the number before each term: ", end = "")
    #empty input protection
    rawInput = input()
    #invalid input protection
    while len(rawInput) == 0 or int(rawInput) < 1 or int(rawInput) > 2:
        print("The number you selected is invalid. Please type in number displayed.")
        print("If you want to exit the program press ctrl+c.")
        print("Enter the number before each term: ", end = "")
        rawInput = input()
    if int(rawInput) == 1:
        return True
    else:
        return False


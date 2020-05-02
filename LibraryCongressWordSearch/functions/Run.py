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
    
    #name search mode
    if argv[1] == True:
        print("\nSearch in name...")
        preciseResult = PreciseSearch.preciseNameSearch(argv[0])
        if len(preciseResult) == 0:
            print("No name precise result find!")
            #fuzzyResult = FuzzySearch.fuzzyNameSearch(argv[0])
    #subject search name
    elif argv[1] == False:
        print("\nSearch in subject...")
        preciseResult = PreciseSearch.preciseSubjectSearch(argv[0])
        if len(preciseResult) == 0:
            print("\nNo subject precise result find!")
            #fuzzyResult = FuzzySearch.fuzzySubjectSearch(argv[0])
    if (len(preciseResult) > len(fuzzyResult)):
        resultList = preciseResult
    elif (len(preciseResult) < len(fuzzyResult)):
        resultList = fuzzyResult
    print("keyword search complete!")
    return resultList

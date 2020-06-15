from bs4 import BeautifulSoup
import DataSeperation
import FuzzySearch
from dataclasses import dataclass
import urllib.request

def fuzzyNameSearchTest(*names):
    nameUrlList = []
    htmlList = []
    termList = []
    # This is a list conatins list!
    dataList = []
    termCluster = []
    
    for name in names[0]:
        nameUrlList.append(FuzzySearch.getNameSearchUrlPrefix() + name + FuzzySearch.getNameSearchUrlSuffix())
    #can be optimized using multi-thread
    for url in nameUrlList:
        htmlList.append(urllib.request.urlopen(url))
    for html in htmlList:
        soup = BeautifulSoup(html, 'html.parser', from_encoding = 'utf-8')
        dataList.append(soup.find_all('tbody', attrs={'class': 'tbody-group'}))
        termCluster = DataSeperation.seperate(dataList)
        #TODO: userChoice = displayOption(termCluster)
    for t in termCluster:
        print("num: ", t.num)
        print("title: ", t.title)
        print("voca: ", t.vocabulary)
        print("concept: ", t.concept)
        print("id: ", t.identifier)
        print("uri: ", t.LC_URI)

def main():
    combinedData = []
    combinedData = FuzzySearch.fuzzyNameSearch(["test"])
    for data in combinedData:
        print(data)

if __name__ == "__main__":
    main()

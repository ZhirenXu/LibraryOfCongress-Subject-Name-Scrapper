from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class Term:
    num: str
    title: str
    vocabulary: str
    concept: str
    identifier: str
    LC_URI: str
    
##Sepreate Data from tags using bs4
# @param	data
#		A list contain tags scraped from webpage
# @return	termCluster
#		A list which contains data classes for one term
def seperate(data):
    termCluster = []
    num = 0
    title = ""
    vocabulary = ""
    concept = ""
    searchID = ""
    uriSuffix = "http://id.loc.gov"
    dataUri = ""
    uri = ""
    i = 0
    
    for searchRecordList in data:
        #for tbody in searchRecordList:
        tr = searchRecordList.find('tr')
        num = tr.contents[1].text
        #first contents get <td>, second contents to get <a>, then <a>'s child
        title = tr.contents[3].a.text
        dataUri = tr.contents[3].a['href']
        uri = uriSuffix + dataUri
        vocabulary = tr.contents[5].text
        #first contents get <td>, second contents get <type>, then <type>'s child
        concept = tr.contents[7].type.text
        searchID = tr.contents[11].text
        newTerm = Term(num, title, vocabulary, concept, searchID, uri)
        termCluster.append(newTerm)
        i = i + 1
        if i >= 10:
            break
    return termCluster

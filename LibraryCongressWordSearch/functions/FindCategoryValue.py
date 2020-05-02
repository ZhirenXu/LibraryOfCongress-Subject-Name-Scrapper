import SimpleCSV
## find and store all contents of desired <li> tags according to categoryList
# @param    source
#           html page that has been parsed by beautifulsoup
# @param    liTagList
#           a list contain 'class' attribution in <li> tag, use it to find correct <li> tag and its content
# @param    valueList
#           a list to store scraped attrs' value
# @param    outFile
#           output csv file
def findCategoryValue(source, liTagList, valueList, outFile):
    content = ""
    for liTag in liTagList:
        result = source.findAll('li', attrs={'class': liTag})
        # use ; to isolate multiple li tag contents
        if len(result) > 1:
            while len(result) > 0:
                if result[0] is not None:
                    rawContent = result[0].text
                    index = rawContent.find('\r\n')
                    if index != -1:
                        content += rawContent[:index]
                    else:
                        content += rawContent    
                    content += '|'
                    result.pop(0)
            valueList.append(content[:len(content)-1])        
            content = ""
        elif len(result) == 1:
            valueList.append(result[0].text)
        else:
            valueList.append("null")
    SimpleCSV.writeCSV(valueList, outFile)

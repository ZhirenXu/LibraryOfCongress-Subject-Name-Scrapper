## find object title and handler, then store it into a list
# @param    source
#           html page that has been parsed by beautifulsoup
# @param    valueList
#           a list contain contents in each <li> tag, in here we just need to add item's title
def findObjectTitle(source, valueList):
    value = ""
    # delete front/back whitespace and add to valueList
    tag = source.find('title')
    value += tag.string.split("|", 3)[1]
    valueList.append(value[1:len(value) - 1])
    value = ""

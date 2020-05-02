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

def fuzzyNameSearch(*names):
    nameUrlList = []
    
    for name in names[0]:
        nameUrlList.append(getNameSearchUrlPrefix() + name + getNameSearchUrlSuffix())

    pass
def fuzzySubjectSearch(*subjects):
    subjectUrlList = []

    for subject in subjects[0]:
        subjectUrlList.append(getSubjectSearchUrlPrefix() + subject + getSubjectSearchUrlSuffix())

    pass

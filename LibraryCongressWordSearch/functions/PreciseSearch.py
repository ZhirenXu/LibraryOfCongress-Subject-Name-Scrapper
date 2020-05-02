#Author: Ruth Kitchin Tillman
#Original script: https://github.com/ruthtillman/subjectreconscripts/blob/master/retrieve-lc-uris-from-csv.py
#Modifiied by: Zhiren Xu
import requests, os, time, urllib


##Process the initial name to fit url format
# @param    word
#           keyword for LOC name search
# @return   a processed word which can put in url without error
def URI_escape(word):
  return word.replace(' -- ', '--').replace(' ', '%20').replace(',', '%2C').replace("'","%27").replace('(', '%28').replace(')', '%29')

##Precisely search the name (direct append into url to test if it exist)
# @param    *names
#           *arg, contain a list of name keywords
# @return   combinedNameData
#           a list contain lists which have name, url and perferred label
def preciseNameSearch(*names):
    nameData = []
    combinedNameData = []
    counter = 1
    totalRecordNum = len(names[0])
    
    for name in names[0]:
      processedName = URI_escape(name)
      print("Processing ", counter, " / ", totalRecordNum, " of records...", end = "")
      nameURL = 'http://id.loc.gov/authorities/names/label/' + processedName
      nameResponse = requests.head(nameURL)
      if nameResponse.status_code == 302:
          nameData.append(name)
          nameData.append(nameResponse.headers['X-Uri'])
          nameData.append(nameResponse.headers['X-Preflabel'])
      else:
          nameData.append("null")
          nameData.append("null")
          nameData.append("null")
      combinedNameData.append(nameData)
      print("Done!")
      counter = counter + 1
      nameData = []
    #add header for output file
    combinedNameData.insert(0, ["Name", "LC_URI", "LC_Label"])
    return combinedNameData

##Precisely search the subject (direct append into url to test if it exist)
# @param    *subjects
#           *arg, contain a list of subject keywords
# @return   combinedSubjectData
#           a list contain lists which have subject, url and perferred label    
def preciseSubjectSearch(*subjects):
    subjectData = []
    combinedSubjectData = []
    counter = 1
    totalRecordNum = len(subjects[0])
    
    #for loop can be parallelized
    for subject in subjects[0]:
      print("Processing ", counter, " / ", totalRecordNum, " of records...", end = "")
      processedSubject = URI_escape(subject)
      subjectURL = 'http://id.loc.gov/authorities/subjects/label/' + processedSubject
      subjectResponse = requests.head(subjectURL)
      if subjectResponse.status_code == 302:
          subjectData.append(subject)
          subjectData.append(subjectResponse.headers['X-Uri'])
          subjectData.append(subjectResponse.headers['X-Preflabel'])
      else:
          subjectData.append("null")
          subjectData.append("null")
          subjectData.append("null")
      combinedSubjectData.append(subjectData)
      print("Done!")
      subjectData=[]
      counter = counter + 1
    #add header for output file
    combinedSubjectData.insert(0, ["Subject", "LC_URI", "LC_Label"])
    return combinedSubjectData

##A parallel process version of precise name search
def preciseNameSearchParallel():
  pass

#A parallel process version of precise subject search
def preciseSubjectSearchParallel():
  pass


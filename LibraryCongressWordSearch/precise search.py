import requests, csv, os, time, urllib

# this expects a CSV with a column titled "subject." You may add additional fields, e.g. the ASpace ID of the subject record, see https://github.com/ruthtillman/subjectreconscripts/blob/master/retrieve-lc-uris-from-csv.py

def URI_escape(value):
  return urllib.parse.quote(value.replace(' -- ', '--'))

def get_subject_URIs(writer,csvSource):
  with open(csvSource, newline='') as data:
    reader = csv.DictReader(data)
    for row in reader:
      subjectLabel = URI_escape(row['subject'])
      subjectURI = 'http://id.loc.gov/authorities/subjects/label/' + subjectLabel
      subjectResponse = requests.head(subjectURI)
      if subjectResponse.status_code == 302:
          print(subjectResponse)
          writer.writerow({'subject' : row['subject'], 'LC_URI' : subjectResponse.headers['X-Uri'], 'LC_Label': subjectResponse.headers['X-Preflabel']})
      else:
          writer.writerow({'subject' : row['subject'], 'LC_URI' : '', 'LC_Label': ''})
      time.sleep(4)

def write_subject_csv(csvOutput,csvSource):
    fieldnames = ['subject', 'LC_URI', 'LC_Label']
    with open(csvOutput, 'w', newline='') as outputFile:
        writer = csv.DictWriter(outputFile, fieldnames=fieldnames)
        writer.writeheader()
        get_subject_URIs(writer,csvSource)

csvOutput=input("Name of output CSV: ")
csvSource=input("Path to / name of source CSV: ")

write_subject_csv(csvOutput,csvSource)

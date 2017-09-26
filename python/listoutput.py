#! /usr/bin/python
# For outputting the list for karaoke from the master spreadsheet
import csv
import datetime

with open('gelkmaster.csv') as csvfile:
  reader = csv.reader(csvfile)
  text = ''
  for row in reader:
    text += row[0].strip() + ' - ' + row[1].strip() + '\n'

  datename = datetime.datetime.now().strftime("%Y%m%d%H%M")

  with open('gelk-'+datename+'.txt', 'w') as listfile:
    listfile.write(text)

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:04:11 2023

@author: tiwashima
"""

import re

importList='C:\\directory\\to\\outlookList.txt'
file=open(importList)
data=file.read()
print('Opened: ' + importList + '.')

#If you need a list of the data
#dataList=list(data.split(';'))

#Test that only an email address will be pulled from an Outlook formatted: lastName, firstName <address>
#testString='Iwashima, Timothy <timothy.iwashima@test.com>'
#dataEmailAddresses=re.search(r'[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+', testString)
#print(dataEmailAddresses)

outputFile=('C:\\directory\\to\\save\\emailOnly.txt')
emailList=open(outputFile,'a')
dataEmailAddresses=re.findall(r'[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-z]+', data)
for address in dataEmailAddresses:
    emailList.write(address + '\n')
emailList.close()
file.close()
print('Saved: ' + outputFile + '.')

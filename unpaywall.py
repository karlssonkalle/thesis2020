#Takes quite a while to run. 
#Remember that Unpaywall asks users to limit calls to 100, 000 per day. 

email = "INPUT MAIL HERE"  #Email needed by unpaywall api
#Packages:
import urllib.request, urllib.parse, urllib.error
import json
import ssl
import re
import csv
from datetime import datetime
import os
from multiprocessing import Pool

doi_data = list()

doi_list = list() #DOI list to add retrieved DOIs
Dcount = 0 #Number of DOIs
broken_doi = list() #Count how many documents have DOIs that does not work/are not found
blank_doi = 0 #Count for blank DOIs

serviceurl = 'https://api.unpaywall.org/v2/' #API link for unpaywall

def grab(x): #returning values and returning "unknown" if value error
    if x is False or x == " " or x == "" or x == "No Information" or x is None:
        return "unknown"
    else:
        try:
            return x
        except:
            return "unknown"

def get_data(doi): #Function to get data for each DOI
    try:
        unpaywallurl = serviceurl + urllib.parse.quote(doi) + "?email=" + email
        #print('Retrieving', url)
        uh = urllib.request.urlopen(unpaywallurl)
        data = uh.read().decode()
        info = json.loads(data)
        #print (info['is_oa'])
        #x = info['is_oa']
        #doi_status.append(x)
        return info
    except:
        #print ("broken DOI")
        x = "broken"
        #doi_status.append(x)
        return x

while True: #opening csv file DOI list
        filename = 'Name of file'
        #filename = "DOIlisttest"
        if len(filename) < 1:
            quit()
        try:
            csv_data = open(filename,encoding="ISO-8859-1") #Saving csv file as csv_data
            break
        except:
            print ("Can't find the file")
            continue

for item in csv_data: #Loop to pull DOIs from csv file line by line
        word = item.rstrip()
        word = word.split(",")
        if len(word[0]) > 1: Dcount = Dcount + 1 
        if Dcount == 1:continue #Skipping first Line which is headers
        if len(word[0]) < 1: #Counting missing DOIs
            word[0] = "No DOI listed"
            blank_doi = blank_doi + 1 #Counting blank DOIS
        doi_list.append(word[0]) #adding DOIs to a DOI list

print (len(doi_list)-blank_doi,"DOIs found. This should take about 1 minute per 1000 DOIs depending on speed of your computer")

count = 0 #Count for how many DOIs have been processed

for doi in doi_list: #Giving updates how much longer to go by comparing counts to the number of DOIs
    if count == int(len(doi_list)*0.25):
        print ("25% processed....")
    if count == int(len(doi_list)*0.50):
        print ("50% processed...")
    if count == int(len(doi_list)*0.75):
        print ("75% processed...")
    count = count + 1

    if doi == "No DOI listed": #keeping track of blank DOIs
        doi_dict = {
            "DOI":"No DOI listed",
            "Oa_status":""
            }
        doi_data.append(doi_dict)
        continue

    try: #Trying to pull from unpaywall API for the list DOI
        unpaywallurl = serviceurl + urllib.parse.quote(doi) + "?email=" + email
        #print('Retrieving', url)
        uh = urllib.request.urlopen(unpaywallurl)
        data = uh.read().decode()
        info = json.loads(data)

    except:
        #print ("URL Retrieving error")
        broken_doi.append(doi)
        doi_dict = { #returning blank info if DOI can't be found
            "DOI":doi,
            "Oa_status": ""
            }
        doi_data.append(doi_dict)
        continue

    doi_dict = { #returning blank info if DOI can't be found
            "DOI":doi,
            "Oa_status":info['oa_status']
            }

    doi_data.append(doi_dict)

csv_name = "UNPAYWALL PULL - "+filename #Creates a new file called UNPAYWALL PULL + the name of the file you inputed above. 
#To make it work as a CSV:
myFile = open(csv_name,'w',newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerow(['DOI', "Oa_status"])
    for a in doi_data:
        data2 = [a["DOI"], a["Oa_status"]]
        writer.writerow(data2)

print ("There were",len(broken_doi),"DOI errors")
print (csv_name,"exported with the data.")
os.startfile(csv_name)
#Done!

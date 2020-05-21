#Altmetric.com asks users not to hammer the server. If needed, add a delay to the API-calls. 
#Packages:
from pyaltmetric import Altmetric, Citation, HTTPException
import csv

# initialize Altmetric
a = Altmetric()

with open('Name of CSV-file with DOIs', 'r') as infile:
    with open('Name of file with results', 'w') as outfile:
        writer = csv.writer(outfile)

        for x in infile:
            x = x.rstrip()
            # search for article using doi
            c = a.doi(x)
            if c:
                # initialize Citation and fetch fields
                citation = Citation(c)
                result = citation.get_fields('doi','title','cited_by_msm_count') #Choose which data to retrieve msm=news media. 
            else:
                result = [x, 'no data'] #No data = DOI not found. 
            # write row to file
            writer.writerow(result)

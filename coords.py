# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 17:38:56 2019

@author: mag
"""
import sqlite3
import json 
import requests

#connects to db
conn = sqlite3.connect("phonebook_database.db")

#link to db with cursor
c = conn.cursor()

def getPostcodesList(tableName):
    c.execute(f"SELECT DISTINCT(postcode) FROM {tableName}")
#    return first element of each row to remove tuples from the list
#    I have now a list of strings instead of list of tuples with strings
    return [item[0] for item in c.fetchall()]
#    return c.fetchall()
    

def queryApi(postcodesList):
   # query the api to get lat & lon for each postcode, supply postcodes list in a json
    r = requests.post("http://api.postcodes.io/postcodes", json={"postcodes": postcodesList})
    #print(r.json())
#    print(json.dumps(r.json().get("result")[:5], indent=4, sort_keys=True))  
    #get result list from api response 
    return r.json().get("result") 


def updateLonLat(tableName, postcode, latitude, longitude):
    c.execute(f'''UPDATE {tableName}
              SET y_coordinate = ?, x_coordinate = ?
              WHERE postcode = ?''', (latitude, longitude, postcode))
    conn.commit()


def updateTable(postcodeMappingList, tableName):
    for item in postcodeMappingList:
        if item["result"] != None:
            updateLonLat(tableName, item["query"], item["result"]["latitude"], item["result"]["longitude"])
        else:
            print(f"Result not found for: {item['query']}")


#personalPostcodes = getPostcodesList("phonebook_personal")
#businessPostcodes = getPostcodesList("phonebook_business")
#personalMappingList = queryApi(personalPostcodes)
#businessMappingList = queryApi(businessPostcodes)
#updateTable(personalMappingList, "phonebook_personal")
#updateTable(businessMappingList, "phonebook_business")

#instead of 6 lines above:
def runAll(tableName):
    postcodes = getPostcodesList(tableName)
    mappingList = queryApi(postcodes)
    updateTable(mappingList, tableName)

if __name__ == "__main__":
    runAll("phonebook_personal")
    runAll("phonebook_business")

#closing cursor
c.close()
#closing connection to db
conn.close()
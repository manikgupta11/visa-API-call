"""
Request: zipcode(optional)

Response: 
	"restaurants": [
		{
			"name": "value",
			"address": "value",
			"cuisine": "value",
			"expense": "value",
			"offers": "value",
			“waitTime”: “value”
		}
	]

"""

#### Synthesized data ####
offers=["10% off on total bill", "1+1 on drinks", "10% off on visa card payments", "20% off on buffet"]
cuisines=["CHINESE", "CONTINENTAL","ITALIAN", "INDIAN"]
expenses=["LOW", "AVERAGE", "HIGH"]
#########################

#### Input ####
zipcode="94404"
cert_file_path = "cert.pem"
key_file_path = "key.pem"
url = "https://sandbox.api.visa.com/merchantlocator/v1/locator"
###############

import requests
import json
import time
import random
finalResponse={"restaurants":[]}
a=time.time()
i=1
while i<6:

	payload = {
		"header": {   
			"messageDateTime": "2020-06-20T16:51:51.903", 
			"requestMessageId": "Request_001",        
			"startIndex": str(i)    
		},
		"searchAttrList": {      
			"merchantCategoryCode": ["5812"],   
			"merchantCountryCode": "840",       
			"merchantPostalCode": zipcode,    
			"distance": "20",       
			"distanceUnit": "M"   
		}, 
		"responseAttrList": ["GNLOCATOR"], 
		"searchOptions": {     
			"maxRecords": "10", 
			"matchIndicators": "true",       
			"matchScore": "true"    
		}
	}

	headers = {
		'Content-Type': 'application/json',
		'Authorization': 'Basic UTlON1pTTVdZQzIxTFRXRjJHQVEyMUl6b0Fzb1lSNTBnOS1RZ2MwbTlieW81eXV2bzpCdjBqeThwM1ZyNDl5aUk0OTZCeXd6MXBNYzBUeFF3eUZ2M3lFUVc='
	}

	cert = (cert_file_path, key_file_path)
	response = requests.request("POST", url, headers=headers, data = json.dumps(payload),cert=cert)

	responseText=response.text.encode('utf8')
	responseJSON = json.loads(responseText)

	# print(responseJSON['merchantLocatorServiceResponse']['response'][0]['responseValues']['visaMerchantName'])
	SynthesizedResponse = {
		"name" : responseJSON['merchantLocatorServiceResponse']['response'][0]['responseValues']['visaMerchantName'],
		"address" : responseJSON['merchantLocatorServiceResponse']['response'][0]['responseValues']['merchantStreetAddress'],
		"cuisine" : random.choice(cuisines),
		"expense" : random.choice(expenses),
		"offer" : random.choice(offers),
		"waitTime" : str(random.randrange(1,30))
	}
	# print(SynthesizedResponse)
	finalResponse["restaurants"].append(SynthesizedResponse)
	i+=1
b=time.time()

print(finalResponse)
f=open("op.json","w")
json.dump(finalResponse,f,indent=4)
f.close()
print("Time elapsed:",b-a)
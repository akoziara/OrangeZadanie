import json
import logging
import time
import requests

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

HowLong = 5
toCheck = 10

logging.basicConfig(filename="log.txt", level=logging.INFO)
for x in range(toCheck):
    url = "https://tvgo.orange.pl/gpapi/status"
    response = requests.get(url)

    responseTime = response.elapsed.total_seconds()
    responseStatusCode = response.status_code

    isJsonresponse = response.headers.get('content-type') == 'application/json' or response.headers.get(
        'content-type') == 'application/vnd.orangeott.v1+json'

    isJson = validateJSON(response.text)


    print(response.json())
    print(isJsonresponse)
    print(responseTime)
    print(responseStatusCode)
    print(isJson)

    logging.info("Response time: " + str(responseTime))
    logging.info("Response statusCode: " + str(responseStatusCode))
    logging.info("Is json response: " + str(isJsonresponse))
    logging.info("Is valid json: " + str(isJson))
    time.sleep(HowLong)

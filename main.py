import json
import logging
import time
import requests

from pythonping import ping

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

#Zadanie dodatkowe
def ping_host(hostName):
    ping_result = ping(target=hostName, count=1, timeout=1)

    return {
        'host': hostName,
        'packet_loss': ping_result.packet_loss,
        'min': ping_result.rtt_min_ms,
        'max': ping_result.rtt_max_ms,
        'avg': ping_result.rtt_avg_ms
    }

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

    # Zadanie dodatkowe
    hosts = 'tvgo.orange.pl'
    ping_result = ping_host(hosts)
    print(ping_result)

    print(response.json())
    print(isJsonresponse)
    print(responseTime)
    print(responseStatusCode)
    print(isJson)


    logging.info("Response time: " + str(responseTime))
    logging.info("Response statusCode: " + str(responseStatusCode))
    logging.info("Is json response: " + str(isJsonresponse))
    logging.info("Is valid json: " + str(isJson))
    # logging.info("Packet loss: " + str(ping_result.packet_loss))
    # logging.info("Min: " + str(ping_result.rtt_min_ms))
    # logging.info("Max: " + str(ping_result.rtt_max_ms))
    # logging.info("Avg: " + str(ping_result.rtt_avg_ms))
    time.sleep(HowLong)

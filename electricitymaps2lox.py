import datetime
import pytz
import requests
import json
import socket


# *********** Config of Electricity Maps to Loxone Bridge ***********
# Electricity Maps login data
auth_token = 'yoursuperprivatetoken'
# Loxone Miniserver IP and UDP target port
miniserver_ip = "192.168.1.30"
miniserver_port = 1234
# *********** Config of Electricity Maps to Loxone Bridge ***********


def convert_to_switzerland_time(utc_datetime_str):
    # Create a datetime object from the UTC string
    utc_datetime = datetime.datetime.strptime(utc_datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")

    # Check if the datetime is in daylight saving time (CEST)
    if pytz.timezone('Europe/Zurich').localize(utc_datetime).dst():
        # Adjust for daylight saving time (CEST)
        local_datetime = utc_datetime + datetime.timedelta(hours=2)
    else:
        # Standard time (CET)
        local_datetime = utc_datetime + datetime.timedelta(hours=1)

    return local_datetime


carbon_intensity_history_url = "https://api-access.electricitymaps.com/free-tier/carbon-intensity/history?zone=CH"
headers = {
  "auth-token": auth_token
}

carbon_intensity_history_response = requests.get(carbon_intensity_history_url, headers=headers)
carbon_intensity_history = json.loads(carbon_intensity_history_response.text)

data_for_loxone = ""
carbon_intensity = 0

for history_element in carbon_intensity_history["history"]:
    local_time = convert_to_switzerland_time(history_element["datetime"])
    carbon_intensity = history_element["carbonIntensity"]
    data_for_loxone = data_for_loxone + "co2/{}/{}\n".format(local_time.hour, carbon_intensity)

# Get last element of carbon intensity and send it as "now" value
data_for_loxone = data_for_loxone + "co2/now/{}\n".format(carbon_intensity)

# Create a UDP socket and send the data to the Loxone Miniserver
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.sendto(bytes(str(data_for_loxone), "utf-8"), (miniserver_ip, miniserver_port))
# print(data_for_loxone)

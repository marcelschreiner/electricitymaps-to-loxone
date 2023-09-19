# Electricity Maps to Loxone Bridge

![Pylint](https://github.com/marcelschreiner/electricitymaps-to-loxone/actions/workflows/pylint.yml/badge.svg)
[![HitCount](https://hits.dwyl.com/marcelschreiner/electricitymaps-to-loxone.svg?style=flat)](http://hits.dwyl.com/marcelschreiner/electricitymaps-to-loxone)

This Python script retrieves real-time carbon intensity data from Electricity Maps and sends it to a Loxone Miniserver using UDP. The script is designed to help you monitor and integrate carbon intensity information into your Loxone home automation system. Below, you'll find instructions on how to set up and use this script.
This script is configured to poll Swiss power grid carbon intensity dat. But is can be easely modified to poll data for an other country.
Keep in mind that you need an account at Electricity Maps. The free tier is enough and allows for 100'000 monthly API calls for non comercial use.

## Prerequisites

Before you can use this script, you'll need the following:

- Python 3
- The `requests` and `pytz` library
- Free account at Electricity Maps

## Setup

1. Install the required Python packages using `pip`:
  (`pip3` is traditionally used on Rapberry Pis to install libraries for Python 3 other systems may use `pip`)

   ```shell
   pip3 install requests pytz
   ```

2. In the script, you need to configure the following parameters:

   - `AUTH_TOKEN`: Your Electricity Maps authentication token.
   - `MINISERVER_IP`: The IP address of your Loxone Miniserver.
   - `MINISERVER_PORT`: The UDP target port on your Loxone Miniserver.
  
   Make sure to replace `'YourSuperPrivateToken'`, `"192.168.1.30"`, and `1234` with your actual credentials.

## Usage

Run the script to retrieve data from Electricity Maps and send it to your Loxone Miniserver:

```shell
python3 electricitymaps2lox.py
```

The script does only poll the Electricyty Maps server once and quits again. The following example is for a Raspberry Pi to run the script every hour 5minutes past the hour mark:

```shell
- In the terminal enter: "crontab -e"
- Then add the line "5 * * * * python3 /home/pi/electricitymaps2lox.py"
- Save and exit
```

## Script Details

- The `convert_to_switzerland_time` function converts UTC datetime strings to Swiss local time, considering daylight saving time.
- It processes the data and creates a formatted string containing hourly carbon intensity values.
- The last element of the data is also sent as a "now" value to the Loxone Miniserver.
- The data is transmitted to the Loxone Miniserver using a UDP socket.

## License

This script is provided under the [MIT License](LICENSE.md). Feel free to modify and use it according to your needs.

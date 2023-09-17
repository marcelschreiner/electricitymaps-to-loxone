# electricitymaps-to-loxone
A python script to send Swiss power grid carbon intensity data to a Loxone Miniserver. Execute this script every hour. The script does only poll the Electricyty Maps server once and quits again.
Keep in mind that you need an account at Electricity Maps. The free tier is enough and allows for 100'000 monthly API calls for non comercial use.

## Example on Raspberry Pi

Let's say the script is run on a Raspberry Pi. To execute it every 60min the following config needs to be made:

- In the terminal enter: "crontab -e"
- Then add the line "5 * * * * python3 /home/pi/electricitymaps2lox.py"
- Save and exit

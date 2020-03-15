# nanoleaf-clock

Use nanoleaf display panels to indicate how long until bedtime. The room turns orangier in half hour increments towards bedtime.

# Setup

Copy `secrets_example.py` to `secrets.py` and fill it in. To find the nanoleaf IP address look at a local router's dhcp server and try a few. There are likely better ways but I couldn't get them to work.

To run every 5 minutes on a raspberry pi, add this to cron:
```
*/5 * * * * /home/pi/.pyenv/versions/3.8.2/bin/python /home/pi/nanoleaf-clock/main.py
```

# doorphone-notify
This is a script to notify when Panasonic doorphone rings

## environment
- Panasonic VL-SWD300KL
  - You probably can use any doorphone with form A contact output
- Raspberry pi zero wh
  - Raspberry pi OS 2020-08-20
  - python 3.7.9

## Hardware setup
Put GPIO 2 and ground into doorphone's form A contact output (A接点出力).
Since it has no polarity, you can connect either port.

## Discord Webhook
Get your discord webhook URL and save it as a textfile named `discord_url` into the working directory.
For getting the webhook URL, visit here: 
https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks

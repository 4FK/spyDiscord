# spyDiscord
discord selfbot to relay a discord server to a webhook, made very poorly and quickly to spy on people
# requirements
discord.py, requests
# setup (for retards)
put the channels you wanna relay in this array
```spyChannels = [1234, 4321, 1337]```
put your webhook in the quotes
```webhookUrl = "https://discord.com/api/webhooks/FAKE/WEBHOOK"```
replace TOKEN with the account you want to spy on
```client.run("TOKEN", bot=False)```
and then run the script to start relaying messages

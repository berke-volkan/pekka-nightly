#python setup.py sdist bdist_wheel
#pip install dist/pekka-0.1-py3-none-any.whl --force-reinstall

#publish:
#twine upload dist/*

slack_app="Insert your Slack App Level Token here (xapp...)"
slack_bot="Insert your Slack Bot User OAuth Token here (xoxb...)"
discord_token="Insert your Discord Bot Token here (Bot Token)"

import pekka

app=pekka.app(slack_bot)
pekka.slash_command(app=app[0],discord_bot=app[1],command="hello", text="Hello from Pekka bot!",platform=["slack"])
pekka.slash_command(app=app[0],discord_bot=app[1],command="hey", text="This is a help message from Pekka bot.")
pekka.run_app(slack_app=slack_app,discord_token=discord_token,sapp=app[0],discord_bot=app[1])

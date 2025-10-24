#python setup.py sdist bdist_wheel
#pip install dist/pekka-0.1-py3-none-any.whl --force-reinstall

#publish:
#twine upload dist/*
#pypi-AgEIcHlwaS5vcmcCJDJmMmQwNGY2LTU1NzEtNDViOC1hOGMwLTAwNTUwOTNlODhlMAACKlszLCJiZjgyMGQxNC05MzU5LTQ1NWEtODIzMS02NGZjZGFhOTRiNDAiXQAABiA5cDdUBveb6E39IqyGlQhB30vOUKM0uBqYv1IcD_CgZw
slack_app="xapp-1-A09MUEPTW3H-9786258264144-9c7adc177137c3a2ab8401e9cfcf6f7096a9eba4c7a6eb68612777879dcf441e"
slack_bot="xoxb-2210535565-9761529116596-exH2izSAyn558vFNdHZI2qfy"
discord_token="MTQzMTMwOTY3ODUwMzAwNjI1OA.GCgse-.Mw4hR2ONjjYhjhYsATmVTUi1xiwzIaMkkPvsks"

import pekka

app=pekka.app(slack_bot)
pekka.slash_command(app=app[0],discord_bot=app[1],command="hello", text="Hello from Pekka bot!",platform=["slack"])
pekka.slash_command(app=app[0],discord_bot=app[1],command="hey", text="This is a help message from Pekka bot.")
pekka.run_app(slack_app=slack_app,discord_token=discord_token,sapp=app[0],discord_bot=app[1])

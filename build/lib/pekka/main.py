from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from discord.ext import commands
import discord
from openai import OpenAI
def hello():
    print("Hello, World!")

def app(slack_bot):
    app = App(token=slack_bot)
    discord_bot = commands.Bot(command_prefix="!")
    APP=app
    return APP,discord_bot

def slash_command(app,command,text,discord_bot,platform=["slack","discord"]):
    if "slack" in platform:
        @app.command(f"/{command}")
        def handle_command(ack, respond):
            ack()
            respond(text)
    if "discord" in platform:
        @discord_bot.slash_command(name=command, description=text)
        async def command(ctx: discord.ApplicationContext):
            await ctx.respond(text)


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="<OPENROUTER_API_KEY>",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="deepseek/deepseek-chat-v3-0324:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)
def run_app(sapp,slack_app,discord_bot,discord_token):
    import threading
    import asyncio
    def _run_discord():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(discord_bot.start(discord_token))
        finally:
            try:
                loop.run_until_complete(loop.shutdown_asyncgens())
            except Exception:
                pass
            loop.close()

    t = threading.Thread(target=_run_discord, name="discord-bot")
    t.daemon = True
    t.start()
    handler = SocketModeHandler(sapp, slack_app)
    handler.start()

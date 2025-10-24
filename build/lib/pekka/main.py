from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from discord.ext import commands
import discord

def hello():
    print("Hello, World!")

def app(slack_bot):
    app = App(token=slack_bot)
    discord_bot = commands.Bot(command_prefix="!")
    APP=app
    return APP,discord_bot

def slash_command(app,command,text,discord_bot):
    @app.command(command)
    def handle_command(ack, respond):
        ack()
        respond(text)
    @discord_bot.slash_command(name=f"{command}", description=f"{text}")
    async def command(ctx: discord.ApplicationContext):
        await ctx.respond(text)

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

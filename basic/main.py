import discord
from discord.ext import commands


class BasicBot(commands.Bot):
    """A single-line docstring giving a brief description of the bot"""

    def __init__(self, *args, **kwargs):
        # It is good practice to manually specify every intent that you will use
        # instead of using discord.Intents.all()
        intents = discord.Intents(
            guilds=True,
            members=True,
            # TODO: Add specific intents as you like
            # Ref: https://discordpy.readthedocs.io/en/stable/api.html#discord.Intents
        )
        super().__init__(
            *args,
            **kwargs,
            command_prefix="",  # FIXME: Add a prefix you like
            intents=intents,
        )

    async def on_ready(self):
        # PS: Do NOT add stuff here. This function is called MULTIPLE times
        # as the client re-connects. If you wish to do one-time things,
        # please use `setup_hook` below.
        assert self.user is not None
        self.logger.info(f"Logged in as {self.user} (ID: {self.user.id})")

    async def setup_hook(self) -> None:
        # Run all your initual setup here.
        pass

    def run(self):
        super().run("BOT_TOKEN", reconnect=True)


if __name__ == "__main__":
    bot = BasicBot()
    bot.run()

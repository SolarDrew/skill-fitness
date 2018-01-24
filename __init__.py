import logging

from opsdroid.message import Message
from opsdroid.matchers import match_always, match_crontab


def setup(opsdroid):
    logging.debug("Loaded fitness module")


@match_crontab("* * * * *", timezone="Europe/London")
async def random_excercise(opsdroid, config, message):
    # Get the main connector and room
    connector = opsdroid.default_connector
    room = connector.default_room

    # Create an empty message to respond to
    message = Message("", None, room, connector)

    # Prompt the user
    await message.respond("Do some excercise!")


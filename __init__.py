import logging
from numpy import random

from opsdroid.message import Message
from opsdroid.matchers import match_always, match_crontab


def setup(opsdroid):
    logging.debug("Loaded fitness module")


def choose_victim(users):
    """Randomly choose one from a list of the people in the room."""
    n = len(users)
    weights = [0.5, 0.1] + ([0.4/n]*n)
    return random.choice([None, 'Everybody']+users, p=weights)


def choose_excercise(excercise_options):
    """Randomly select one from the list of designated exercises."""
    return random.choice(excercise_options)


def choose_number():
    """Determine number of repetitions for the selected exercise."""
    return round(random.normal(loc=10, scale=2))


@match_crontab("/15 9-17 * * 1-5", timezone="Europe/London")
async def random_excercise(opsdroid, config, message):
    # Get the main connector and room
    connector = opsdroid.default_connector
    room = connector.default_room

    # Create an empty message to respond to
    message = Message("", None, room, connector)

    # Choose who's doing the excercise this time.
    user = choose_victim(config['participants'])
    if not user:
        return
    excercise = choose_excercise(config['excercises'])
    n = choose_number()

    # Prompt the user
    await message.respond(f"{user}, do {n} {excercise}! RIGHT NOW!")


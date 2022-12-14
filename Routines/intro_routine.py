from Assets.application import Application
import click, Utils.messaging_util as mU

def intro_routine(routine: Application):
    game_title = routine.game_data["title"]
    mU.print_title(game_title)
    
    intro_msg = routine.game_data["messages"]["intro"]
    click.pause(intro_msg)

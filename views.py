from route_helper import simple_route
from flask import Flask, render_template
from flask import request


@simple_route('/')
def index(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    return render_template("index.html")



def INITIATION(location):
    return render_template(f"{location}.html")
#def GAME_HEADER():
#    return render_template("FirstObstacle.html")
@simple_route('/goto/<where>/')
def open_door(world: dict, where: str) -> str:
    """
    Tell the user they are spiderman and prompt the player
    to give them a name.

    :param world: The current world
    :param where: The new location to move to
    :return: The HTML to show the player
    """
    world['location'] = where
    return INITIATION(world['location'])

#@simple_route('/goto/')
@simple_route("/save/name/")
def save_name(world: dict, Spider_name: str) -> str:
    """
    Update the name of Spiderman.

    :param world: The current world
    :param monsters_name:
    :return:
    """
    world['name'] = Spider_name

    return render_template("FirstObstacle.html", name=Spider_name)

@simple_route('/yes/')
def answer(world: dict):
    return render_template("answer.html")
@simple_route('/no/')
def answer2(world: dict):
    return render_template("No.html")\


@simple_route('/move/', methods=["POST"])
def move(world:dict, *args):
    if request.values["move"]=="water":
        return render_template("waterhim.html")
    else:
        return render_template("webs.html")
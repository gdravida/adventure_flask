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
    '''
    prompt the user to pick a training move
    :param world: The Current World
    :return:
    '''
    return render_template("training.html")
@simple_route('/no/')
def answer2(world: dict):
    '''
    ask the user if they are sure about the decision and give the option to go back
    :param world:
    :return:
    '''
    return render_template("No.html")
@simple_route('/response2/', methods=["POST"])
def response(world:dict, *args):
    '''
    either they see the page about training again or they are told they let the city down
    :param world:
    :param args:
    :return:
    '''
    if request.values["response"]=="Yes":
        return render_template("letgo.html")
    else:
        return render_template("training.html")

@simple_route('/kick/')
def kick(world: dict):
    '''
    tells them that they have mastered the kick and prompt them to choose a move to execute
    :param world:
    :return:
    '''
    return render_template("kick.html")
@simple_route('/punch/')
def punch(world: dict):
    '''
    tells them that they have mastered the punch and prompt them to choose a move to execute
    :param world:
    :return:
    '''
    return render_template("punch.html")

@simple_route('/move/', methods=["POST"])
def move(world:dict, *args):
    '''
    they either see that they kicked the Sandman into water and killed him or didn't master the move and got killed
    :param world:
    :param args:
    :return:
    '''
    if request.values["move"]=="water":
        return render_template("waterhim.html")
    else:
        return render_template("webs.html")

@simple_route('/move2/', methods=["POST"])
def move2(world:dict, *args):
    '''
    they either see that they punched the Sandman into water and killed him or didn't master the move and got killed

    :param world:
    :param args:
    :return:
    '''
    if request.values["move2"]=="water":
        return render_template("waterhim2.html")
    else:
        return render_template("webs2.html")

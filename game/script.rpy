# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define M = Character("Mysterious Voice", who_color = "#ffffff")
define Me = Character ("Me")
define player = Character("[name]")
image black = "#000000"

# The game starts here.

label start:
    scene black

    "Ugh my head... What happened...?"

    # apparently renpy puts file names in all lowercase

    "I manage to crack my eyes open and..."

    scene earth blurred with dissolve

    "Huh?"

    M "Great, you finally woke up."

    "A sarcastic voice rings out all around me. My head throbs with an incessant headache."

    M "I'll give you a second."

    scene earth with dissolve

    "Huh? That's... the Earth?!"

    Me "What's going on? Why do I see the Earth? Like the whole Earth? Is this space? How is"

    M "Let me cut you off."
    M "Well for starters, yeah we're above the Earth right now. I guess you could say the heavens."
    M "Yup."

    "This voice is irksome."

    M "Now let's see… "

menu:

    "Sure…":
        jump yes
    "No":
        jump no

label yes:

    python:
        player = renpy.input("Sign Here")
        player = player.strip()

    player "My name is [player]!"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy


    # This ends the game.
label no:
    return

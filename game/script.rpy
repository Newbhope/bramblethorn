# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mysterious Voice", who_color = "#ffffff")
define me = Character ("Me")
define player = Character("[player]")
image black = "#000000"

# The game starts here.

label start:
    scene black

    "Ugh my head... What happened...?"

    # apparently renpy puts file names in all lowercase

    "I manage to crack my eyes open and..."

    scene earth blurred with dissolve

    "Huh?"

    m "Great, you finally woke up."

    "A sarcastic voice rings out all around me. my head throbs with an incessant headache."

    m "I'll give you a second."

    scene earth with dissolve

    "Huh? That's... the Earth?!"

    me "What's going on? Why do I see the Earth? Like the whole Earth? Is this space? How is"

    m "Let me cut you off."
    m "Well for starters, yeah we're above the Earth right now. I guess you could say the heavens."
    m "Yup."

    "This voice is irksome."

    m "Now let's see…"
    m "Says on this page that you died from… falling? Haha what a way to go."
    me "...What did you say?"
    "The voice keeps rattling on ignoring my question"
    m "Oh man. I misplaced the rest of your file. Crap."
    m "Hey, could you tell me your name?"

menu:
    "Sure…":
        jump yes
    "Are you kidding me?!?":
        jump no
label no:
    m "Nope!"
    m "Look, the sooner you give me your name, the sooner we can get this ball rolling."

menu:
    "Fine.":
        jump name
    "No.":
        jump reject

label yes:
    m "Thanks buddy!"
label name:

    python:
        player = renpy.input("My name is...")
        player = player.strip()

    m "Great thanks [player]."

    m "Sadly I don't have much time. Other dead people to get to you know. So I'm just going to do this real quick."

    scene lake with dissolve
    scene nature1 with dissolve
    scene nature2 with dissolve
    scene nature4 with dissolve
    scene snow with dissolve
    scene sunshine with dissolve
    scene nature3 with dissolve

    m "Well, apologies. Looks like we're out of time. I'll send you back. Make sure you reycle and stuff."

    jump end

label reject:
    m "Well I have all day. Haha, get it? Because we're always on the day side of the Earth?"
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    "Fine."
    
    jump name
label end:
    return

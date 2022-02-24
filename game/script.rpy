################################################################################
## Character Definitions
################################################################################

define cas = Character("Casper", color = "#38b95f")
define mc = Character("[name]", image = "mc",  color = "#227cf1")


################################################################################
## Images
################################################################################
image cas neutral = im.FactorScale("images/casper/hoodie/neutral.png", 0.5)
image cas smile = im.FactorScale("images/casper/hoodie/smile.png", 0.5)
image cas laugh = im.FactorScale("images/casper/hoodie/laugh.png", 0.5)
image cas grin = im.FactorScale("images/casper/hoodie/grin.png", 0.5)
image cas smirk = im.FactorScale("images/casper/hoodie/smirk.png", 0.5)
image cas angry = im.FactorScale("images/casper/hoodie/angry.png", 0.5)
image cas annoyed = im.FactorScale("images/casper/hoodie/annoyed.png", 0.5)
image cas grumpy = im.FactorScale("images/casper/hoodie/grumpy.png", 0.5)
image cas shocked = im.FactorScale("images/casper/hoodie/suprised.png", 0.5)
image cas blank  = im.FactorScale("images/casper/hoodie/blank.png", 0.5)
image cas sad = im.FactorScale("images/casper/hoodie/sad.png", 0.5)
image cas crying = im.FactorScale("images/casper/hoodie/crying.png", 0.5)
image cas sad smile = im.FactorScale("images/casper/hoodie/sad-smile.png", 0.5)
image cas crying smile = im.FactorScale("images/casper/hoodie/crying-smile.png", 0.5)

image mc neutral = im.FactorScale("images/mc/neutral.png", 0.5)
image mc smile = im.FactorScale("images/mc/smile.png", 0.5)
image mc laugh = im.FactorScale("images/mc/laugh.png", 0.5)
image mc grin = im.FactorScale("images/mc/grin.png", 0.5)
image mc smirk = im.FactorScale("images/mc/smirk.png", 0.5)
image mc angry = im.FactorScale("images/mc/angry.png", 0.5)
image mc annoyed = im.FactorScale("images/mc/annoyed.png", 0.5)
image mc grumpy = im.FactorScale("images/mc/grumpy.png", 0.5)
image mc shocked = im.FactorScale("images/mc/suprised.png", 0.5)
image mc blank  = im.FactorScale("images/mc/blank.png", 0.5)
image mc sad smile = im.FactorScale("images/mc/sad-smile.png", 0.5)
image mc sad = im.FactorScale("images/mc/sad.png", 0.5)


################################################################################
## Game
################################################################################

label start:
    label setup:
        show mc neutral
        "You'll be playing this character."

        python:
            name = renpy.input("What should their name be?", default="Jayne")

            name = name.strip()
        
    scene bg living room:
        zoom 0.7
    show mc smile at right
    show cas sad at left
    mc "It'll be ok."
    return

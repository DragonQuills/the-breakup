################################################################################
## Character Definitions
################################################################################

define cas = Character("Casper", color = "#38b95f")
define mc = Character("[name]", image = "mc",  color = "#227cf1")
define phone = Character("Text",  color = "#994f4f")


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
image cas suprised = im.FactorScale("images/casper/hoodie/suprised.png", 0.5)
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
image mc suprised = im.FactorScale("images/mc/suprised.png", 0.5)
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
    label warnings:
        # Add content warnings here.

    label intro:
        scene bg stairs:
            zoom 0.7

        show mc annoyed
        "I trudged up the stairs towards my apartment grumpily."
        "Today had been a long day and I was more than ready for bed."
        "Work had run late by almost 3 hours, I had somehow got caught in traffic despite the time, and the take-out I ordered was cold by the time I picked it up."
        "I got out my phone and shot off a text to Casper."
        
        phone "Just got home. Let's hang out soon? It feels like it's been forever."

        show mc blank
        "I sighed and tucked my phone back into my pocket, not expecting a reply until tomorrow at the earliest."
        "Casper and I had been best friends since middle-school. Though the friendship had evolved over the years, we were still as close as when we were kids."
        
        show mc sad
        "At least... I thought we were."
        "Over the past few months, Casper seemed like he'd been getting more distant."
        "He took much longer to respond to messages, rarely picked up calls, and when we spent time together in person he seemed distracted."
        "On top of that, he just felt... off to me."
        "I couldn't put my finger on what, but I had known him since before he lost his baby teeth. We had been together through graduating high school, our first jobs, his Dad's death, and his discovery of his trans identity and subsequent transition."
        "If something felt off to me, I trusted that there really was something wrong."
        "But every time I asked, Casper brushed me off and told me he was fine. He always gave some excuse - I'm just tired, I forgot to eat breakfast, work was hard today. But I knew there was something deeper going on."
        "It was odd for him to be concealing something like this, but I figured he had his reasons."
        "I would just continue to do what I always had - check in, remind him I'm here, and give him space to working things out and tell me in his own time."

        show mc suprised
        "My ringtone startled me, as loud as it was in the quiet staircase."
        "I looked at the caller ID - Casper. This had to have been the first time he had called me in two or three months."
        "I hurriedly picked up and pressed the phone to my ear."

        mc "Hello? Cas?"
        cas "..."
        mc "Casper? Are you there? Are you ok?"
        cas "{w}I...{w} I... {w}No, I..."
        show mc sad
        "I heard Casper's breath catch in his throat and my heart jumped into my chest. Something was wrong."
        
        menu:
            "\"Tell me what happened.\"":
                $ q = "Tell me what happened."
                jump what_happened
            "\"Tell me what's wrong.\"":
                $ q = "Tell me what's wrong."
                jump what_happened
            "\"Tell me how I can help.\"":
                $ know_broke_up = False
                jump how_help
        
        label what_happened:
            $ know_broke_up = True
            mc "[q]"
            "I hear a few seconds of ragged breathing."
            cas "I...{w} Taylor...{w} we...{w} he..."
            show mc grumpy
            mc "Did he hurt you?"
            cas "No!{w} No, no, he... he wouldn't."
            cas "He... broke up with me. {w} Like, just now. He... he just left."

            show mc sad
            mc "Oh... Oh Cas, I'm so sorry."
            
            label how_help:
                cas "C-could you come over? I... I really don't want to be alone right now."
        
        mc "Of course. I'll be right there."
        cas "Thanks. Really, thank you, I know I-"
        
        show mc neutral
        mc "It's ok. Don't worry about anyhting but yourself right now. I'll be over as soon as I can get there."
        show mc sad
        mc "Do you want to stay on the line while I drive?"
        cas "No, that's... that's ok. Focus on driving. I'll be fine until you get here, I'll just, sit here or something."
        mc "Ok. I'll drive carefully, but I'll be there really soon. Hang in there."
    
    return

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
image cas smile = im.FactorScale("images/casper/hoodie/happy.png", 0.5)
image cas laugh = im.FactorScale("images/casper/hoodie/laugh.png", 0.5)
image cas grin = im.FactorScale("images/casper/hoodie/grin.png", 0.5)
image cas smirk = im.FactorScale("images/casper/hoodie/smirk.png", 0.5)
image cas angry = im.FactorScale("images/casper/hoodie/angry.png", 0.5)
image cas annoyed = im.FactorScale("images/casper/hoodie/annoyed.png", 0.5)
image cas grumpy = im.FactorScale("images/casper/hoodie/grumpy.png", 0.5)
image cas surprised = im.FactorScale("images/casper/hoodie/surprised.png", 0.5)
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
image mc surprised = im.FactorScale("images/mc/surprised.png", 0.5)
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
        "I would just continue to do what I always had - check in, remind him I'm here, and give him space to work things out and tell me in his own time."

        show mc surprised
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
        mc "It's ok. Don't worry about anything but yourself right now. I'll be over as soon as I can get there."
        show mc sad
        mc "Do you want to stay on the line while I drive?"
        cas "No, that's... that's ok. Focus on driving. I'll be fine until you get here, I'll just, sit here or something."
        mc "Ok. I'll drive carefully, but I'll be there really soon. Hang in there."
    
    label approaching:    
        scene black
        hide mc
        "I rushed down the stairs and into my car, all of my earlier tiredness washed away by adrenaline."
        if not know_broke_up:
            "I didn't know what was happening but that wasn't important right now."
        "I needed to get to Casper as soon as I could. I trusted him when he said he would be ok until I arrived, but my heart still ached at how raw his voice was."
        "I drove as fast as I could safely go. Casper's apartment was 40 minutes away normally, but the lack of cars on the road plus gratuitous speeding meant I made the trip in 30."

        scene bg outside apt
        "When I arrived at Casper's apartment complex, I took the stairs two at a time. I knew the way to his apartment better than the way to my parent's house at this point, so the complex was easy to navigate despite the dark."
        show mc sad
        "I flew to his door, then slowed in front of it."
        menu:
            "Knock on the door.":
                jump knock
            "Text Casper that you're outside.":
                jump msg
            "Call out to Casper.":
                jump called
        
        label knock:
            "I rapped quietly on the door, then waited for Casper to let me in."
            "I didn't hear anything from inside the apartment."
            "My phone chimed Casper's text tone."
            phone "is thta you ousdid"
            "I messaged back right away."
            phone "Yeah, it's me."
            jump in_the_apartment

        label msg:
            "I shot off a quick text to Casper."
            phone "I'm outside."
            "My phone immediately chimed back."
            phone "brt"
            jump in_the_apartment

        label called:
            "I called out, loud enough that my voice would carry but hopefully quiet enough the neighbors wouldn't complain."
            mc "Casper? It's [name]. I'm out front."
            "I heard shuffling sounds from inside the apartment."
            jump in_the_apartment

    label in_the_apartment:
        scene bg doorway dark
        show cas sad smile
        with Dissolve(1)
        cas "Hey. Thank you for coming."
        mc "Of course."
        
        "Cas reached behind himself and flipped a light switch."
        scene bg doorway
        show cas sad smile
        cas "Heh. I guess I didn't realize how dark it had gotten."

        show cas neutral at right
        show mc neutral at left
        with moveinleft
        cas "C'mon in."

        "We stepped inside and I followed Casper to his living room."

        show bg living room with Dissolve(1)
        show cas blank
        "Cas sat down on the couch and curled his knees up to his chest."
        show cas neutral
        cas "Seriously, thank you so much for coming over."
        show cas sad smile
        cas "I... I haven't been a very good friend lately and it really means a lot to me that you came. I just- "

        menu:
            "Let him say what's on his mind":
                jump cas_apology
            "Tell him not to worry about it":
                jump dw_fam
        
        label cas_apology:
            show cas sad
            show mc blank
            cas "I haven't been very responsive lately and I know I've been spacey when we hang out."
            cas "I just... there's been a lot going on but I didn't know how to tell you about any of it and..."
            show cas sad smile
            cas "...And I was worried you would ask questions I didn't want to think about the answers to."
            show cas sad
            cas "But I still shouldn't have dodged your calls or avoided you like I have been, and I'm sorry."
            cas "Thank you for coming over despite that."

            menu:
                "\"Thank you for apologizing.\"":
                    show mc smile
                    mc "Thank you for the apology."
                    mc "I was a bit hurt that you we ghosting me like that, but I also figured there had to be a reason."
                    mc "I'm glad you reached out tonight and I'm here now."
                    jump sitting
                "\"It's ok.\"":
                    show mc smile
                    mc "Don't even worry about it at all. I didn't take it personally, I just figured you had some stuff you were dealing with and that you would tell me about it when you were ready."
                    show cas sad
                    cas "But..."
                    mc "Cas, I've known you for over a decade. I know you didn't mean any harm and I'm not mad."
                    show cas neutral
                    cas "Ok. Thank you."
                    jump sitting
        
        label dw_fam:
            show mc smile
            show cas sad
            mc "Don't worry about that at all right now."
            cas "But..."
            mc "We can talk about it later if you really want to, but right now my first priority is helping you."
            show cas neutral
            cas "Ok. Thank you."

        label sitting:
            show mc sad
            show cas sad
            mc "Are you ok with telling me what happened?"
            "Cas gives a small nod."
            if know_broke_up:
                cas "Uh, I guess I already told you Taylor broke up with me."
            if not know_broke_up:
                show mc sad
                cas "Uh. Yeah, I guess the first think you should know is Taylor broke up with me."
                cas "He left a little before I called you."
                "Cas lets out a deep, shuddering breath."
                mc "Oh... Oh Cas, I'm so sorry."
            
            show cas sad smile
            cas "It's... it's probably for the best."

    "The End"
    return

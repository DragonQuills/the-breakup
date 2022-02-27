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
        hide mc
        
        "This game contains themes of aphobia and toxic relationships, but the game has a happy ending. It's kind of a rough read though, not gonna lie."
        "It has a lot of grief processing, but your character is there to help."
        $ show_warnings = True
        while show_warnings:
            menu: 
                "Would you like any more details on either of those? Details include spoilers."
                "Aphobia":
                    "The main character's best friend, Casper just went through a break up with his boyfriend Taylor."
                    "There were many factors at play, but the final thing that caused the breakup was Casper admitting he did not want to have sex, and Taylor being upset by that."
                    "Casper is not aware he is asexual at the start of the game, so there is also a lot of internalized aphobia, such as him asking the main character why he can't just 'be normal.'"
                    "Over the course of the game, Casper learns what asexuality is and begins to realize that there is nothing wrong with him."
                "Toxic relationship":
                    "The main character's best friend, Casper just went through a break up. Casper and his ex, Taylor, were both not good for each other."
                    "Taylor was jealous and suspicious, and very codependent. Casper was bitter and short tempered due to his frustration with Taylor's behavior."
                    "There was not physical, sexual, or verbal abuse, but there were some elements of emotional manipulation."
                    "By the beginning of the game, the relationship has already ended and Casper is dealing with his emotions around it."
                    "Casper will not resume his relationship with Taylor, however you have a role in deciding if he stays in contact with Taylor."
                "Nah, I'm good.":
                    $ show_warnings = False
        "Please remember to take care of yourself. Take breaks or stop playing if you need to!"
        "Another thing to note - this game is not a dating sim and there is no way to romance Casper."
        "You will have opportunities to physically comfort Casper by hugging him, holding his hand, and so on."
        "These will not be framed as or taken as romantic advances, but rather as platonic shows of affection."
        "Finally, the main character's pronouns are not asked because the main character is not referred to in the third person at any point, since the game is almost exclusively two characters interacting one-on-one."
        "Thanks, and have fun!"

    label intro:
        scene bg stairs:
            zoom 0.7
        play music "audio/Relax.ogg"

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

        play music "audio/Splatters.ogg" fadeout 1 fadein 1
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
        play music "audio/GuitarOnTheWater.ogg" fadeout 1 fadein 1

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
                    jump couch_time
                "\"It's ok.\"":
                    show mc smile
                    mc "Don't even worry about it at all. I didn't take it personally, I just figured you had some stuff you were dealing with and that you would tell me about it when you were ready."
                    show cas sad
                    cas "But..."
                    mc "Cas, I've known you for over a decade. I know you didn't mean any harm and I'm not mad."
                    show cas neutral
                    cas "Ok. Thank you."
                    jump couch_time
        
        label dw_fam:
            show mc smile
            show cas sad
            mc "Don't worry about that at all right now."
            cas "But..."
            mc "We can talk about it later if you really want to, but right now my first priority is helping you."
            show cas neutral
            cas "Ok. Thank you."

        label couch_time:
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
            "Cas had been so excited when he and Taylor had started dating. Taylor was his first boyfriend, and Cas was head-over-heels for him."
            "I didn't know much about Taylor. I had only met him a handful of times, always in passing. He seemed nice enough."
            "I just nodded at Cas. I didn't really feel like I knew enough about their relationship to comment."
            
            show cas sad
            cas "Things... things have been rough with us for a while now."
            cas "More fighting, more uncomfortable quiet, more nights going to sleep hurt or angry."
            cas "I... didn't want to tell you about it. I didn't want you to think badly of him, or of me."

            "Cas met my eyes with intensity."
            show cas grumpy
            cas "He's... he's not a bad person. He's just been through a lot and sometimes... I think sometimes it just gets to be too much for him and he lashes out."
            show cas sad
            cas "Or I do or say the wrong thing and he just goes cold."
            cas "He's never been awful to me, or anything like that. Just, sometimes he gets..."
            "Cas's voice gets so small I have to lean in to hear it."
            cas "Sometimes he's just, kind of... mean."
            "Cas's body started shaking."

            menu:
                "Hug him":
                    "I wrapped my arms around Cas and squeezed tightly."
                    "He gave a little squeeze back and rested his head on my shoulder."
                    cas "Thanks..."
                    "Cas pulled back from me after a few moments."
                "Get him some water.":
                    show mc neutral
                    mc "One sec."
                    "I grabbed a cup of water from the kitchen and handed it to Cas."
                    cas "Thanks."
                    "Cas took a few small sips."
            
            cas "I... I think I want to keep talking about this."
            cas "I didn't tell you or anyone else about any of this but I think I need to."
            cas "I think I should have talked about it earlier. Maybe..."
            "Another breath. Tears well up in his eyes."
            show cas crying smile
            cas "Maybe things would have gone differently tonight if I had."
            
            menu:
                "Hold his hand":
                    "I reached out and took Casper's hand, giving it a firm squeeze."
                    show mc sad smile
                    mc "Talk about whatever you need to. I'll listen."
                    show cas sad smile
                    "Cas wraps his fingers around mine."
                    cas "Ok. Thank you."
                    $ holding_hands = True
                "Stay quiet":
                    "I give a small nod to show I'm listening."
                    $ holding_hands = False
            
            show cas sad smile
            show mc sad
            cas "Taylor's last relationship was really bad. {w}Like {i}really{/i} bad."
            cas "It's not my place to talk about what happened."
            cas "But because of it, Taylor's always been really insecure."
            cas "At first, I thought it was just a normal relationship thing. It wasn't like it was bad, he just wanted me to reassure him that I loved him pretty often."
            cas "And I was happy to remind him that because of course I care about him, and I want him to know it."
            show cas sad
            cas "But... It didn't get better. It got worse as time went on."
            cas "He started getting really scared when I didn't see him for a while, especially if I was hanging out with someone else."
            cas "I always told him that it was fine and I made as much time as I could but... it wasn't enough."
            cas "That was part of why I've been so bad about responding to you."
            cas "I just didn't want to stress him out, and I knew that he worried about it when I saw you so I just sort of... stopped responding."
            "Cas swallows hard."
            show cas crying smile
            cas "It. It sounds so bad when I say it like that, huh?"
            cas "He never asked me to avoid you or anything like that I just didn't want to hurt him. But I guess I did anyway, huh?"
            if holding_hands:
                "I gave Casper's hand what I hoped was a comforting squeeze, and he squeezed back."
            show cas sad
            cas "I... I haven't been the nicest person to him recently."
            show cas grumpy
            "Casper's voice rose."
            cas "It, it just got so frustrating!"
            cas "I kept telling him I cared and that I only had eyes for him but he just wouldn't believe me."
            cas "And he kept questioning who I was with and where I went."
            "His voice returned to a whisper."
            show cas sad
            cas "I know he was just scared, but I just got so tired of having to constantly explain myself and walk on eggshells around him."
            cas "And I barely had time or energy for anything else. I haven't gone running in almost a month. I've barely even cooked recently."
            cas "So I guess I started getting short with him, and took longer and longer to text him back. But of course that just made everything worse."
            cas "Tonight everything just... all came to a head."
            
            show cas crying
            "Cas let out a sob."
            cas "I... I need a second."
            mc "We don't have to keep talk-"
            "Cas shook his head firmly."
            cas "No, I, I need to talk about this. But I just. {w}I can't deal with it right now. {w}I need to pull myself back together."
            
            mc "I understand."
            
            menu:
                "Do you want to go for a walk?":
                    show cas sad smile
                    cas "In the middle of the night?"
                    show mc grin
                    mc "Sure, why not?"
                    "I tried cracking a joke to see how it would land."
                    mc "I'm pretty sure the two of us could take down..."
                    "I looked Casper up and down."
                    mc "Like at least 3 and a half bears."
                    show cas laugh
                    "That was absurd enough to startle a laugh out of Casper."
                    cas "Haha!"
                    show cas neutral
                    cas "A walk sounds good."
                    jump walk
                "Do you want to watch a show?":
                    jump tv
    # TODO: Add more conversation about your relationship with Casper, or his relationship with Taylor here.
    label walk:
        "We went for a walk until Casper calmed back down."
        jump resume_talk
    label tv:
        "We watched a few TV shows until Casper calmed down."
        jump resume_talk

    
    label resume_talk:
        scene bg bedroom:
            zoom 0.8
        show mc neutral at left
        show cas neutral at right
        with Dissolve(1)
        "We went into Casper's room together and sat down on the bed."
        menu:
            "Invite Casper to put his head on your lap.":
                $ on_lap = True
                show mc smile
                "I tapped my legs with my hands."
                mc "Do you want to rest your head on my legs?"
                "Casper thought for a moment."
                cas "Yeah. That would be really nice, actually."
                "Casper curled up on his side and lay his head down on my lap, facing upwards."
                "I stroked his hair gently."
                show cas smile
                cas "Thank you."
            "Just sit together.":
                $ on_lap = False
        show mc sad
        "After a long pause, I spoke."
        show cas sad
        mc "...Do you want to keep talking about what happened?"
        "Casper gave a tentative nod."
        cas "I think I should, yeah."

        "Casper took a deep breath, held it for a moment, then let it out."
        cas "Ok. I need to give you a little more background first, though."
        "I nodded."
        mc "I'm all ears."
        cas "Ok. {w} Ok."

        show cas blank
        show mc blank
        play music "audio/Death.ogg" fadeout 1 fadein 1
        cas "Do you remember how, in health class during middle school, I covered my ears during the sex portions a lot?"
        "I nodded. Casper had been very uncomfortable with anything related to sex. Even when the teacher had asked him not to, or the other kids teased him about it, he had continued covering his ears or putting headphones on when he got overwhelmed."
        "I hadn't really understood why at the time, just that he was unhappy. I teased him about it the first day, but he burst into tears."
        "After realizing just how upset it made him, I tried to cover for him when I could by joking around to distract the other kids or asking the teacher questions before she could say anything to Cas."
        cas "Well, that feeling, being uncomfortable with sex? It never really went away."
        show cas grumpy
        cas "During high school when the other guys were talking about their. Ugh. {i}Conquests.{/i}"
        cas "... I tried to play along, but it really sickened me. Not just hearing them talk about people like that, though that was a big part of it."
        show cas sad
        cas "But also the details really... freaked me out."
        if on_lap:
            show mc neutral
            "I pet his hair and gave him a sympathetic smile."
            show cas neutral
            cas "Thanks."
            "He nuzzled into my hand and I rubbed the start of a tear from the corner of his eye."
        show cas smile
        cas "I'm glad you never talked about that kind of thing with me."
        show mc grin
        mc "Pft, of course not. There are way more interesting things to talk about than sex-ploits, especially since neither of us were even in relationships. I'm sure at least two thirds of those guys were lying anyway."
        cas "Yeah, probably."
        "Thinking back to high school, I had never realized that Casper was uncomfortable with the sexual nature of the conversations the guys were having, and not just how awful they were to women."
        "A suspicion started forming in my mind, but I kept it to myself for now. I could bring it up later."
        
        show cas blank
        show mc blank
        cas "So anyway, that brings us to more recently. I'm {i}still{/i} really uncomfortable with sex."
        show cas sad smile
        cas "I avoided having sex as long as I could with Taylor. I told him I wanted to take things slow but... I was really scared."
        cas "I love kissing and cuddling and sometimes even making out, but that's where it ends for me."

        "Cas started speaking faster, stumbling over his words."
        if on_lap:
            "I squeezed his shoulder gently and his pace slowed, just a bit."
        cas "It took months for us to start kissing and even longer to start making out but... after that I starting making excuses."
        show cas sad
        cas "I was so scared to tell him that I... didn't want him when he clearly wanted me."
        cas "So I told him I was too tired, or that I wasn't in the mood, or, or-"
        show cas crying smile
        cas "I even set up my phone to act like I was getting a call a few times. How ridiculous is that?"
        "Cas's pace picked up more, a rapid patter of words building louder."
        cas "I couldn't tell him! He would think it was about him and it's not about him, it's never been about him!"
        cas "I just can't have sex!"

        show cas crying
        cas "He wanted to have sex tonight and I was tired of dancing around it and pretending, so I didn't make an excuse. I just told him no."
        cas "And that really upset Taylor. He... really lost his head."
        "Cas sniffled."
        cas "He. He accused me of sleeping with someone else."
        show mc angry
        "Before I fully thought it through, I blurted out-"
        mc "That's ridiculous! Cas, you've never cheated on anything in your life! You barely even lie!"
        show cas sad smile
        cas "I know. But Taylor didn't believe me."
        show cas crying
        show mc sad
        cas "He told me that I must be sleeping with someone else on the side, that it was why I wasn't ever interested in sex with him."
        cas "I started blurting things out, I tried to explain that it wasn't about him but he just, he was too upset to listen."
        cas "He told me that he couldn't be with me, not when I made him feel so unwanted and scared and then he just... left."
        "Cas stared directly at me."
        cas "I need you to understand, I don't think he truly meant what he said. He was just hurt, and I should have been more careful..."
        cas "His eyes, and, and his posture..."
        show cas crying smile
        "Cas gave a joyless smile."
        cas "He was panicking so badly. I think he might have even started having a panic attack after a bit."

        menu:
            "\"This isn't your fault.\"":
                pass
            "\"He shouldn't have treated you like that.\"":
                pass

        "Cas didn't even seem to hear me."
        show cas crying
        cas "Why... why couldn't I just have had sex with him?"
        show cas angry
        cas "God dammit!"
        "Cas balled up his hands and pressed them to his forehead."
        cas "Why can't I just be normal?"
        show cas crying
        
        if on_lap:
            "I reached out and gently unballed one hand. It was shaking."
            "He wrapped his fingers around mine like a lifeline, squeezing so hard it hurt."
        "Casper was fully crying at this point, sobs shaking his body."

        cas "Why can't I be normal?"
        cas "Why do I have to be some... some freak who can't have sex with his partner!"
        cas "I love him so much but I just couldn't-"
        "He gasped out another sob."
        cas "Not even for Taylor, I just couldn't..."

        menu:
            "Tell Casper you think he might be ace.":
                $ still_crying = True
                "It might not be the right time, and maybe it wouldn't land, but he had to know that he wasn't a freak."
            "Try to help him calm down first.":
                $ still_crying = False
        
        show mc sad smile
        "I spoke softly but firmly."
        mc "Hey."
        "Cas didn't respond. He wasn't even looking at me."
        "I tried again, a little louder."
        mc "Hey. Casper, hey, look at me."
        show cas crying
        "This time Cas startled slightly, then looked at me. His eyes were glassy and distant."
        show mc neutral
        "I spoke slowly, making eye contact."
        if still_crying:
            jump ur_ace_bro
        mc "Casper. I'm glad you're processing this but I think we need to bring you back down a little."
        mc "Ok?"
        "Casper shook and let out a stuttering breath."
        cas "O-ok."
        show mc smile
        "I started on a grounding technique Casper had told me about. He had learned it from a therapist shortly after his Dad died."
        mc "Can you tell me five things you can see?"
        "Casper's eyes flitted rapidly from spot to spot, not quite focusing."
        cas "T-there's, uh, you next to me."
        mc "Yep. What else."
        cas "And there's the w-window over there. And my plant by the door."
        "I nodded."
        mc "Mhm. That's three."
        cas "M-my desk too. And there's the book I was reading on it."
        show cas sad
        "As he spoke, Casper's breaths were slowing and his shaking was subsiding slightly."
        show mc grin
        mc "Good job, you're doing great."
        show mc neutral
        mc "Can you list four things you can hear?"
        cas "Yeah. There's the air conditioner running. And I think I can hear a car going by outside."

        "We continued this way, counting down things Cas could see, hear, feel, smell, and taste until his breath had come back to normal."
        if on_lap:
            "The whole time, I ran my fingers through his hair, hoping to provide some comfort."
        "Eventually, after Cas had calmed back down, I decided to broach the topic of his sex aversion."
        
    label ur_ace_bro:
        # TODO: add the other term here
        show mc neutral
        play music "audio/EvansFull.ogg" fadein 1 fadeout 1
        mc "Have you heard the term asexual?"
        if still_crying:
            "Cas startled a little and looked confused. He blinked several times as his eyes strained to focus."
        else:
            show cas blank
        cas "Asexual's where... it's where someone doesn't want to date anyone, right?"
        "I shook my head."
        mc "You're thinking of aromantic. People get them mixed up or conflate them a lot."
        
        if still_crying:
            "Cas continued to look at me, his shakes slowing a bit as he tried to focus on my words."
        "I paused for a moment, trying to work out exactly how to say what I meant to."
        mc "Asexual, in the most simple terms, means someone who doesn't feel sexual attraction."
        mc "There's a spectrum of course, but right now we don't need to go into that."
        mc "What's important is that some asexual people are also sex-repulsed, which means they're disgusted or uncomfortable with the idea of having sex with someone."
        "I paused again as Cas stared up at me, understanding not quite dawning on him yet."
        mc "I think that there's a pretty go chance that you're asexual, and it sounds like you're sex-repulsed too."
        
        if still_crying:
            "Casper sniffed hard and wiped his eyes."

        cas "There's... there's a word for that kind of thing?"
        "I nodded several time firmly."
        mc "Yeah, and there are a lot of other people who feel like you've been describing."
        show cas surprised
        "Cas's eyes widened."
        cas "What does that mean...?"
        show mc sad
        "My chest felt heavy thinking about how long Cas must have been carrying his feelings without telling me or anyone else. I spoke with fervor, desperately needing my words to get through to him."
        mc "Cas, it means there's nothing wrong with you. You're not a freak, you're not broken. There are hundred of thousands of people who feel this way and there's nothing wrong with it."
        show cas blank
        "I could see him turning it over in his mind."
        show cas sad
        cas "I... I'm not broken?"
        if on_lap:
            "I clutched Cas's shoulder tightly."
        else:
            "I shook my head."
        mc "No, of course you're not."
        cas "I... I think I need a second to think about all this."

        show cas blank
        cas "... You promise you're not just making this up or something?"
        show mc surprised
        mc "No! I would never!"
        "Cas nodded quickly."
        show cas sad
        cas "Yeah, sorry, of course you wouldn't."
        show cas sad smile
        show mc sad
        cas "I'm just gonna... Think for a bit, ok?"
        menu:
            "Offer to get some food and give Cas some space.":
                jump get_food
            "Offer to sit with him while he thinks.":
                mc "Do you want me to sit here with you for a bit?"
                "Cas shrugged."
                cas "Ok. I'm just going to be in my own head for a while though. Might do a little reading about asexual people on my phone."
                jump sit_with_cas
                

        label get_food:
            mc "I could order us some take-out if you want a little space."
            cas "That... would actually be great. Geez, what time even is it?"
            "I checked the clock."
            show mc sad smile
            mc "It's a little after three AM."
            cas "Oof. I don't think I've eaten since this time in the afternoon."
            mc "Oof indeed. Pizza?"
            show cas neutral
            cas "Pizza sounds good."
            scene black with Dissolve(1)
            # TODO: flesh this out with MC getting some pizza and thinking about signs casper was ace or smtg
            "I drove out to get us a pizza, then came back."
            jump dang_im_ace

        label sit_with_cas:
            scene black with Dissolve(1)
            "I sat beside Casper as he read articles by and about ace folks."
            "I could see the gears turning in his head, but I stayed quiet and waited for him to be ready to talk again."
            # TODO: flesh this out with Casper reading stuff and quietly talking
            "After an hour or so, I hopped up to use the bathroom."
            jump dang_im_ace
    
    label dang_im_ace:
        scene bg bedroom dark:
            zoom 0.7
        with Dissolve(1)
        # play music "audio/EvansFull.ogg" fadein 1 fadeout 1

        show cas blank at right
        show mc neutral at left
        "When I came back into the room, it was dark. Casper must have turned the lights off while I was away."
        "He sat still on the bed, the light from his phone illuminating his face."
        mc "Hey, I'm back."
        show cas smile
        "Casper looked up at me and set his phone next to him."
        cas "Hey."
        mc "How are you feeling?"
        "Cas looked pensive."
        cas "I think I'm a little better. I did a lot of reading and a lot of thinking and..."
        show cas sad smile
        cas "I think you're probably right. Everything I read about asexuality feels like it fits. It feels weird that I never learned about it."
        cas "But it just makes a lot of things make sense and... feel valid, I guess."
        show mc smile
        mc "I'm really glad. I hoped it would."
        # TODO: Maybe add some more deets here?
        show cas sad
        cas "Although... something else happened while you were out of the room."
        show mc sad
        "Uh oh."
        mc "What happened?"
        "Cas hesitated for a long moment before extending his arm and offering his phone to me."
        cas "Taylor texted me. Just read the last few messages."
        "I took the phone and glanced over the messages, sitting down beside Cas as I did."
        phone "I'm so sorry, babe. I should never have said that. You just make me so scared and insecure sometimes. Are we ok? Please please please say yes."
        show cas blank
        "Casper watched me, gauging my reaction."
        menu:
            "I felt..."
            "Angry that he was blaming Casper.":
                show mc angry
                "What kind of apology was that?"
                "The text read like Taylor thought that his yelling at Casper was Casper's fault."
                "It wasn't fair of him to message Casper just a few hours after breaking their relationship off just to get Casper back!"
            "Astonished that he was trying to brush this off.":
                show mc surprised
                "The text was just so weird. It was a backhanded apology, an accusation, and emotional manipulation all in one."
                "How could he have yelled at Casper like that, walked out, and then texted only a few hours later hoping things were fine?"
            "Honestly, I felt kind of bad for him.":
                show mc sad
                "Taylor clearly had a lot of fear around losing Casper, and he was dealing with it in the worse ways."
                "From what Casper had said, Taylor seemed like he really needed help, and I hoped he got it, ideally from a therapist and not a romantic partner."
                "But it absolutely didn't make how he was treating Casper ok, and this text had a manipulative feeling to it that made me very uncomfortable."
        
        cas "Does... does the text feel kind of weird to you too...?"
        show mc blank
        mc "Yeah. It does."
        mc "It feels manipulative, and like he's blaming you for what happened."

        show cas sad
        "Cas gave terse nod."
        cas "I thought so too. I just... didn't know if that was me being defensive."

        menu:
            "\"It's not.\"":
                mc "No, I think that's a really reasonable conclusion to draw from that text."
            "\"You're allowed to be defensive right now.\"":
                mc "Cas, Taylor hurt you really badly tonight. It's ok to be defensive, especially since you're not trying to get back at him. You're just processing."
        
        "Cas sighed heavily."
        cas "I just... don't know where to go from here."
        cas "It would be so, so easy just for me to tell him that everything is ok and try to get things to go back to normal."
        show cas crying
        show mc sad
        "Cas's eyes started to well up again."
        cas "But it's not. It's not ok and I don't think we've been ok for months now."

        menu:
            "Nod.":
                $ hugs = False
                "I bobbed my head and listened attentively."
            "Put your arm around him.":
                $ hugs = True
                "I wrapped my arm around Cas's shoulder and pulled him against my side."
                "He leaned into me and nuzzled into my shoulder."
        
        cas "I... I don't think this is healthy. Not for him and not for me either."
        show cas crying smile
        "Tears were falling from Casper's eyes again, but it was different from before."
        "He felt less panicky and he wasn't blaming himself. He was crying, but he wasn't sobbing or shaking."
        "There was a sense of melancholy resignation to his words."
        "He breathed a few times, slowly, preparing himself."
        cas "I think. That we shouldn't get back together."
        show cas crying
        cas "It hurts so, so bad to say that."
        cas "I love him so much and I don't want this to be how things end."
        cas "But he's getting worse and there's nothing I can do to help him. Not like this."
        show cas sad
        "Casper looked down, ashamed."
        cas "And I don't like the person I've been becoming these past few months. I don't want to be short with my boyfriend, or ghost my best friend, or drop my hobbies and interests."
        "Cas lowered his voice and asked, tentatively."
        cas "Does that make me a bad person? That I can't keep doing this?"

        if hugs:
            "I held Casper tight against me."
        mc "No, of course it doesn't."
        
        cas "Do you think that I'm making the right call?"
        menu:
            "\"I think so.\"":
                show mc neutral
                mc "From everything you've told me tonight... Yeah."
                mc "It doesn't sound like being together with Taylor is good for either of you any more."
            "\"I really don't think that it's my decision.\"":
                show mc sad smile
                mc "I really don't know Taylor that well, and I'm not in your head. I don't have all the details, or all the answers."
                mc "But I can see how much this is hurting you and I trust you to make the right decision for yourself."
                mc "And if you think that letting the relationship end here is the best thing for you, I fully support you."


    "The End"
    return

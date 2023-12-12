define K = Character("Kaleb", color = "#cd3333")

define L = Character("Lyla", color = "#7AC5CD")

define MH = Character("Mr.Hawk", color = "#FF8C00")

define C = Character("Cecilia", color = "#ADFF2F")

define E = Character("Eugene", color = "#66CDAA")

define MW = Character("Mr.Wilson", color = "#FA8072")

image K:
    "kaleb"

image L:
    "lyla"
    
image MH:
    "mrhawk"
image MHS:
    "mrhawksad"

image C:
    "cecilia"

image CB:
    "ceciliablush"

image E:
    "eugene"

image ES:
    "eugenesmile"

image MW:
    "mrwilson"
image MWT:
    "mrwilsontalking"

define M = "Mom"

image neighborhood:
    "neighborhood.jpeg"
    zoom 1.5

image mainBedRoom:
    "mainBedRoom.jpeg"
    zoom 1.5
image kitchen:
    "kitchen.jpeg"
    zoom 1.5
image FrontSchool:
    "FrontSchool.jpeg"
    zoom 1.5
image CrowdedHallway:
    "CrowdedHallway.jpeg"
    zoom 1.5
image Classroom:
    "classroom2.jpg"
    zoom 1.0

image Lunchoom:
    "lunchroom.jpeg"
    zoom 2.64

image ScienceRoom:
    "scienceroom.jpg"
    zoom 2.4

label start:
    scene neighborhood 
    play music "mixkit-feeling-happy-5.mp3"
    $ Y = renpy.input("What's your name?")
    if Y == "":
        $ Y = renpy.input("Come on! Enter a name!")  
    "{i}One early Monday morning...{i}"
    scene mainBedRoom
    with fade
    play music "mixkit-classic-short-alarm-993.wav"
    Y "Ugh..."
    stop music 
    play music "mixkit-feeling-happy-5.mp3"
    Y "Ah... I miss my old school already..."
    Y "Why did we have to move states..."
    Y "What should I wear for today?"
    menu:
        " Preppy Clothing: Blazer, dress shirt, Khaki pants, and boat shoes":
            $ clothes = "Preppy"
            Y "If I'm gonna try for honors, might as well look the part!"
        " Sports Clothing: Pikey Sports tee shirt with shorts and sneakers":
            $ clothes = "Sports"
            Y "Maybe I'll try out for a sport!"
        " Normal Clothing: A Resonance Rockers tee shirt and sweatpants":
            $ clothes = "Casual"
            Y "No one's gonna care right?"
    M "Come on! You'll be late!"
    Y "Coming Mom!"
    scene kitchen
    with fade
    M "Hey there Kiddo!"
    "{i}She notices your outfit{i}"
    M "Great outfit! Ready for your first day [Y]?"
    menu:
        "Yes":
            $ MomC = "Yes"
            Y "I'm excited for a fresh new start!"
        "No":
            $ MomC = "No"
            Y "Not at all!"
    if MomC == "Yes":
        M "Thats the spirit!"
    if MomC == "No":
        M "Well, think about it as a clean slate!"
    "{i}she looks at the time{i}"
    M "Come along! I'll drop you off before you're late!"
    scene neighborhood
    with dissolve
    "After 20 minutes..."
    scene FrontSchool
    with fade
    M "Alright [Y]! Good luck on your first day! Make lots friends kiddo!"
    Y "Ok ok Mom! Bye!"
    "{i}Your mother drives away{i}"
    "{i}You walk to the front doors to start your 4 year journey...{i}"
    scene CrowdedHallway
    with dissolve
    play music "mixkit-big-crowd-talking-loop-364.wav"

    "{i}the hallway is crowded with kids walking around{i}"
    "{i}Mainly including clubs and sports with tables trying to recuite{i}"
    "{i}You think to yourself...{i}"
    Y "{i}I got here pretty early, I should check out some of these clubs.{i}"
    "{i}Who do you visit first?{i}"
    menu:
        "Football":
            $ TableChoice = "Football"
            "{i}You decide to check out the Football teams table first{i}"
        "Honors Society":
            $ TableChoice = "Honors"
            "{i}You decide to check out the Honor Society's table first{i}"
    if TableChoice == "Football":
        "{i}When you head over to the Football team's table, a boy with blonde hair and red eyes puts his hand up, to stop you from visiting their table{i}"
        show K 
        K "I'm gonna stop you right there pipsqueak!"
        K "What do you think you're doing?"
        Y "I just wanted to check out your guy's table-"
        K "Shush peepsqueak!"
        "{i}Kaleb notices your outfit{i}"
        if clothes == "Sports":
            K "Even though you dress like someone who plays... "
            K"You're  still too small to be apart of the football team!"
            "{i}The other members of the football team laugh{i}"
            "{i}You turn to walkaway as they continue to laugh at you...{i}"
            Y "{i}I have time for one more table, wonder who i should visit next...{i}"
        else:
            K "Maybe you could be like a water boy or something!"
            "{i}The other members of the football team laugh{i}"
            "{i}You turn to walkaway as they continue to laugh at you...{i}"
            
    if TableChoice == "Honors":
        "{i}At the Honor Society's table, you see a girl with blue hair, standing there shyly{i}"
        show L
        L "Oh! Hi there!"
        L "I-I'm Lyla!"
        Y "It's [Y]!"
        L "Hi [Y]"
        L "Are- are you interested in joining the Ho- Honor Society?"
        menu:
            "Yes":
                $ Hchoice = "yes"
                Y "I wanted to level up academically!"
            "No":
                $ Hchoice = "no" 
                Y "Just seeing what you guys offer is all!"
        if Hchoice == "yes" and clothes == "Preppy":
            "{i}Lyla notices your outfit{i}"
            L " You certainly look the part!"
        if Hchoice =="yes":
            L "Well, you're in lu-luck then!"
            L "Not many join the Honor Society..."
            L "But the few who do, end up in great colleges!"
            
        if Hchoice == "no":
            L "Well, we offer Honors classes, whi-which sound difficult..."
            L "But are just a little more difficult than regular classes!"
            L "Plus, being in honor classes will look great for colleges!"  
    "{i}You hear the ring of the school bell{i}"
    Y "{i}I wonder who's going to be in my first class...{i}"
        
    scene Classroom
    with fade
    stop music
    play music "sunrise-groove-176565.mp3"
    "{i}You walk into music class and wonder where to sit{i}"
    menu:
        "Front":
            $ SeatChoice = "Front"
        "Middle":
            $ SeatChoice = "Middle"
        "Back":
            $ SeatChoice = "Back"
    if SeatChoice == "Front":
            "{i}you decide to sit in the very front{i}"
    if SeatChoice == "Middle":
            "{i}you decide to sit in the middle to seem impartial{i}"
    if SeatChoice == "Back":
        "{i}to avoid detection, you sit in the back{i}"
    "{i}8 minutes after the bell rang{i}"
    "{i}Your music teacher comes in late...{i}"
    show MHS 
    with moveinright
    " Sorry sorry, I'm late!"
    "It's my first day!"
    "{i}he seems a little nervous...{i}"
    "{i}offer some encouragment?{i}"
    menu:
        "Yes":
            $ echoice = "yes"
        "No":
            $ echoice = "no"
    if echoice == "yes":
        "{i}you give a small smile and a thumbs up{i}"
        "{i}he notices your encouragement and takes a deep breath in{i}"
    if clothes == "Casual":
        "{i}He also notices your shirt and gives a small smile{i}"
        "{i}you think to yourself...{i}"
        Y "{i}Why does he look so familiar?{i}"
            
    if echoice == "no":
        "{i}he stands there a bit to collect himself and takes a deep breath in to adress the class. {i}" 
    show MH  
    "Hello everyone!"
    "{i}it's silent...{i}" 
    MH "I am your music teacher... Mr.Hawk!"
    MH "I may be young..."
    MH "But i know a lot about music!"
    MH "So, everyone excited to learn about music?"
    "{i}his question is accompanied by several weak agreements{i}"
    MH "Well.. ok then!"
    MH "Today we are going to learn about the piano!"
    "{i}a student raises his hand{i}"
    MH "Yes? You in the back?"
    "Aren't you in that band called The Resonance Rockers?"
    MH "Well.. I {b}WAS{b} a part of The Resonance Rockers but that was a long time ago!"
    MH "I've turned to a new life teaching what I had to you guys!"
    hide MH
    show MHS 
    "{i}the students errupt with questions, asking more about Mr.Hawk's past celebrity life{i}" 
    "{i}Do you wanna know more about Mr.Hawks or do you want to continue with the class?{i}"
    menu:
        "Ask more about Mr.Hawks?":
            $ MHChoice = "more"
        "Continue on with class?":
            $ MHChoice = "cont"

    if MHChoice == "more":
        "{i}you raise your hand{i}"
        menu:
            "Why did you leave the spotlight?":
                $ MHReason = "change"
            "Do you miss the spotlight?":
                $ MHReason = "miss"
            "Do students recognize you?":
                $ MHReason = "rec"
        if MHReason == "change":
            MH "The celebrity life wasn't for me"
            MH "Sure, it has it's perks but once i reached my dream..."
            MH "It wasn't what I was expecting"
            MH "But now I teach so I can pass my knowledge onto the younger generation!"
        if MHReason == "miss":
            MH "Well, there are moments I miss..."
            MH "The crowds screaming out your name..."
            MH "Playing with your bandmates on stage..."
            MH "It's stuff like that I miss but, it was time for a change!"
        if MHReason == "rec":
            MH "Not many students recognize me but most of the teachers do"
            MH "I had to give out some autographs this morning to some of the teachers..."
    "{i}After many students bombard him with questions...{i}"
    "{i}the bell rings{i}"
    MH "Welp... it seems like that's all of our time for today!"
    MH "I hope we can learn more about music and not about me next time!"
    stop music 
    scene CrowdedHallway
    with dissolve
    play music "mixkit-big-crowd-talking-loop-364.wav"
    "{i}the bell rings and now it's onto lunch!{i}"
    "{i}you start to walk to lunchroom as everyone starts to rush{i}"
    scene Lunchoom
    with fade
    "{i}you walk up to the lunchline and await your turn{i}"
    "{i}once you get to the lunch lady she asks you{i}"
    "What'll you be havin kid?"
    menu:
        "Mac and Cheese with a Garlic Bread Stick":
            $ FChoice = "MC"
        "Chicken Sandwich with tater tots":
            $ FChoice = "CS"
        "Salad Bowl":
            $ FChoice = "SB"
    "{i}You walk towards the tables when you notice most tables are taken{i}"
    "{i}But there are two tables that have empty seats with them{i}"
    "{i}Which table do you sit at?{i}"
    menu:
        "Table 1":
            $ TabChoice = "Table 1"
        "Table 2":
            $ TabChoice = "Table 2"

    if TabChoice == "Table 1":
        "{i}you head over to table 1{i}"
        "{i}you see a boy with a little piece of paper"
        Y "Hey, is this seat taken?"
        show E
        "Not at all! Take a seat!"
        "{i}you sit down{i}"
        hide E 
        show ES 
        E "Eugene Smith is the name!"
        E "I've heard whispers from the Paladins that a new adventurer would be joining us this school year! "
        E "That would be you correct?"
        Y "Yeah, my name is [Y]!"
        Y "Wait.. Paladins?"
        E "Yeah! As in the greatest story telling game of all time?"
        "{i}you shake your head in confusion{i}"
        E "I'm talking about Wizards and Wyverns my friend!"
        E "Not to roll a natural 20 on my own performance check, but.."
        "{i}He smirks{i}"
        E "I happen to be the Campaign Conductor at DreamScape's Wizards and Wyverns Club!"
        E "It's a new school year so it's a new campaign!"
        E "You should join us on our journey!"
        menu:
            "Tell me more!":
                $ EChoice = "Tell"
            "Not interested sorry...":
                $ EChoice = "no"
        if EChoice == "Tell":
            E "Wizards and Wyverns is a fantastical tabletop role-playing game set in a magical realm where players create characters, embark on epic quests, and face mythical challenges!"
            Y "Oh ok so it's just like playing pretend!"
            E "Not quite my naive friend!"
            E "We are simply not {i}playing pretend{i}!"
            E "The characters we make and play as, are a reflection of who we are!"

        if EChoice == "no":
            E "No worries [Y]!"
            E "Our campaigns can get intense for the Fresh-faced Adventurer!"
            E "Feel free to come by and watch our campaign anytime [Y]!"
        "{i}you and eugene continue to chat until the bell rings{i}"
        E "Well, it seems like our time together is up [Y]!"
        E "Farewell, fellow adventurer! May your next quest be filled with loot and legendary encounters!"
        "{i}Eugene gathers his belongings and stands to leave{i}"
        hide ES
        with moveoutleft


        

    if TabChoice == "Table 2":
        "{i}you head over to table 2{i}"
        show C
        "{i}You see this girl sitting by herself, sketching in a little notebook{i}"
        Y "Hey, this seat taken?"
        "Oh! Uh no, it's not.."
        "{i}You sit down{i}"
        "{i}You get a little glimpse of her notebook{i}"
        menu:
            "Compliment her drawings":
                $ CChoice = "Compliment"
            "Ignore":
                $ CChoice = "Ignore"
        if CChoice == "Compliment":
            Y "Woah! Did you draw those?"
            "Um.. yeah?"
            Y "Those look so good!"
            hide C 
            show CB
            "{i}she blushes{i}"
            "Oh! They're nothing really.."
            Y "Oh come on! You're really talented!"
            "Thanks.."
            "{i}after a couple seconds of silence..{i}"
            
        if CChoice == "Ignore":
            "{i}the silence was loud{i}"
            "{i}until she says something{i}"
        C "Cecilia..."
        Y "What?"
        C "My name is Cecilia"
        Y "Oh! My name is [Y]!"
        C "Nice to meet you [Y].."
        C "You're new around here right? I haven't seen you before"
        Y "Yeah, I moved here a week ago!"
        C "Moving is tough..."
        if CChoice == "Compliment":
            C "I get the feeling though.."
            C "You feel like you're alone in a new environment..."
        if CChoice == "Ignore":
            "{i}She was about to say something but stopped herself{i}"
        Y "Yeah, you can say that again..."
        "{i}for the entire lunch period, you sit with Cecilia and chat with her{i}"
        "{i}the bell rings{i}"
        C "Well it was nice meeting you [Y]."
        C "I'll see you around.."
        hide CB 
        with moveoutright
        "{i}she puts on her headphones and stands up to leave{i}" 
    "{i}you also stand up to leave{i}"
    scene CrowdedHallway
    with fade 
    "{i}up next is your science class{i}"
    stop music
    scene ScienceRoom
    with fade
    play music "science-documentary-169621.mp3"
    "{i}you walk in and take your seat at one of the tables, waiting for your teacher to speak{i}"
    show MWT 
    with moveinleft
    "{i}The teacher talks in a low, tired voice{i}"
    "Hello class..."
    "Welcome to Chemistry.."
    MW "My name is Mr. Wilson.. but you can call me whatever.."
    MW "I don't really care."
    "{i}a student raises his hand{i}"
    MW "Yes.. I have Heterochromia.."
    "{i}the student puts his hand down slowly{i}"
    MW "Please find a student to become your lab partner.."
    MW "The student you pick will be your lab partner for the year.." 
    MW "I will wait.."
    "{i}He sits down at his desk and plays on his phone{i}"
    hide MWT
    with moveoutleft
    "{i}You look around to try to find someone{i}"
    "{i}suddenly someone comes up to you{i}"
    show L
    with moveinright
    if TableChoice == "Honors":
        L "[Y] right?"
        Y "Lyla!"
        Y "What are you doing here? This isn't an honors class!"
        L "Even though I'm in Honors, I'm only a Freshman so I still have to take Chemistry to move on.."
        Y "Ah, that does make sense!"
        L "Can we be lab partners?"
        L "I don't know anyone else here..."
        Y "Of course Lyla!"
        "{i}Lyla exhales{i}"
        L "Whew... I was worried I was going to have to be social..."
    else:
        "Um.. hey.."
        "Could we be lab partners?"
        Y "Oh uh, sure!"
        L "L-Lyla is my name, nice to meet you"
        Y "Nice to meet you too Lyla"
        Y "[Y] is my name!"
        L "Nice to meet you [Y]"

    hide L
    show MW
    with moveinleft 
    hide MW
    show MWT
    MW "Has everyone gotten a lab partner yet?"
    "{i}the class nods their head{i}"
    MW "Alright time to start the lesson"
    MW "Everyone take your seats.."
    "{i}as everyone takes their seats, Mr. Wilson draws a water molecule"
    MW "We'll start with the basics and work out way up."
    MW "When you know the answer, raise your hand and tell me your name."
    MW "How many Hydrogen atoms are in a Water molecule?"
    "{i}Do you raise your hand?{i}"
    menu:
        "yes":
            $ RH = "y"
        "no":
            $ RH = "n"
    if RH == "y":
        MW "Yes?"
        menu:
            "[Y], Just one":
                $ MWChoice = "1"
            "[Y], There's two":
                $ MWChoice = "2"
            "[Y], There's 3":
                $ MWChoice = "3"
        if MWChoice == "2":
            MW "Yes, that's correct [Y]"
            MW "That's what the 2 in H2O is" 
        else:
            "{i}a couple students chuckle{i}"
            MW "Well, that's the wrong answer.."
            "{i}Lyla raises her hand{i}"
            L "Lyla, There's 2"
            MW "Yes, that's correct"
            MW "That's what the 2 in H2O is"
    if RH == "n":
        MW "Well? Anyone?"
        "{i}Lyla raises her hand{i}"
        L "Lyla,Th-There's 2"
        MW "Yes, that's correct"
        MW "That's what the 2 in H2O is"
    MW "Onto the next."
    MW "Identify the gas commonly known as laughing gas."
    "{i}Do you raise your hand?{i}"
    if RH == "y":
        menu:
            "yes":
                $ RH2 = "y"
            "no":
                $ RH2 = "n"
        if RH2 == "y":
            MW "Yes [Y]? "
            menu:
                "Nitrous Oxide":
                    $ MWChoice2 = "NO"
                "Helium":
                    $ MWChoice2 = "H"
                "Methane":
                    $ MWChoice2 = "M"

            if MWChoice2 == "NO":
                MW "Correct once again [Y]."
                MW "It's normally used with procedures like wisdom teeth removal."
            else:
                MW "That is incorrect [Y]"
                MW "Anyone else like to answer?"
                L "Lyla, N-Nitrous Oxide?"
                MW "Correct Lyla."
    if RH == "n":
        menu:
            "yes":
                $ RH2 = "y"
            "no":
                $ RH2 = "n"
        if RH2 == "y":
            MW "Yes?"
            menu:
                "[Y],Nitrous Oxide":
                    $ MWChoice2 = "NO"
                "[Y],Helium":
                    $ MWChoice2 = "H"
                "[Y],Methane":
                    $ MWChoice2 = "M"

            if MWChoice2 == "NO":
                MW "Correct [Y]."
                MW "It's normally used with procedures like wisdom teeth removal."
            else:
                MW "That is incorrect [Y]"
                MW "Anyone else like to answer?"
                L "N-Nitrous Oxide?"
                MW "Correct Lyla."
                MW "It's normally used with procedures like wisdom teeth removal."
    if RH2 == "n":
        MW "Anyone like to answer?"
        L "N- Nitrous Oxide?"
        MW "Correct Lyla."
        MW "It's normally used with procedures like wisdom teeth removal."
    "{i}After many questions..."
    "{i}the bell rings{i}"
    MW "Alright.. that's all the time we have for today."
    MW "I'll see you guys tomorrow."
    "{i}Everyone starts to pack up and leave, including you{i}"
    scene CrowdedHallway
    with fade
    stop music
    play music "mixkit-big-crowd-talking-loop-364.wav"
    "{i}After two more classes, the final bell rings{i}"
    "{i}Time to go home!{i}"
    scene FrontSchool
    with fade
    "{i}As kids are walking out to come home, you're waiting for your mom to pick you up{i}"
    "{i} you look to your right and see someone familiar{i}"
    show C
    with moveinright
    C "[Y]!"
    Y "Cecilia!"
    Y "Are you also waiting for someone to pick you up?"
    C "Yeah, my dad is coming to pick me up."
    C "So, how was you're first day at Dreamscape High?"
    menu: 
        "It was great!":
            $ SChoice = "g"
        "It was terrible!":
            $ SChoice = "t"
    if SChoice == "g":
        Y "I met a lot of different people!"
        Y "Even if some were a little weird..."
    if SChoice == "t":
        Y "I already miss my old school..."
    C "Well. you'll get used to it [Y] don't worry."
    "{i}suddenly, a car pulls up{i}"
    play audio "car-horn-6408.mp3"
    M "Hey Kiddo!"
    M "Ooo- Who is this? A new friend?"
    C "My name is Cecilia."
    M "Well, very nice to meet you Cecilia!"
    M "I hope you can come over some time!"
    Y "Mom!"
    C "It's fine. It's what moms do."
    M "Well get in kiddo, we got some grocery shopping to do!"
    "{i}You turn to Cecilia{i}"
    Y "I'll see you tomorrow?"
    C "See you tomorrow [Y]."
    "{i}you get in the car and drive off{i}"
    scene neighborhood
    with dissolve
    stop music
    play music "mixkit-feeling-happy-5.mp3"
    "Well that's it!"
    "I hope you enjoyed Dreamscape High!"
    "I actually had a lot of fun doing this!"
    "I might continue to add more into this and expand into this during my college years!"
    "Have a great day!"


    pause
return
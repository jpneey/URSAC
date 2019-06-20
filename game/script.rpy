init:
    #variable declaration on 'initialization' / init blocks are executed before anything else <3
    $ chi = 0
    $ coba = 0
    $ osds = 0
    $ shs = 0
    $ canteen = 0
    $ coe = 0
    $ coeng = 0
    $ tree = 0
    $ flag = 0
    $ court = 0
    $ end_na = 0
    $ map_visible = False
    
init:
    $ a = 0
    $ b = 0
    $ c = 0
    
# text displayables on custom coordinates
image talk = ParameterizedText(size=35,xalign=0.5, yalign=0.3 , who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ])        
image talks = ParameterizedText(xalign=0.7, yalign=0.5)
image tx = ParameterizedText(size=35,xalign=0.6, yalign=0.4 , who_outlines=[ (1, "#000000") ], what_outlines=[ (1, "#000000") ]) 


#Character side images and name on top of textbox
image side lynn = "lyns.png"
image side jpp = "jps.png"
image side studs = "students.png"
image side gur = "guards.png" 
image side narr = "narrators.png"
image side drr = "drews.png"
image side uss = "uss.png"
image side jarr = "joshs.png"
#character string declarations
define j = Character(None, image="jarr")
define g = Character(None, image="gur")
define narrator = Character(None , image="narr") 
define d = Character(None, image="drr")
define s = Character(None, image="studs")
define jp = Character(None, image="jpp")
define k = Character(None, image="lynn")
#splashscreen block
label splashscreen:

    scene white
    play sound "audio/pito.wav"
    show splash2 at poppu
    $ renpy.pause(1.0, hard = True)
    hide splash2 with dissolve
    $ renpy.pause(0.3, hard = True)
    show spscreen at poppu
    $ renpy.pause(1.5, hard = True)
    hide spscreen 
    scene x_ca
   # play sound "audio/hoverb.mp3"
    $ renpy.pause(0.5)
    play music "audio/turbotornado.mp3"
    show splash_act_a
    $ renpy.pause(0.5, hard = True)
    return
#custom defined images with 'ATL' transofrmation animation    
image bg outs:
    "bg shed3.png" with dissolve
    2
    "bg coba.png" with dissolve
    2
    "bg out.png" with dissolve
    
image menu_a:
    "bg coba.png" with dissolve
    1.5
    "bg shed3.png" with dissolve
    1.5
    "bg eng.png" with dissolve
    1.5
    repeat
image urs:
    "bg coba.png" with dissolve
    1.5
    "bg shed3.png" with dissolve
    1.5
    "bg chi.png" with dissolve
    1.5
    "bg cob_hall.png" with dissolve
    1.5
    #"bg cob_entrance.png" with dissolve
    #.5
    #"bg cob1.png" with dissolve
    #.5
    #"bg cob2.png" with dissolve
    #.5
    "bg facculty.png" with dissolve
    1.5
    "black.png" with dissolve
image 15_whut:
    "whut.png"
    time 1.2
    "transparent.png" with dissolve
    
image spscreen:
    "splash.png" 
    0.5
    "splash1.png" with dissolve
    1.0
    #"splash2.png" with dissolve
    #0.5


#Main body of the in-game scripts and dialouge    
    
label start:
    play sound "audio/school_bell.wav"
    play music "audio/Happyplace.mp3"

    define u = Character(None, image="uss")
    scene bg outs at zoo
    show narrators
    with dissolve
    "The sun was at its peak as different students\n of {i}URSAC{/i}{size=-5} (UNIVERSITY OF RIZAL SYSTEM ANTIPOLO CAMPUS){/size}\n headed out to eat their lunch"
    "However , Our hero -"
    play sound "audio/twinkle.wav"
    show andrew_intro at ups
    show wow at rights1
    show drew at rights_x1
    extend "\nAndrew ,"
    show wow at rights1_back behind drew
    hide wow with dissolve 
    show andrew_intro2 at ups
    extend "\ A freshly transferred student\nalong with his aesthetically pleasing personality -"
    play sound "audio/eek.wav"
    show drew_meme2 at rights_x
    show emoji_lol_a at emoji_roll behind drew
    show emoji_lol_b at emoji_roll_b behind drew
    "-was entrusted by his Mom\n to deliver a special parcel for his long lost twin ."
    #hide emoji_roll_a
    #hide emoji_roll_b
    #with dissolve
    play sound "audio/romantic.wav"
    show andrew_intro at ups_back 
    show andrew_intro2 at ups_back2
   # show bento at leftss behind drew
    show aww_yiss at aww_yiss behind drew
    "That parcel is a delicious lunch made with passion\nand love ~"
    hide andrew_intro
    hide andrew_intro2
    hide aww_yiss
    with dissolve
    scene bg out_var1 at zoo1
    with dissolve
    play sound "audio/zoom.mp3"
    "But - Andrew , doesn't know where to find his long lost twin ! "
    #show whut at whuts
    #with dissolve
    "This may be the first time of them seeing each other\nafter fifteen years ! " 
    play sound "audio/tokok.wav"
    "All clue he has as of now is that : his twin can be found inside the campus ."
    scene urs at zoo
    with dissolve
    #$ renpy.pause(3.0)
    
    show narrators with dissolve
    "Let's help Andrew "
    extend ", as we uncover the hidden beauty\nof URS ANTIPOLO ! "
    extend "{i}Tehe~{/i}"
    scene bg out at zoo
    with dissolve
    "Andrew, filled with uncertainty "
    extend ", was about to take his first step\non a{i}DO or DIE{/i} quest!"
    hide narrators
    show drews
    show drew 
    show drew_close at rights behind drew
    with dissolve
    d "Hey you !  ~"
    d "The one reading this !"
    show drew_close at rights_back
    show drew at rights
    d "Are you willing to be my companion on this \nessential task ?"
    hide drews
label aba:
    menu:
        "Yes ! ":
            show drews
            play sound "audio/romantic.wav"
            show drew_close_blush at aww_yiss
            show drew at rights
            d "Alright !"
            d "That's what I wanted to hear ! "
        "No !":
            show drew at rights
            d "Oh you mean yes ?"
            jump aba
label pro:
    hide drews
    show narrators
    "And without further ado , Andrew's will to \nfight was re-established because of\nyour aid !"
    "Andrew , jumping with joy , rushed his way inside the university ."
    hide drew with dissolve
    "Oh no! You were getting left out! "
    "Pick up your pace and try not to leave \nandrew wandering the university alone ! "
    ". . ."
label pro1:
menu:
    "Are you ready to follow Andrew ?"
    "OFCOURSE !":
        jump pro2
    "NOPE.":
        "Do you mean yes?"
        jump pro1
    #extend " you decided to set your foot inside"
label pro2:
    scene bg entrance at zoo
    with dissolve
    show narrators
    "{i}And finally , you decided to enter the university{/i} ."
    "A vivid environment with grass swaying along the hum\nof the wind filled your gaze ."
    "All is well ."
    "Everything seems peaceful ."
    "but then you heard a somewhat familiar sound fom behind ."
    stop music fadeout(2.0)
    play sound "audio/pito.wav"
    "All sound turned flat ."
    "suddenly, all you can hear was your heart -\nBeating the tempo of fear ."
    scene black with dissolve
    show narrators
    "You turned around . slowly as you could ."
    scene bg guard at zoo
    with vpunch
    show narrators
    play music "audio/trash.mp3"
    play sound "audio/guwah.wav"
    "Oh no! A Narrator look-like Guard suddenly appeared !"
    show stoppu at rights
    show emoji_lol_a at emoji_roll behind drew
    show emoji_lol_b at emoji_roll_b behind drew
    show stoppu at aww_yiss
    hide narrators
    show guards
    play sound "audio/frog.wav"
    g "HALT !"
    g "May I ask your business here?"
    hide guards
    show narrators
    "Oh no ! "
    "I forgot to tell you that \nsecurity here requires\nstudent identification cards upon entry !"
    hide narrators
    show guards
    g "May I ask where your {i}I.D.{/i} is ?"
    hide guards
    show uss
    u "err ... "
    hide uss
    show guards
    
menu:
   
    g "May I ask where your {i}I.D.{/i} is ?"
    " BEND THE TRUTH ":
        hide guards
        show uss
        u "Err . . ."
        u "H-how d-dare you talk to me like that ! "
        u "I-Im the new Guard ! "
        stop music 
        play sound "audio/dooom.wav"
        show shock2 with hpunch
        hide uss
        show guards
        g "eh ? ."
        g "Do you think I'm gonna buy that excuse ?"
        scene black with dissolve
        show guards 
        g "Come on now. You know lying was never an option "
        play sound "audio/ost1.mp3"
        scene black with dissolve
        show text "{color=#FFF}The following event dealt  heavy damage on your morale{/color}" with dissolve
        $ renpy.pause()
        show text "{color=#FFF}Unfortunately , you lost your chance to enter the school again that day{/color}" with dissolve
        $ renpy.pause()
        show text "{color=#FFF}Who knows? Maybe if you were honest , You and Andrew will be able to accomplish the task{/color}" with dissolve
        $ renpy.pause()
        show text "{color=#FFF}:: BAD ENDING ::\n'{i}Honesty is the best Policy{/i}'{/color}" with dissolve
        $ renpy.pause()
        stop sound fadeout(2.0)
        return
    " BE HONEST ":
        hide guards
        show uss
        u "Umm .. Actually I'm not a student here .. "
    " TELL A LIE FABULOUSLY ~ ":
        hide guards
        show uss
        u "Err . . ."
        u "H-how d-dare you talk to me like that ! "
        u "I-Im the new Campus Director ! "
        stop music 
        play sound "audio/dooom.wav"
        show shock2 with hpunch
        hide uss
        show guards
        g "eh ? ."
        g "Do you think I'm gonna buy that excuse ?"
        scene black with dissolve
        show guards 
        g "Come on now. You know lying was never an option "
        play sound "audio/ost1.mp3"
        scene black with dissolve
        show text "{color=#FFF}The following event dealt  heavy damage on your morale{/color}" with dissolve
        $ renpy.pause()
        show text "{color=#FFF}Unfortunately , you lost your chance to enter the school again that day{/color}" with dissolve
        $ renpy.pause()
        show text "{color=#FFF}Who knows? Maybe if you were honest , You and Andrew will be able to accomplish the task{/color}" with dissolve
        $ renpy.pause()
        show text "{color=#FFF}:: BAD ENDING ::\n'{i}Honesty is the best Policy{/i}'{/color}" with dissolve
        $ renpy.pause()
        stop sound fadeout(2.0) 
        return
label chap1_b:
    hide uss
    show guards
    g "Oh! Are you here to inquire ?"
    stop music
    play sound "audio/twinkle.wav"
    show starstruck with vpunch
    hide guards
    show uss
    u "well .. sort of .."
    play music "audio/cartoon.mp3"
    hide uss
    show guards
    g "Oh! My bad "
    extend "Well.. \nEnjoy your visit !"
    scene bg entrance at zoo
    show narrators
    with dissolve
    "And by just telling the truth ,\nYou managed to slip your way inside \nthe campus"
    show drew at rights
    play sound "audio/twitch.wav"
    hide narrators
    show drews
    d "Heyya !"
    hide drew
    show drew_a at rights
    play sound "audio/twitch.wav"
    with dissolve
    d "What took you so long ?"
    hide drews
    show uss
    u "err , the guard asked me some questions. {i}tehe~{/i}" 
    u "Well, we're suppose to deliver your twin's lunch right ?"
    u "err .. Do you have a picture or some sort that may\nhelp us find her quickly ?"
    hide uss
    show drews
    d "hmm ... "
    hide drew_a
    show drew at rights
    play sound "audio/twitch.wav"
    with dissolve
    d "Oh Yeah! I got this picture on my phone!"
    d "but .. Its kinda .. blurry . ha-ha"
    show phone at rights
    play sound "audio/point.wav"
    show taka at aww_yiss_var2 behind drew
    show emoji_lol_a at emoji_roll behind drew
    show emoji_lol_b at emoji_roll_b behind drew
    play sound "audio/eek.wav"
    hide drews
    show uss
    u "(Great.)"
    hide phone with dissolve
    hide uss
    show drews
    d "Well , That is all I have . {i}hehe{/i}"
    hide drews
    show narrators
    "The actual problem starts here ~"
    "All you have is a blurred picture as a clue"
    "The glowing hope of success\nthat once soared up on your sky slowly turned faint"
    "You were about to lose hope but suddenly -"
    hide drew
    show emoji_lol_a at emoji_roll behind drew
    show emoji_lol_b at emoji_roll_b behind drew
    play sound "audio/eek.wav"
    #show drew_a at rights
    show josh at rights
    with dissolve
    "Another Fresh and young looking student appeared ! "
    play sound "audio/twinkle.wav"
    show josh_intro at ups behind josh
    show wow at rights1 behind josh
    #show josh at rights_x1
    extend " ~ hehez"
    hide wow behind josh
    show wow at rights1_back behind josh
    show josh_intro2 at ups behind josh
    "It is Joshua , A proud student of the said University"
    play sound "audio/twitch.wav"
    show josh_intro at ups_back 
    show josh_intro2 at ups_back2
    show aww_yiss at aww_yiss behind josh
    hide narrators
    show joshs
    j "' Heyya ! You guys looked like in-need of some help '"
    play sound "audio/romantic.wav"
    show emoji_kiss_a at emoji_roll behind drew
    show emoji_kiss_b at emoji_roll_b behind drew
    show josh at rights_center 
    show drew_a at rights
    with dissolve
    j "'Can I help you ? '"
    hide joshs
    show drews
    d "Oh H-hi ! "
    d "Actually we're in a pinch right now .. "
    hide drews
    show joshs
    j "'Well , I would like to help if I can ..'"
    hide joshs
    show drews
    play sound "audio/romantic.wav"
    show emoji_kiss_a at emoji_roll behind drew
    show emoji_kiss_b at emoji_roll_b behind drew
    show drew_close_blush at aww_yiss
    d "Oh ~ "
    extend "  T-thanks ~ "
    hide josh 
    show drew_a at whisper
    with dissolve
    hide drews
    show narrators
    "{i}Andrew moved closer and whispered on your ears {/i}"
    hide narrators
    show drews
    d "(That's what I like here !)"
    d "(Every student here is helpful)"
    d "(What do you think ? )"
    d "(Should we accept his offer ?)"
menu:
    d "...."
    "SURE !":
        d "tehe~"
    "NOPE !":
        d "(A-are you sure ?)"
        d "(He seems nice .. )"
label chap1_c:
    hide drews
    show uss
    u "Well , Maybe he could {i}ACTUALLY{/i} help us ..'"
    hide uss
    show drews
    d "Haha Yey!"
    hide drew_a
    show drew at rights
    show josh at center
    with dissolve
    d "We would gladly accept your help Josh !" 
    hide drews
    show josh
    show aww_yiss at aww_yiss
    j "What can I do for you ?"
    hide joshs
    show drews
    d "I'm looking for my twin .. I'm new here so.. "
    hide drews
    show joshs
    j "Okay , I get it "
    j "Well follow me !\nMaybe I can help you navigate\nour University !"
    scene bg ursmap at zoo
    show joshs
    show josh at rights
    with dissolve
    j "Here's the map of our university !"
    extend "\nC'mere and take a closer look ."
    $ map_visible = True
    scene map_tutorial with dissolve
    $ renpy.pause()
    scene map_ground with dissolve
    $ renpy.pause(.1)
    call screen urs_map
    
    
#init:
    #chi = 0
    #coba = 0
    #osds = 0
    #shs = 0
    #canteen = 0
    #coe = 0
    #coeng = 0
    #tree = 0
    #flag = 0
    #court = 0    
label Chi:
    
    stop music fadeout(4.0)
    
    $ chi = 1
    $ end_na += 1
    scene chi_1 at zoo
    show narrators
    show screen umb
    play sound "audio/romantic.wav"
    "After walking for a while .."
    play music "audio/Funday.mp3"
    extend "\nYou start to look\naround the 'College of Hospitality Industries' area"
    hide narrators
    show josh at lefts
    show joshs
    with dissolve
    j "Welcome to 'CHI' !"
    show drew_a at rights
    hide joshs
    show drews
    d "CHI ? "
    hide drews
    show joshs
    j "Yeah , This is the College of {i}Hospitality Industry{/i}"
    extend "\n~The cleaniest area on our campus ! {i}hihi{/i}"
    j "Students here can cook delicous stuffs !"
    show food at aww_yiss behind drew_a #behind josh
    hide joshs
    show drews
    d "W-woah !"
    extend "\nI-is it for freee ?! " with vpunch
    show emoji_lol_a at emoji_roll #behind drew
    show emoji_lol_b at emoji_roll_b #behind drew
    play sound "audio/eek.wav"
    hide drews
    show joshs
    j "Well , Sometimes they offer free taste services"
    extend "\nAnyway , we should start looking for your twin now . "
    scene chi_2 at zoo
    show narrators
    with dissolve
    "With occasional stops , You , Joshua and Andrew\nventured the 'CHI' area deeper"
    scene chi_4 at zoo
    show drew_a at lefts
    show drews
    with dissolve
    d "What's this room ? "
    show josh at rights
    hide drews
    show joshs
    j "..this ?"
    show josh_a at right
    with dissolve
    j "This is the school's Food Laboratory "
    hide josh
    scene bg foodlab 
    show josh at right
    with dissolve
    j "You can say that this is one of the\nmost important area around here."
    with dissolve
    show josh_a at right
    with dissolve
    
    j "This is also where they prepare delicous foods\nfor events held inside the campus"
    show drew_a at lefts
    hide joshs
    show drews
    d "Oh - This place looks neat "
    scene chi_2 at zoo
    show josh at lefts
    show drew_a at rights
    show drews
    with dissolve
    d "So .. "
    extend  "\nIt looks like my twin ; Keulyn , is not here"
    play sound "audio/guwah.wav"
    show jpe_g at left_shake
    with vpunch
    hide drews
    show students
    s "DID SOMEONE SAY KEULYN ?! "
    hide students
    show drews
    d "Err.. "
    extend ".. Do you know her ? "
    d "We're looking for her .. "
    hide drews
    show students
    s "Actually.."
    extend ".. no . "
    show emoji_lol_a at emoji_roll #behind drew
    show emoji_lol_b at emoji_roll_b #behind drew
    play sound "audio/eek.wav"
    s "I'm just a random stranger that\nspreads love around the campus"
    s "Bye ! {i}Hakhak{/i} "
    hide students
    hide jpe_g 
    show drews
    with dissolve
    d " ... "
    d "What did just happened ?"
    hide drews
    show joshs
    j "err.. haha Forget that ."
    j "Let's focus on finding your twin "
    stop music fadeout(2.0)
    j "Let's check the school map again !"
    
    play music "audio/Cartoon.mp3"
    scene map_ground with dissolve
    $ renpy.pause(.1)
    call screen urs_map
    
    
    
label Coba:
    $ coba = 1
    $ end_na += 1
    show screen umb
    scene coba_1 at zoo
    play sound "audio/romantic.wav"
    show josh at right
    show joshs
    with dissolve
    j "The College of Business ~"
    hide josh
    show josh_a at right
    with dissolve
    j "Home of aspiring Businessmen and women~"
    scene coba_2 at zoo
    show josh at right
    show joshs
    with dissolve
    j "I feel like we can find your twin here~"
    show drew_a at lefts
    hide joshs
    show drews
    with dissolve
    d "Oh ? Why ?"
    j "Well , because many things can be found here ~"
    #show josh at center 
    show cobs at left_shake behind josh 
    with dissolve
    j "such as the Computer laboratories , The Registrar ,\nThe MIS , The Dean's office\nAnd many more !"
    j "Maybe that's the reason why\nthis building is called \"{i}The Admin Building{/i}\""
    scene coba_3 at zoo
    show drew_josh at left_shake
    show drews
    d "Well .. I hope I can find Keulyn here .."
    show jp_intro at ups behind drew_josh
    #show wow at lefts
    #show jpe at rights_x1
    show jps
    jp"\nDid you say Keulyn ?"
    hide wow 
    show jp_intro2 at ups
    hide jps
    show narrators
    "He is JP , One of Keulyn's classmate ~"
    show jpe at lefts
    hide jp_intro #at ups_back
    hide jp_intro2 #at ups_back2
    hide narrators
    show drews
    d "D-do you know her ? "
    hide drews
    show jps
    show phone2 at ups behind drew_josh
    jp "Is this 'her' by any chance ?"
    hide jps
    show drews
    d "Y-yes !" with hpunch
    d "I'm here to deliver her lunch !"
    d "WHY DO YOU HAVE HER PICTURE ON YOUR PHONE ?!" with vpunch
    hide drews
    hide phone2
    show jps
    with dissolve
    jp "Well , "
    extend "\nOur group was planning to develop a {i}Visual Novel{/i}"
    extend "\nAnd she's gonna be one of our main characters ~"
    jp "So yeah .. I've been editing their pictures .. "
    hide jps
    show joshs
    j "{i}fishy~{/i}"
    hide joshs
    show jps
    jp "N-no its true ! "
    extend " Here's our {i}playable beta{/i} !"
    show meni at ups
    hide jps
    show narrators
    "AN APP WITHIN AN APP ?! " with hpunch
    hide narrators
    show drews
    hide meni with dissolve
    d "Okay I get it ! "
    d "Can you please tell where can I find her ?"
    hide drews
    show jps
    jp "Oh ~"
    jp "She just left ~"
    jp "She said that she is gonna look for her lunch~ "
    hide jps
    show drews
    d "Oh thanks !"
    d "Come on Josh ! We might still be able to catch her up !"
    d "Thanks Jp ! "
    scene map_ground with dissolve
    $ renpy.pause(.1)
    call screen urs_map
    
    
    
    
label Osds:
    stop music fadeout(2.0)
    
    $ osds = 1
    $ end_na += 1
    show screen umb
    scene osd_1 at zoo
    with dissolve
    $ renpy.pause(.5)
    scene osd_2 at zoo
    show drews
    show drew_josh at left_shake
    with dissolve
    d "What is this place ?"
    play music "audio/Curious.mp3"
    hide drews
    show joshs
    j "This is the {i}OSDS{/i}\n\"Office of Student Development Services\""
    j "They are the one who implements hair-cut policies\nI.D validation , Scholarships and other rules\nthat we must follow"
    scene osd_4 at zoo
    show drew_josh at left_shake
    show joshs
    with dissolve
    j "Around the back , The guidance councilor can be found"
    j "In times of trouble\nthey're the one who will accompany you"
    hide joshs
    show drews
    d "Well, I dont want to assume that my twin\nis in a guidance councelling session right now .. "
    hide drews
    show joshs
    j "Well , who knows?"
    extend "Maybe she got pissed\nbecause her lunch is late"
    extend "\nthen she started causing some ruckus ~ "
    play sound "audio/waoh.wav"
    show keu_b at aww_yiss_var2
    extend "{i}HIHI{/i}"
    hide joshs
    show drews
    d "Err - Don't scare me like that .."
    stop music fadeout(1.0)
    d "If that's the case , We better hurry !"
    
    play music "audio/Cartoon.mp3"
    
    scene map_ground with dissolve
    $ renpy.pause(.1)
    call screen urs_map
    
    
    
    
label Shs:
    $ shs = 1
    $ end_na += 1
    show screen umb
    scene shs_1 at zoo
    show narrators
    with dissolve
    "After a short walk ,\nThe Senior High department filled your gaze"
    hide narrators
    show drew_josh at left_shake
    show drews
    with dissolve
    d "So - They also offer Senior Highschool strands?"
    hide drews
    show joshs
    j "Yup !"
    scene shs_2 at zoo
    show joshs 
    #with dissolve
    j "Though the first floor of this building is occupied\nby the College of Education's Faculty ,\nIt is still considered as the SeniorHigh's Department"
    scene shs_3 at zoo
    show joshs
    j "The School library can also be found on\nthe second floor !"
    scene shs_4 at zoo
    show josh at rights
    with dissolve
    menu:
        j "Do you want to check the library ?"
        "yes":
            scene shs_5 at zoo 
            with dissolve
            show drew_a t rights
            show drews 
            d "The Library eh?"
            d "Well , the chance of finding my twin here is low\nbut its nice to see different books sometimes"
            scene shs_4 at zoo
            show josh at right
            with dissolve
            show drew_a at lefts
            show joshs
            j "So , Did you find her inside ?"
            hide joshs
            show drews
            d "Haha unfortunately , No "
            hide drews
            show joshs
            j "So , Let's go ! Time is runnin' fast"
            scene map_ground with dissolve
            $ renpy.pause(.1)
            call screen urs_map
        "No":
            show drew_a t rights
            show drews 
            d "The Library eh?"
            d "Well , the chance of finding my twin here is low\nbut its nice to see different books sometimes"
            hide drews
            show joshs
            j "So , Let's go ! Time is runnin' fast"
            scene map_ground with dissolve
            $ renpy.pause(.1)
            call screen urs_map
                
        
    
    
    
    
    
label Canteen:
    stop music fadeout(1.5)
    
    $ canteen = 1
    $ end_na += 1
    show screen umb
    scene can_1 at zoo
    show drew_josh 
    with dissolve
    show joshs
    j "This is the Canteen"
    play music "audio/trash.mp3"
    scene can_2 at zoo
    show joshs
    with dissolve
    show drew_josh at left_shake
    play sound "audio/romantic.wav"
    j "They offer different varieties of meal each day"
    play sound "audio/twitch.wav"
    show meed_gfx at aww_yiss_var2 behind drew_josh
    extend "\nAnd different policies for a healthy diet"
    hide joshs
    show drews
    with dissolve
    d "Err ,"
    extend " Keulyn looks like not here "
    show emoji_lol_a at emoji_roll #behind drew
    show emoji_lol_b at emoji_roll_b #behind drew
    play sound "audio/eek.wav"
    d "We should look around more "
    hide drews
    show joshs
    stop music fadeout(1.0)
    j "Well , Let's check the map again "
    
    play music "audio/happyplace.mp3"
    scene map_ground with dissolve
    $ renpy.pause(.1)
    call screen urs_map
    
    
    
    
label Coe:
    stop music fadeout(2.0)
    
    $ coe = 1
    $ end_na += 1
    show screen umb
    scene coe_1 at zoo
    show drew_josh at left_shake
    show joshs
    play sound "audio/romantic.wav"
    j "This is the College of Education!"
    play music "audio/Funday.mp3"
    j "The home of future teachers , instructors and many more !"
    hide joshs
    show drews
    d "Oh . I heard that {i}URSAC{/i} focuses on Education Students more\ncompared on other URS campuses .."
    hide drews
    show joshs
    j "Well, The unversity focuses on all courses . \nIt is just that Bachelor of Science in Education\nwas one of the pioneer courses offered by our campus"
    j "And in fact , this building was one of the\noldest here on our campus !" 
    hide joshs
    show drews
    d "Is it true that they yearly conduct different events ?"
    hide drews
    show joshs
    j "Yes !"
    show educ at left_shake
    play sound "audio/twitch.wav"
    j "{i}EDUC{/i} students are well known about those events ! Such as:"
    show educ_1 at left_shake
    play sound "audio/point.wav"
    j "Parades"
    show educ_2 at left_shake
    play sound "audio/point.wav"
    extend "\nVarious Contests and fashion shows"
    show educ_3 at left_shake
    play sound "audio/point.wav"
    extend "\nAnd Different team building games"
    hide educ_1
    hide educ_2
    hide educ_3
    hide educ
    with dissolve
    j "Anyways , Lets take a look inside "
    scene coe_2 at zoo
    $ renpy.pause(1.2)
    scene coe_5 at zoo
    show drew_josh at left_shake
    show joshs
    with dissolve
    play sound "audio/romantic.wav"
    j "The {i}CBA{/i} can be found here "
    hide joshs
    show drews 
    with dissolve
    d "CBA ? 'Corparate and Business Affairs' Right?"
    hide drews
    show joshs
    j "Yes , This is where you can buy different school uniforms\nand other school related stuffs"
    j "For example , This shirt that Im wearing ~"
    j "This is our Campus Shirt and should be\nused ONLY during WEDNESDAY"
    j "But , As you can see -"
    stop music fadeout(.5)
    play sound "audio/I dunno.mp3"
    show thug at left_shake
    j "I'm Wearing it today ~"
    extend "\nJust kiddin' "
    hide thug with dissolve
    stop sound fadeout(3)
    play music "audio/happyplace.mp3" fadein(.5)
    j "We should follow the school's guidelines and regulations\nwhich can be found on our student handbook"
    hide joshs
    show drews
    d "{i}ehehe{/i}"
    scene coe_3 at zoo
    show joshs
    j "The canteen's extension can also be found here -"
    hide joshs
    show drews
    d "Oh man ! "
    extend "\nIt looks like Keulyn is not here"
    hide drews
    show joshs
    stop music fadeout(1.0)
    j "Well , Its not too late to check other places "
    
    play music "audio/Cartoon.mp3"
    scene map_ground with dissolve
    $ renpy.pause(.1)
    call screen urs_map
    
    
    
    
label Coeng:
    stop music fadeout(1.0)
    
    $ coeng = 1
    $ end_na += 1
    show screen umb
    scene eng_1 at zoo
    with dissolve
    show narrators
    "Behold!"
    play music "audio/Funday.mp3"
    "\nThe College of Engineering!"
    show josh at lefts 
    with vpunch
    hide narrators
    show joshs
    play sound "audio/hey.mp3"
    j "Don't steal my lines Narrator kun !" with hpunch
    hide joshs
    show narrators
    "oops {i}hehe{/i}"
    hide narrators
    show joshs
    show josh at rights
    j "Behold!"
    j "\nThe college of Engineering!"
    show drew at lefts
    hide joshs
    show drews
    d "Woah , The view here looks good!"
    hide drew
    hide josh
    show drew_josh at left_shake
    with dissolve
    d "I wanna take a picture !"
    hide drews
    show joshs
    j "Would you please take a picture of us ?"
    hide joshs with dissolve
    menu:
        "Oh sure!":
            call screen cam2
            jump engeng
        "Oh Okay!":
            call screen cam2
            jump engeng
        "(I CAN'T ACTUALLY DECLINE RIGHT? ._.)":
            call screen cam2
            jump engeng
label engeng:
    scene white with vpunch
    scene eng_1 with Dissolve(.5)
    show breezy_101 at left_shake
    show narrators
    stop music fadeout(.5)
    play sound "audio/I dunno.mp3"
    "Weee ~ "
    "~Love is in the air ~"
    stop sound fadeout(3)
    play music "audio/Funday.mp3" fadein(.5)
    scene eng_2 at zoo
    show narrators 
    with dissolve
    "The three of you entered the {i}COENG{/i}'s building"
    hide narrators
    show drew_josh at left_shake
    show joshs
    j "The campus cashier can be found here"
    j "If you need to inquire about payments\nand other finance related stuff -"
    extend "\nThis is the place that you must head first ~"
    scene eng_3 at zoo
    show drew_josh at left_shake
    show joshs
    with dissolve
    j "{i}phew{/i}"
    j "It looks like keulyn is not here ~"
    hide joshs
    show drews
    d "Yeah .. "
    hide drews
    show joshs
    j "Don't lose hope!"
    stop music
    play sound "audio/bdmts.mp3"
    show will at left_shake
    j "We {b}WILL{/b} find her soon! "
    
    j "Unto the map! ~"
    
    
    play music "audio/Cartoon.mp3"
    scene map_ground with dissolve
    $ renpy.pause(.1)
    call screen urs_map
    
    
    
    
label Tree:
    $ tree = 1
    show screen umb
    #$ end_na += 1
    scene bg tree at zoo
    with dissolve
    show narrators
    show drew_josh at left_shake
    "You , Josh and Andrew decided to take a little break ~"
    hide narrators
    show drews
    d "Josh , The ambient here seems nice "
    hide drews
    show joshs
    j "Of course !"
    j "On my opinion , this spot is the most relaxing area on our campus "
    j "Come to think of it ,\nWould you please {i}snap{/i} me a picture with this tree? tehe~"
    show emoji_lol_a at emoji_roll #behind drew
    show emoji_lol_b at emoji_roll_b #behind drew
    play sound "audio/eek.wav"
    j "I just want to take some memento of some sort . {i}HiHi{/i}~"
    call screen cam
label piccc:
    play sound "audio/twitch.wav"
    show white
    $ renpy.pause(.5)
    hide white with Dissolve(0.5)
    scene bg tree at zoo
    show piccc at left_shake
    
    show joshs
    with dissolve
    j "I'm so photogenic {i}talaga{/i} hihi~"
    hide piccc with dissolve
    show drew_josh at left_shake
    j "Well, we better get moving "
    j "Lunch time won't last forever !"
    scene map_ground with dissolve
    $ renpy.pause(.1)
    call screen urs_map
    
    
    
    
label Flag:
    stop music fadeout(1.0)
    
    $ flag = 1
    show screen umb
    #$ end_na += 1
    scene bg flag at zoo
    with dissolve
    show narrators
    "{i}The sun was still at its peak{/i}"
    play music "audio/Curious.mp3"
    hide narrators
    show josh at lefts
    show joshs
    j " err , This is the assembly area "
    show drew at rights
    hide joshs
    show drews
    d "Oh - So this is where students gather for the flag ceremony .."
    d ".."
    d "Anyways , It's so hot , Keulyn is probably not here "
    hide drews
    show joshs
    j "Ha! You're right !"
    stop music fadeout(2.0)
    play music "audio/Cartoon.mp3"
    
    scene map_ground with dissolve
    $ renpy.pause(.1)
    call screen urs_map
    
    
    
    
label Court:
    $ court = 1
    $ end_na += 1
    show screen umb
    scene bg court at zoo
    with dissolve
    show josh at lefts
    show drew at rights
    show joshs
    j "This is our beloved multi-purpose court!"
    j "It also serves as our event area on night events "
    hide joshs
    hide drew
    show drew_a at rights
    show drews
    d "Night events ?"
    hide drews
    show joshs
    hide josh
    show josh_a at lefts
    j "Yeah ! hihi"
    show ily at aww_yiss_var2 behind drew_a
    j "The University organizes night events\nto deepen the bond of every student !"
    j "Well, Obviously there is no one here right now"
    j "Let's look around some more !"
    scene map_ground with dissolve
    $ renpy.pause(.1)
    call screen urs_map
    
    
label Ending_na:
    hide screen umb
    stop music
    play sound "audio/dooom.wav"
    scene black with vpunch
   
    show text "{color=#FFF}Lunch will be over soon{/color} " with dissolve
    $ renpy.pause()
    show text "{color=#FFF}Still , she is nowhere to be found {/color} " with dissolve
    $ renpy.pause()
    show drews
    d ".. I'm a failure as a brother .."
    scene black with vpunch
    play sound "audio/frog.wav"
    show text "{color=#FFF}STOOOP !{/color} " with dissolve
    $ renpy.pause()
    scene end_na_to at zoo
    with dissolve
    show jpe at lefts
    show jps
    jp "Don't tell me that you will give up just like that ?  ~"
    #hide jpe
    #show jpe at center
    show drew_josh at left_shake
    with dissolve
    jp "You were supposed to deliver her lunch right ?\nI would like to help if you want ~"
    hide jps
    show narrators
    "The three of them shared their thoughts about finding keulyn ~ "
    "Unexpectedly .. "
    scene end_na_to at zoomer
    play sound "audio/zoom.mp3"
    $ renpy.pause()
    play music "audio/tenses.mp3"
    scene zoofin at zoo
    $ renpy.pause()
    play sound "audio/guwah.wav"
    show shout at left_shake
    show shout with vpunch
    $ renpy.pause()
    play sound "audio/guwah.wav"
    show shout2 at left_shake
    $ renpy.pause()
    scene black 
    play sound "audio/guwah.wav"
    show text "{size=+30}{color=#FFF} S H O U T !{/color}{/size}"
    with vpunch
    $ renpy.pause()
    scene zoofin
    show tap_tut
    with dissolve
    $ tap = 0
    $ renpy.pause()
    hide tap_tut
    play music "audio/tenses1.mp3"
label ending_na_talaga:
    #play sound "audio/guwah.wav"
    play sound "audio/crk.mp3"
    show tap with hpunch
    $ tap += 2.5
    

    
label ending_na_dapat:
    if tap != 100:
        call screen tapped
    else:
        play shout2 "audio/guwah.wav"
        play shout "audio/suddenstop.mp3"
        stop music
        scene white with vpunch
        $ renpy.pause()
        play sound "audio/dragon.wav"
        $ renpy.pause()
        show text "You unleashed a powerful scream" with dissolve
        $ renpy.pause()
        show text "Loud enough making her notice you ~" with dissolve
        $ renpy.pause()
        scene end_na_to at zoo
        show keyu at center
        show drew_josh at left_shake behind keyu
        show jpe at lefts
        with dissolve
        $ renpy.pause()
        play shout2 "audio/passed.mp3"
        show passed_na with hpunch
        $ renpy.pause()
        hide passed_na with dissolve
        show lyns
        k "Oh hello !"
        play sound "audio/romantic.wav"
        show drew_close_blush at aww_yiss
        hide lyns
        show drews
        d "Oh H-hi !"
        d "Its me ~ I-im here to deliver your lunch .. "
        d "I'm Sorry its kinda late ~"
        play shout "audio/bdts.mp3"
        extend "\ hehe"
        hide drews
        show lyns
        k "well , It is better late than never ~"
        extend "haha"
        hide keyu
        show keyu_d 
        with dissolve
        k "So where is it? "
        hide lyns
        show drews
        d "Oh here !"
        play sound "audio/twitch.wav"
        show lunch at ups
        hide drews
        show lyns
        k "Oh ! Thanks ! but .."
        hide lyns
        show drews
        d "But ? . . "
        hide drews
        show lyns
        k "I'm done eating .. "
        extend "\nI got hungry and since you didnt came on time .. "
        extend "\nIve ate quite my share at the cafeteria .."
        extend "\nbut ~"
        play music "audio/unknown.mp3"
        scene end_na_to at zoo
        show hearty3 at left_shake
        with dissolve
        $ renpy.pause()
        hide hearty3
        show hearty2
        with dissolve
        $ renpy.pause()
        show lyns
        k "Well , you can try next time !"
        k "You're studying here now and we will \nbe seeing each other more often ~"
        k "Who knows ? Maybe I'll be needing your help next time ~"
        extend "\nAnd if that happens , There is your friend and Joshua\non your aid ~"
        hide lyns
        show drews
        d "Ha ! Next time , I'll make sure to deliver it on time !"
        d "Thanks JP ! Thanks Josh !"
        hide drews
        show jps
        jp "Ha , I havent done anything "
        #play sound "audio/bdts.mp3"
        hide jps
        show joshs
        j "And before this game ends , I just wanna say this ~"
        scene end_na_to2 at zoo
        show hearty2
        play sound "audio/romantic.wav"
        show ending at left_shake
        with dissolve
        $ renpy.pause()
        play shout2 "audio/twitch.wav"
        show drew_close_blush at aww_yiss
        $ renpy.pause()
        #play shout "audio/eek.wav"
        #stop music
        show ending2 with dissolve
        $ renpy.pause()
        scene black with dissolve
        show text "{size=+30}{color=#FFF}:: T H E  E N D ::{/color}{/size}"
        $ renpy.pause()
label end_cred:
        scene bg cob1 at zoo
        show cred_josh at left_shake
        show joshs at rights
        play sound "audio/romantic.wav"
        with dissolve
        $ renpy.pause(1.5)
        scene bg guard at zoo
        show cred_jp at left_shake
        show jps at rights
        play sound "audio/romantic.wav"
        with dissolve
        $ renpy.pause(1.5)
        scene bg coba at zoo
        show cred_kyu at left_shake
        show lyns at rights
        play sound "audio/romantic.wav"
        with dissolve
        $ renpy.pause(1.5)
        scene bg out at zoo
        show cred_dre at left_shake
        show drews at rights
        play sound "audio/romantic.wav"
        with dissolve
        $ renpy.pause(1.5)
        scene spscreen with dissolve
        #play sound "audio/zoom.mp3"
        $ renpy.pause(2.2)
        scene blue 
        #play sound "audio/bdts.mp3"
        show text "{size=+30}{color=#FFF}:: T H A N K  Y O U ::{/color}{/size}"
        with dissolve
        stop music fadeout(2)
        $ renpy.pause(1)
        return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
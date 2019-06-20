#much more comples transform animations for images

transform zoom_but:
    xcenter 0.5
    ycenter 0.5
    linear 20.0 zoom 1.2
    linear 20.0 zoom 1.1
    repeat
transform zoo1:
    xcenter 0.5
    ycenter 0.5
    linear 2.0 zoom 0.9
transform zoomer:
    xcenter 0.5
    ycenter 0.5
    linear 2.0 zoom 1.5


transform zoo:
    xcenter 0.5
    ycenter 0.5
    linear 5.5 zoom 0.9
    
transform zoo5:
    xcenter 0.5
    ycenter 0.5
    linear 1 zoom 1
transform rights_out:
    xcenter 1.5
    ycenter 0.5
    linear 5.5 xcenter -1.0
transform ups_back2:
    xcenter 0.5
    ycenter 0.5
    linear 1.5 xcenter -2.0
transform ups_back:
    xcenter 0.5
    ycenter 0.5
    linear 1.5 ycenter -2.0
transform ups:
    xcenter 0.5
    ycenter 1
    linear 0.5 ycenter 0.5
transform ups_out:
    xcenter 0.5
    ycenter 1
    linear 3.5 ycenter 1.5
transform rights1:
    xcenter 1
    ycenter 0.5
    linear 0.5 xcenter 0.5
transform rights1_back:
    xcenter 0.5
    ycenter 0.5
    linear 0.5 xcenter 1.0
transform rights_center:
    xcenter 0.8
    ycenter 0.5
    linear 1.0 xcenter 0.5
transform rights:
    xcenter 1
    ycenter 0.5
    linear 0.5 xcenter 0.8
transform lefts:
    xcenter -1
    ycenter 0.5
    linear 0.5 xcenter 0.2
transform rights_back:
    xcenter 0.8
    ycenter 0.5
    linear 0.5 xcenter 1.8
transform rights_x:
    xcenter 1
    ycenter 0.5
    linear 0.8 xcenter 0.9
    linear 0.8 xcenter 1.5
transform rights_x1:
    xcenter 1
    ycenter 0.5
    linear 0.3 xcenter 0.9
transform rights2:
    xcenter 1
    ycenter 0.5
    linear 1.5 xcenter 0.45
transform rights2_back:
    xcenter 0.45
    ycenter 0.5
    linear 1.5 xcenter 1.5
transform aww_yiss:
    xcenter 1.5
    ycenter 0.5
    linear 4.5 xcenter -1.5
transform leftss:
    xcenter -1.5
    ycenter 0.5
    linear 3.0 xcenter 1.5
transform emoji_roll:
    xcenter 1.5
    ycenter 0.5
    parallel:
        linear 5.5 xcenter -1.5
    parallel:
        linear 7.0 rotate 360.0
        linear 7.0 rotate -360.0
        repeat
transform emoji_roll_b:
    xcenter 1.5
    ycenter 0.5
    parallel:
        linear 5.5 xcenter -1.5
    parallel:
        linear 5.0 rotate -360.0
        linear 7.0 rotate 360.0
transform whuts:
    xcenter 0.5
    ycenter 0.5
   # alpha 1.0
   # parallel:
    linear 2.0 zoom 1.9
    #parallel:
    #    alpha 0.2
    
transform whisper:
    xcenter 0.8
    ycenter 0.5
    linear 1.0 xcenter 0.5
    parallel:
        linear 1.0 zoom 1.7
        
transform left_shake:
    xcenter -1
    ycenter 0.5
    linear 0.5 xcenter 0.5
        
transform aww_yiss_var2:
    xcenter 1.5
    ycenter 0.50
    linear 8.5 xcenter -1.5   
    
# The in-game map function alongwith its x-y clickable hotspot
label nulled:
    call screen urs_map
screen urs_map:
    $ renpy.transition(dissolve)
    if end_na != 8:
        vbox:
            imagemap:
                ground "map_idle.png"
                idle "map_ground.png"
                hover "map_hover.png"
                
                hotspot (899, 65, 373, 467) clicked Jump("nulled")
                if chi == 0:
                    hotspot (141, 163, 173, 64) clicked Jump("Chi") #CHI
                if coba == 0:
                    hotspot (360, 161, 197, 67) clicked Jump("Coba") #COBA
                if osds == 0:
                    hotspot (577, 163, 42, 33) clicked Jump("Osds")  #OSDS
                if shs == 0:
                    hotspot (632, 160, 240, 36) clicked Jump("Shs") #SHS
                if canteen == 0:
                    hotspot (826, 196, 47, 33) clicked Jump("Canteen")  #CANTEEN
                if coe == 0:
                    hotspot (819, 229, 48, 195) clicked Jump("Coe") #COE
                if coeng == 0:
                    hotspot (248, 359, 250, 51) clicked Jump("Coeng") #COENG
                if tree == 0:
                    hotspot (661, 212, 149, 73) clicked Jump("Tree") #TREE
                if flag == 0:
                    hotspot (273, 212, 145, 63) clicked Jump("Flag") #FLAG
                if court == 0:
                    hotspot (94, 357, 144, 60) clicked Jump("Court")  #COURT
    elif end_na == 8:
        add "gfx_dot.png"
        imagebutton:
            idle "pa_end.png" 
            hover "pa_end.png"
            action Jump("Ending_na")
screen tapped:
    hbox:
        xpos 0.3 # Across from right
        ypos 0.4 # Up from bottom
        xanchor 1.0  # On Right
        yanchor 1.0   # On Bottom
        text "{size=+50}{color=#FFF}[tap]{/color}{/size}"
    hbox:
        xpos 0.35 # Across from right
        ypos 0.48# Up from bottom
        xanchor 1.0  # On Right
        yanchor 1.0   # On Bottom
        text "{size=+50}{color=#FFF}TAPS !{/color}{/size}"
    vbox:
        imagemap:
            ground "tap.png"
            hover "tap.png"
            hotspot (1, 1, 719, 1279) clicked Jump("ending_na_talaga")
    
screen cam2:
    $ renpy.transition(dissolve)
    add "screen/cam_back2.png" at zoo
    vbox:
        imagemap:
            ground "screen/cam_a.png"
            hover "screen/cam_b.png"
            hotspot (863, 247, 130, 142) clicked Jump("engeng")
screen cam:
    $ renpy.transition(dissolve)
    add "screen/cam_back.png" at zoo
    vbox:
        imagemap:
            ground "screen/cam_a.png"
            hover "screen/cam_b.png"
            hotspot (863, 247, 130, 142) clicked Jump("piccc")
#custom defined audio channel for playback and sound effect audio layer , buttons etc .
init python:
    renpy.music.register_channel("shout", "shouting", False)
    renpy.music.register_channel("shout2", "shouting", False)
    renpy.music.register_channel("1", "sfx", False)
    renpy.music.register_channel("2", "sfx", False)
    renpy.music.register_channel("3", "sfx", False)
    renpy.music.register_channel("4", "sfx", False)
   
init python:
    style.hotspot.hover_sound = "audio/hoverb.mp3"
    style.choice_button.activate_sound = "audio/hovera.mp3"
    style.choice_button.hover_sound = "audio/hoverb.mp3"
    style.image_button.activate_sound = "audio/hoverb.mp3"
    style.image_button.hover_sound = "audio/hoverb.mp3"
    style.button.activate_sound = "audio/hoverb.mp3"
    style.button.hover_sound = "audio/hoverb.mp3"


transform poppu:
    xcenter 0.5
    ycenter 0.54
    alpha 0.0
    parallel:
        linear 0.2 zoom 1.05
    parallel:
        linear 0.2 ycenter 0.5
    parallel:
        linear 0.2 alpha 1.0
   
   

   
   
   
   
   
   
   
   
   
   
   
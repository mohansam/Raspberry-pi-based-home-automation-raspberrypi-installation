import pygame
import time
import datetime
import os
import subprocess
import threading
import timer
import random
import wallpaper
#import camerapreview
#import assitant
import variable
#import relay
x = -2
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
######## variable decleration and image loading #############
pygame.init()
display_width = 800
display_height = 480
black = (64,64,64)
white = (255,255,255)
line=(255,204,255)
red = (200,0,0)
bright_red=(255,0,0)
light_blue=(0,128,255)
bright_green=(0,255,0)
violet=(147,112,219)
colour_value=light_blue
values=[5,5,5,10]
pygame.mouse.set_visible(False)
Display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('control panel')
icon = pygame.image.load("/home/pi/Desktop/package/snowboy/icon/icon.png")
pygame.display.set_icon(icon)
pygame.display.update()
clock = pygame.time.Clock()
button1_img= pygame.image.load("/home/pi/Desktop/package/snowboy/icon/light.png").convert_alpha()
button2_img= pygame.image.load("/home/pi/Desktop/package/snowboy/icon/fan.png").convert_alpha()
button3_img= pygame.image.load("/home/pi/Desktop/package/snowboy/icon/plug.png").convert_alpha()
button4_img= pygame.image.load("/home/pi/Desktop/package/snowboy/icon/microphone.png").convert_alpha()
button5_img= pygame.image.load("/home/pi/Desktop/package/snowboy/icon/camera.png").convert_alpha()
button6_img= pygame.image.load("/home/pi/Desktop/package/snowboy/icon/timer.png").convert_alpha()
button7_img= pygame.image.load("/home/pi/Desktop/package/snowboy/icon/lamp.png").convert_alpha()
button8_img= pygame.image.load("/home/pi/Desktop/package/snowboy/icon/Ac.png").convert_alpha()
button9_img= pygame.image.load("/home/pi/Desktop/package/snowboy/icon/frame.png").convert_alpha()
button10_img= pygame.image.load("/home/pi/Desktop/package/snowboy/icon/consumption.png").convert_alpha()
rocket=pygame.image.load("/home/pi/Desktop/package/snowboy/icon/rocket.png").convert_alpha()
variable.main=True
light=True
variable.plug_toggle=False
camera_toggle=False
variable.light2_toggle=False
Ac_toggle=False
rocket_y=235
events=None
position=None
colour_change=True
colour_check=False
    ############## button creation and main gui function ###############
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def get_events():
    global events
    events=pygame.event.get()
def touch_pos():
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            return list(event.pos)
def quit_window():
    for event in events:
        if event.type == pygame.QUIT:
            assitant.stop=True
            variable.relayStop=False
            pygame.quit()
            #subprocess.call("sudo shutdown -h now", shell=True)
            quit()
            

def button(msg,x,y,w,h,ic,ac,action=None):
    global colour_change
    if type(position)==list and x+w > position[0] > x and y+h > position[1] > y and action!=None:
        pygame.draw.rect(Display, bright_green,(x,y,w,h))
        action(msg)    
             
    elif variable.light1_toggle==True and msg=="light1":
             pygame.draw.rect(Display, bright_green,(x,y,w,h))
    elif variable.fan_toggle==True and msg=="fan":
             pygame.draw.rect(Display, bright_green,(x,y,w,h))
    elif variable.plug_toggle==True and msg=="plug":
             pygame.draw.rect(Display, bright_green,(x,y,w,h))
    elif assitant.voice_toggle==True and msg=="voice" and assitant.mic_prob==False and assitant.listen==False:
                
             pygame.draw.rect(Display, bright_green,(x,y,w,h))
    elif camera_toggle==True and msg=="camera":
             pygame.draw.rect(Display, bright_green,(x,y,w,h))
    elif variable.timer_toggle==True and msg=="timer":
             pygame.draw.rect(Display, bright_green,(x,y,w,h))
    elif variable.light2_toggle==True and msg=="light2":
             pygame.draw.rect(Display, bright_green,(x,y,w,h))
    elif Ac_toggle==True and msg=="Ac":
             pygame.draw.rect(Display, bright_green,(x,y,w,h))
    elif assitant.voice_toggle==True and msg=="voice" and assitant.mic_prob==False and assitant.listen==True:
             pygame.draw.rect(Display, colour_value,(x,y,w,h))
             if colour_change==True:
                 chang=threading.Thread(target=change_colour_fuc)
                 chang.start()
   
    elif assitant.mic_prob==True and msg=="voice":
             pygame.draw.rect(Display, bright_red,(x,y,w,h))

   
    else:
        pygame.draw.rect(Display, ic,(x,y,w,h))
    smallText = pygame.font.Font("/home/pi/Desktop/package/snowboy/icon/COMIC.TTF",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h-15)) )
    Display.blit(textSurf, textRect)    
def  change_colour_fuc():
    global colour_change
    global colour_value
    global colour_check
    colour_change=False
    time.sleep(0.5)
    if colour_check==False:
        colour_value=bright_green
        colour_check=True
    else:
        colour_value=light_blue
        colour_check=False    
    
    colour_change=True
    
def sidewall():
    global rocket_y
    h_y=rocket_y+50
    a_y=rocket_y+68
    v_y=rocket_y+86
    e_y=rocket_y+104
    a1_y=rocket_y+130
    n_y=rocket_y+156
    i_y=rocket_y+176
    c_y=rocket_y+196
    e1_y=rocket_y+216
    d_y=rocket_y+242
    a2_y=rocket_y+262
    y_y=rocket_y+282
    font = pygame.font.Font("/home/pi/Desktop/package/snowboy/icon/design.graffiti.comicsansmsgras.ttf",21)
    h=font.render("H", True, white)
    a=font.render("A", True, white)
    v=font.render("V", True, white)
    e=font.render("E", True, white)
    n=font.render("N", True, white)
    i=font.render("I", True, white)
    c=font.render("C", True, white)
    d=font.render("D", True, white)
    y=font.render("Y", True, white)
    pygame.draw.rect(Display,violet,(722,10,68,283))
    Display.blit(rocket,[724,rocket_y])
    if h_y<270:
        Display.blit(h,[746,h_y])
    if a_y<270:
        Display.blit(a,[746,a_y])
    if v_y<270:
        Display.blit(v,[746,v_y])
    if e_y<270:
        Display.blit(e,[746,e_y])
    if e_y<270:
        Display.blit(e,[746,e_y])
    if a1_y<270:
        Display.blit(a,[746,a1_y])
    if n_y<270:
        Display.blit(n,[746,n_y])
    if i_y<270:
        Display.blit(i,[746,i_y])
    if c_y<270:
        Display.blit(c,[746,c_y])
    if e1_y<270:
        Display.blit(e,[746,e1_y])
    if d_y<270:
        Display.blit(d,[746,d_y])
    if a2_y<270:
        Display.blit(a,[746,a2_y])
    if y_y<270:
        Display.blit(y,[746,y_y])
    if rocket_y<=-300:
        rocket_y=235
    rocket_y-=2
    

def home():
    pygame.draw.rect(Display,violet,(366,296,424,140))
    currentime = datetime.datetime.time(datetime.datetime.now())
    Date=datetime.date.today().strftime("%A")[:3]+" /"+datetime.date.today().strftime("%B")[:3]+" /"+str(datetime.date.today().strftime("%d"))
    font = pygame.font.Font(None, 50)
    time1= font.render(currentime.strftime("%I:%M %p"), 1, (255,255,255))
    date=font.render(Date, True, (255,255,255))
    font = pygame.font.Font(None, 90)
    text= font.render("LIVING ROOM", True, white)
    Display.blit(time1,[500,310])
    Display.blit(date,[480,340])
    Display.blit(text,[368,375])
    
##################### function for buttton ############

def photoframe(msg):    
    wallpaper.wallpaper_window()
    
def on_off_time():
    timer.timer_window()  
def cameraframe():
    print(variable.time_lst)   
    camerapreview.cam_window() 
   
def game_loop(msg):    
    global camera_toggle    
    global Ac_toggle
    if msg=="light1":
       variable.light1_toggle=not variable.light1_toggle
    if msg=="fan":
        variable.fan_toggle=not variable.fan_toggle
    if msg=="plug":
        variable.plug_toggle=not variable.plug_toggle
    if msg=="voice":
        assitant.voice_toggle=not assitant.voice_toggle
        if assitant.voice_toggle==True:
            assitant.stop=False
            thread=threading.Thread(target=assitant.voice_assitant)
            thread.deaemon=True
            thread.start()
        else:
            assitant.stop=True
    if msg=="camera":
        camera_toggle=not camera_toggle
        cameraframe()
    if msg=="timer":
       on_off_time()
    if msg=="light2":
       variable.light2_toggle=not variable.light2_toggle
    if msg=="Ac":
       Ac_toggle=not Ac_toggle       
    ######### main loop ##########
def main_window():  
        while variable.main==True:
            global position
            get_events()
            quit_window()
            position=touch_pos()      
            Display.fill((255,127,80))
            button("light1",10,10,175,140,light_blue,bright_green,game_loop)
            button("fan",188,10,175,140,light_blue,bright_red,game_loop)
            button("plug",366,10,175,140,light_blue,bright_green,game_loop)
            button("voice",544,10,175,140,light_blue,bright_green,game_loop)
            button("timer",10,153,175,140,light_blue,bright_green,game_loop)
            button("light2",188,153,175,140,light_blue,bright_green,game_loop)
            button("Ac",366,153,175,140,light_blue,bright_green,game_loop)
            button("camera",544,153,175,140,light_blue,bright_green,game_loop)
            button("frame",10,296,175,140,light_blue,bright_green,photoframe)
            button("consumption",188,296,175,140,bright_green,bright_green,game_loop)
            Display.blit(button1_img,(30,10))
            Display.blit(button2_img,(215,5))
            Display.blit(button3_img,(400,10))
            Display.blit(button4_img,(570,10))
            Display.blit(button5_img,(570,153))
            Display.blit(button6_img,(40,153))
            Display.blit(button7_img,(215,153))
            Display.blit(button8_img,(390,153))
            Display.blit(button9_img,(40,290))
            Display.blit(button10_img,(216,296))
            home()
            sidewall()
            pygame.display.update()
            clock.tick(15)
            
        pygame.quit()
        quit()
if __name__ == "__main__":
     t=threading.Thread(target=relay.main_relay)
     t.deaemon=True
     t.start()
     main_window()


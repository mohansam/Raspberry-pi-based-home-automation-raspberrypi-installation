import pygame
import threading
import maingui
import time_set
import variable
import time
pygame.init()
display_width = 800
display_height = 480
Display = pygame.display.set_mode((display_width,display_height))
black = (64,64,64)
yellow=(128,129,0)
light_blue=(0,128,255)
bright_green=(0,255,0)
colour_value=light_blue
variable.time_lst=[10,45,5,0]
am_toggle=True
pm_toggle=False
variable.start_merdian="AM"
variable.stop_merdian="PM"
start_toggle=True
stop_toggle=False
variable.timer_toggle=False
events=None
position=None
colour_change=True
colour_check=False
hour_toggle=True
minute_toggle=False

clock = pygame.time.Clock()
def timer_window():
        global one_thread
        spindown=pygame.image.load("/home/pi/Desktop/package/snowboy/icon/spindown.png").convert_alpha()
        spinup=pygame.image.load("/home/pi/Desktop/package/snowboy/icon/spinup.png").convert_alpha()
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
                                close()


        def button(msg,x,y,w,h,ic,ac,action=None):
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if type(position)==list and x+w > position[0] > x and y+h > position[1] > y:
                    pygame.draw.rect(Display, ac,(x,y,w,h))
                    action(msg)                  
            elif start_toggle==True and msg=="Start time":
                     pygame.draw.rect(Display, bright_green,(x,y,w,h))
            elif stop_toggle==True and msg=="Stop time":
                     pygame.draw.rect(Display, bright_green,(x,y,w,h))
            elif am_toggle==True and msg=="AM":
                     pygame.draw.rect(Display, bright_green,(x,y,w,h))
            elif pm_toggle==True and msg=="PM":
                     pygame.draw.rect(Display, bright_green,(x,y,w,h))
            elif variable.timer_toggle==True and variable.check==False and msg=="On/Off":
                     pygame.draw.rect(Display, bright_green,(x,y,w,h))
            elif variable.timer_toggle==True and variable.check==True and msg=="On/Off":
                     pygame.draw.rect(Display, colour_value,(x,y,w,h))
                     if colour_change==True:
                         chang=threading.Thread(target=change_colour_fuc)
                         chang.start()
            elif hour_toggle==True and msg=="Hour":
                     pygame.draw.rect(Display, ac,(x,y,w,h))
            elif minute_toggle==True and msg=="Minute":
                     pygame.draw.rect(Display, ac,(x,y,w,h))                
            else:
                pygame.draw.rect(Display, ic,(x,y,w,h))

            smallText = pygame.font.Font("/home/pi/Desktop/package/snowboy/icon/COMIC.TTF",20)
            textSurf, textRect = text_objects(msg, smallText)
            if msg=="AM" or msg=="PM" or msg=="Close":
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
            else:
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

            
        def select_box(msg):
            global am_toggle
            global pm_toggle
            global start_toggle
            global stop_toggle
            global hour_toggle
            global minute_toggle
                         
            if msg=="AM":
                am_toggle=True
                pm_toggle=False
                if start_toggle==True:
                    variable.start_merdian=msg                    
                if stop_toggle==True:
                    variable.stop_merdian=msg
            elif msg=="PM":
                pm_toggle=True
                am_toggle=False
                if start_toggle==True:
                    variable.start_merdian=msg
                if stop_toggle==True:
                    variable.stop_merdian=msg
            elif msg=="Start time":
                start_toggle=True
                stop_toggle=False
                if variable.start_merdian!=variable.stop_merdian:
                    if variable.stop_merdian=="PM":
                        am_toggle=True
                        pm_toggle=False
                    else:
                        am_toggle=False
                        pm_toggle=True
                           
            elif msg=="Stop time":
                start_toggle=False
                stop_toggle=True
                if variable.start_merdian!=variable.stop_merdian:
                    if variable.start_merdian=="PM":
                        am_toggle=True
                        pm_toggle=False
                    else:
                        am_toggle=False
                        pm_toggle=True
                
                
            elif msg=="On/Off":
                if variable.time_lst[0]==variable.time_lst[2] and variable.time_lst[1]== variable.time_lst[3] and variable.start_merdian== variable.stop_merdian:
                    return
                th=threading.Thread(target=time_set.main)
                th.daemon=True
                th.start()
                variable.timer_toggle=not variable.timer_toggle
            elif msg=="Hour":
                hour_toggle=True
                minute_toggle=False
            elif msg=="Minute":
                hour_toggle=False
                minute_toggle=True
         
          
                
            
            
        def spin(x,y,w,h,ic,ac,action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x+w > mouse[0] > x and y+h > mouse[1] > y:
                pygame.draw.rect(Display, ac,(x,y,w,h))

                if click[0] == 1 and action != None:
                    action()         
            else:
                pygame.draw.rect(Display, ic,(x,y,w,h))
        def spin_up():
                click = pygame.mouse.get_pressed()
                if click[0]==1:
                    if hour_toggle==True:
                        if start_toggle==True and variable.time_lst[0]<12:
                            variable.time_lst[0]+=1
                            pygame.time.wait(300)
                        elif start_toggle==True:
                            variable.time_lst[0]=1
                            pygame.time.wait(300)
                        elif stop_toggle==True and variable.time_lst[2]<12:
                            variable.time_lst[2]+=1
                            pygame.time.wait(300)
                        elif stop_toggle==True:
                            variable.time_lst[2]=1
                            pygame.time.wait(300)
                    else:
                        if start_toggle==True and variable.time_lst[1]<59:  
                            variable.time_lst[1]+=1
                            pygame.time.wait(300)
                        elif start_toggle==True:
                            variable.time_lst[1]=0
                            pygame.time.wait(300)
                        elif stop_toggle==True and variable.time_lst[3]<59:
                            variable.time_lst[3]+=1
                            pygame.time.wait(300)
                        elif stop_toggle==True:
                            variable.time_lst[3]=0
                            pygame.time.wait(300)                                           
                                              
        def spin_down():
            click = pygame.mouse.get_pressed()
            if click[0]==1:
                if hour_toggle==True:
                    if start_toggle==True and variable.time_lst[0]>1:
                        variable.time_lst[0]-=1
                        pygame.time.wait(300)
                    elif start_toggle==True:
                        variable.time_lst[0]=12
                        pygame.time.wait(300)
                    elif stop_toggle==True and variable.time_lst[2]>1:
                        variable.time_lst[2]-=1
                        pygame.time.wait(300)
                    elif stop_toggle==True:
                        variable.time_lst[2]=12
                        pygame.time.wait(300)
                else:
                    if start_toggle==True and variable.time_lst[1]>0:
                        variable.time_lst[1]-=1
                        pygame.time.wait(300)
                    elif start_toggle==True:
                        variable.time_lst[1]=59
                        pygame.time.wait(300)
                    elif stop_toggle==True and variable.time_lst[3]>0:
                        variable.time_lst[3]-=1
                        pygame.time.wait(300)
                    elif stop_toggle==True:
                        variable.time_lst[3]=59
                        pygame.time.wait(300)
                    
                        
                    
        def text_objects(text, font=20):
            textSurface = font.render(text, True, (255,255,255))
            return textSurface, textSurface.get_rect()
        def show_text(text,size,x,y,w,h):
            smallText = pygame.font.Font("/home/pi/Desktop/package/snowboy/icon/digital-7.ttf",size)
            textSurf, textRect = text_objects(text, smallText)
            textRect.center = ( (x+(w/2)), (y+(h/2)) )
            Display.blit(textSurf, textRect)
        def show_time(hour,minute):
            show_text(str(hour),110,50,50,125,140)
            show_text(str(minute),110,175,50,125,140)
        def close(msg=None):
            maingui.main_window()
            


        while 1:
                get_events()
                quit_window()
                position=touch_pos()
             #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                  #  close()
                    
                Display.fill((255,127,80))
                pygame.draw.rect(Display,light_blue,(40,40,270,170))
                pygame.draw.rect(Display,bright_green,(50,50,250,150))
                spin(500,43,100,74,light_blue,bright_green,spin_up)
                spin(500,140,100,74,light_blue,bright_green,spin_down)
                button("AM",350,43,120,70,light_blue,bright_green,select_box)
                button("PM",350,140,120,70,light_blue,bright_green,select_box)
                button("Start time",44,290,150,80,light_blue,bright_green,select_box)
                button("Stop time",200,290,150,80,light_blue,bright_green,select_box)
                button("On/Off",356,290,150,80,light_blue,bright_green,select_box)
                button("Close",512,290,150,80,light_blue,bright_green,close)
                button("Hour",50,50,125,150,bright_green,yellow,select_box)
                button("Minute",170,50,130,150,bright_green,yellow,select_box)
                pygame.draw.rect(Display,light_blue,(165,100,10,10))
                pygame.draw.rect(Display,light_blue,(165,130,10,10))
                Display.blit(spinup,(500,30))
                Display.blit(spindown,(500,127))
                if start_toggle==True:
                        show_time(variable.time_lst[0],variable.time_lst[1])
                else:
                        show_time(variable.time_lst[2],variable.time_lst[3])
                if variable.timer_toggle==True:
                        show_text("ON",40,356,290,150,80)                                                
                            
                else:
                        
                        show_text("OFF",40,356,290,150,80)                        
                s_time=str(variable.time_lst[0])+":"+str(variable.time_lst[1])+"  "+variable.start_merdian
                st_time=str(variable.time_lst[2])+":"+str(variable.time_lst[3])+" "+variable.stop_merdian
                show_text(s_time,40,44,290,150,80)
                show_text(st_time,40,200,290,150,80)
                pygame.display.update()
                clock.tick(10)
if __name__ == "__main__":
     timer_window()

import snowboydecoder
import sys
import signal
import pygame
import threading
import time
import variable
pygame.init()
pygame.mixer.init()
starting_sound=pygame.mixer.Sound("/home/pi/Desktop/package/snowboy/resources/starting_speech.wav")
lighton_sound=pygame.mixer.Sound("/home/pi/Desktop/package/snowboy/resources/turning on light.wav")
fanon_sound=pygame.mixer.Sound("/home/pi/Desktop/package/snowboy/resources/turning on fan.wav")
lightoff_sound=pygame.mixer.Sound("/home/pi/Desktop/package/snowboy/resources/turning off light.wav")
fanoff_sound=pygame.mixer.Sound("/home/pi/Desktop/package/snowboy/resources/fanoff.wav")
turnedon_device=pygame.mixer.Sound("/home/pi/Desktop/package/snowboy/resources/turned on device.wav")
turnedoff_device=pygame.mixer.Sound("/home/pi/Desktop/package/snowboy/resources/turned off device.wav")
stoping_sound=pygame.mixer.Sound("/home/pi/Desktop/package/snowboy/resources/sleep.wav")
wake_sound=pygame.mixer.Sound("/home/pi/Desktop/package/snowboy/resources/wakeup.wav")
heysam_sound=pygame.mixer.Sound("/home/pi/Desktop/package/snowboy/resources/heysam.wav")
helpme_sound=pygame.mixer.Sound("/home/pi/Desktop/package/snowboy/resources/help me.wav")
voice_toggle=False
variable.light1_toggle=False
variable.fan_toggle=False
stop=False
mic_prob=False
wakeup=False
call_listen=True
listen=False
t1=None
def voice_assitant():
    try:
        global mic_prob
        global wakeup
        if wakeup==False:
            pygame.mixer.Sound.play(starting_sound)
            wakeup=True
        else:
            pygame.mixer.Sound.play(wake_sound)
        def interrupt_callback():
            global listen
            global call_listen
            if stop==True:
                listen=False
                call_listen=True
                print("stoped............/n")
                pygame.mixer.init()
                pygame.mixer.stop()
                pygame.mixer.Sound.play(stoping_sound)
                return stop
        def light_on():
            global mic_prob
            pygame.mixer.stop()
            if listen==True:
                if variable.light1_toggle==False:
                    pygame.mixer.Sound.play(lighton_sound)
                    variable.light1_toggle=True
                else:
                    pygame.mixer.Sound.play(turnedon_device)
        def light_off():
            if listen==True:
                pygame.mixer.stop()
                if variable.light1_toggle==True:
                    pygame.mixer.Sound.play(lightoff_sound)
                    variable.light1_toggle=False
                    if variable.check==True:
                        variable.timer_toggle=False
                else:
                    pygame.mixer.Sound.play(turnedoff_device)
        def on_fan():            
            pygame.mixer.stop()
            if listen==True:
                if variable.fan_toggle==False:
                    pygame.mixer.Sound.play(fanon_sound)
                    variable.fan_toggle=True
                else:
                    pygame.mixer.Sound.play(turnedon_device)
        def fan_off():            
            if listen==True:
                if variable.fan_toggle==True:
                    pygame.mixer.Sound.play(fanoff_sound)
                    variable.fan_toggle=False
                else:
                    pygame.mixer.Sound.play(turnedoff_device)
        def hey_sam():
            global listen
            global call_listen
            pygame.mixer.stop()
            pygame.mixer.Sound.play(heysam_sound)
            if call_listen==True:
                listen=True
                t1=threading.Thread(target=listen_fuc)
                t1.start()
                
        def listen_fuc():
            global call_listen
            global listen
            call_listen=False
            time.sleep(60)
            print("stop")
            listen=False
            call_listen=True
        def help_me():
            pygame.mixer.stop()
            pygame.mixer.Sound.play(helpme_sound)
        model=['/home/pi/Desktop/package/snowboy/resources/onfan.pmdl','/home/pi/Desktop/package/snowboy/resources/lighton.pmdl','/home/pi/Desktop/package/snowboy/resources/turn_off_light.pmdl','/home/pi/Desktop/package/snowboy/resources/heysam.pmdl','/home/pi/Desktop/package/snowboy/resources/turn_off_fan.pmdl','/home/pi/Desktop/package/snowboy/resources/help_me.pmdl']
        sensitivity = [0.5]*len(model)
        callbacks=[on_fan,light_on,light_off,hey_sam,fan_off,help_me]
        detector = snowboydecoder.HotwordDetector(model, sensitivity=sensitivity)
        print('Listening... Press Ctrl+C to exit')
        detector.start(detected_callback=callbacks,
                       interrupt_check=interrupt_callback,
                       sleep_time=0.03)
        
        detector.terminate()
    except:
        print("problem with microphone")
        mic_prob=True
        print(mic_prob)
if __name__ == "__main__":
    voice_assitant()

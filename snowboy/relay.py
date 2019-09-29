import RPi.GPIO as GPIO
import variable
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
light1=37
fan=35
plug=33
light2=31
GPIO.setup(light1, GPIO.OUT)
GPIO.setup(fan, GPIO.OUT)
GPIO.setup(plug, GPIO.OUT)
GPIO.setup(light2, GPIO.OUT)
GPIO.output(light1,GPIO.HIGH)
GPIO.output(fan,GPIO.HIGH)
GPIO.output(plug,GPIO.HIGH)
GPIO.output(light2,GPIO.HIGH)
def main_relay():
	while variable.relayStop==True:
		GPIO.output(light1, not variable.light1_toggle)
		GPIO.output(fan, not variable.fan_toggle)
		GPIO.output(plug, not variable.plug_toggle)
		GPIO.output(light2, not variable.light2_toggle)
		time.sleep(0.1)
	GPIO.cleanup()
	print ("Shutdown All relays")
	quit()
if __name__=="__main__":
	main_relay()

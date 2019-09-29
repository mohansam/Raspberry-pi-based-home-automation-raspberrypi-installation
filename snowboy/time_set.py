from gpiozero import TimeOfDay
from datetime import datetime, time
import variable
import time as t
start_object=None
start_time=None
stop_time=None
def main():
	variable.check=False
	print(datetime.now().time())
	def convert_to24(hour,minute,merdian):
		ti=str(hour)+':'+str(minute)+' '+merdian
		strt = t.strptime(ti, '%I:%M %p')
		t1=t.strftime('%H:%M', strt)
		return t1
	def set_time():
		global start_object
		if int(start_time[:2])==0 and int(stop_time[:2])==0:
			start_object=TimeOfDay(time(12,int(start_time[-2:])), time(12,int(stop_time[-2:])),utc=False)
		elif int(start_time[:2])==0:
			start_object=TimeOfDay(time(12,int(start_time[-2:])), time(int(stop_time[:2]),int(stop_time[-2:])),utc=False)					
		elif int(stop_time[:2])==0:
			start_object=TimeOfDay(time(int(start_time[:2]),int(start_time[-2:])), time(12,int(stop_time[-2:])),utc=False)
		else:
			start_object=TimeOfDay(time(int(start_time[:2]),int(start_time[-2:])), time(int(stop_time[:2]),int(stop_time[-2:])),utc=False)
		
	start_time=convert_to24(variable.time_lst[0],variable.time_lst[1],variable.start_merdian)
	stop_time=convert_to24(variable.time_lst[2],variable.time_lst[3],variable.stop_merdian)
	print(start_time,stop_time)	
	set_time()
	while variable.timer_toggle:
		print(start_object.value,variable.check)
		
		if start_object.value==True:
			variable.check=True
			variable.light1_toggle=True
		if start_object.value==False and variable.check==True:
			variable.check=False
			variable.timer_toggle=False			
		t.sleep(1)
	variable.light1_toggle=False	
	print("stoped............................")
if __name__=="__main__":
	main()


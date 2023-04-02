import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

#PIR Sencor
GPIO.setup(3,GPIO.IN)
#Water Pump Moter
GPIO.setup(4,GPIO.OUT)
#Smell detection sencor
GPIO.setup(5,GPIO.IN)
GPIO.setup(6,GPIO.IN)
#Flush Button
GPIO.setup(7,GPIO.IN)

while True:
    str state;
    val1=GPIO.input(3)
    val2=GPIO.output(4)
    val3=GPIO.input(5)
    val4=GPIO.input(6)
    
    if val1==1:
        state="IN"
        flush_water(state)
        perfume(val3,val4)
        
        
    else val1==0:
        state="OUT"
        flush_water(state)
        perfume(val3,val4)

def flush_water(state):
    bval=GPIO.input(7)
    if state=="OUT" && bval==0 :
        print "flush water"
    else if state=="OUT" && bval==1:
        print "donot flushwater"
        
def perfume(smell1,smell2):
    if smell1>0.7 && smell2>0.6:
        print "Release Perfume"
    else :
        print "Donnt release Perfume"
        
    
    
    
        
    
    
    

from __future__ import division
import time
import Adafruit_PCA9685

#Aktiviert den Spannungsumsetzer vor dem PCA9685
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.OUT, initial=GPIO.HIGH)


# Standardadresse: (0x40).
#pwm = Adafruit_PCA9685.PCA9685()

# Initalisierung mit alternativer Adresse
pwm = Adafruit_PCA9685.PCA9685(address=0x41)

# Einstellen der Minimal- und Maximal-Pulslaengen
servo_min = 150  # Minimale Pulslaenge
servo_max = 600  # Maximale Pulslaenge

# Hilfsfunktion
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000 
    pulse_length /= 50     
    print('{0}us per period'.format(pulse_length))
    pulse_length /= 4096     
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    print(pulse_length)
    pulse /= pulse_length
    print(pulse)
    pulse = round(pulse)
    print(pulse)
    pulse = int(pulse)
    print (pulse)
    pwm.set_pwm(channel, 0, pulse)

# Frequenz auf 50Hz setzen
pwm.set_pwm_freq(50)

print('Druecke Ctrl+C zum abbrechen...')
#while True:
start_position0 = 0.5 
start_position1 = 0.65
start_position2 = 1.5
start_position3 = 1.9
start_position4 = 0.85
start_position5 = 1.25
end_position0 = 2.5    
end_position1 = 1.5
end_position2 = 1.5   
end_position3 = 1.9
end_position4 = 1.8
end_position5 = 1.8
#  Kanal 0 Motor 1 (Kralle)
 # if ()

set_servo_pulse(1,end_position1)
time.sleep(1.0)
set_servo_pulse(5,end_position5)
time.sleep(1.0)
set_servo_pulse(0,start_position0)
time.sleep(1.0)
# Kanal 1 Motor 2 (Handgelenk1)
set_servo_pulse(1,start_position1)
time.sleep(2.0) 
# Kanal 2 Motor 3 (Handgelenk2)
set_servo_pulse(2,start_position2)
time.sleep(1.0)
# Kanal 4 Motor 4 (Oberarm)
set_servo_pulse(3,start_position3)
time.sleep(1.0)
set_servo_pulse(5,start_position5)
time.sleep(1.0)
# Kanal 5 Motor 6 (Unterarm)
set_servo_pulse(4,start_position4)
time.sleep(1.0)
# Kanal 5 Motor 6 (Schwenkgelenk)
set_servo_pulse(1,end_position1)
time.sleep(1.0)
set_servo_pulse(2,end_position2)
time.sleep(1.0)
set_servo_pulse(3,end_position3)
time.sleep(1.0)
set_servo_pulse(0,end_position0)
time.sleep(1.0)
set_servo_pulse(4,end_position4)
time.sleep(1.0)
set_servo_pulse(1,start_position1)
time.sleep(2.0)
set_servo_pulse(4,start_position4)
time.sleep(1.0)
set_servo_pulse(5,end_position5)
time.sleep(2.0)



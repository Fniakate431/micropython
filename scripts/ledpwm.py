from machine import Pin, PWM
import utime
pin = 4 #number for gpio pin
 
pwm_pin = PWM (Pin(pin))
#frequency is cycles per second (Hertz,Hz)
pwm_pin.freq(10)#Hz

percent = 10
pwm_pin.duty_u16(percent*1000)



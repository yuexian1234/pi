import RPi.GPIO as GPIO
import time
 
# 设置编码方式
GPIO.setmode(GPIO.BOARD)
 
# 设置引脚
OUT1 = 40
OUT2 = 16
GPIO.setup(OUT1, GPIO.OUT)
GPIO.setup(OUT2, GPIO.OUT)
 
# 实例化PWM
pwm1 = GPIO.PWM(OUT1, 60)
pwm2 = GPIO.PWM(OUT2, 60)
 
# 开启PWM
pwm1.start(0)
pwm2.start(0)
t=100 
for _ in range(t):
    # 黄灯呼吸
    for dc in range(0, 101, 5):
        pwm1.ChangeDutyCycle(dc)
        time.sleep(0.1)
 
    for dc in range(100, -1, -5):
        pwm1.ChangeDutyCycle(dc)
        time.sleep(0.1)
 
    # 绿灯呼吸
    for dc in range(0, 101, 5):
        pwm2.ChangeDutyCycle(dc)
        time.sleep(0.1)
 
    for dc in range(100, -1, -5):
        pwm2.ChangeDutyCycle(dc)
        time.sleep(0.1)
else:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

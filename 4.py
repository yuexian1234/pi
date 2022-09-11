import RPi.GPIO as GPIO
import time
 
# 设置编码方式和引脚
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
 
# 实例化PWM，初始频率为50Hz，占空比为50%
pwm = GPIO.PWM(16, 50)
while True:
    pwm.start(50)
    time.sleep(1) 
    # 修改占空比为100%
    pwm.ChangeDutyCycle(100)
 
# 停止PWM，释放引脚资源
pwm.stop()
GPIO.cleanup()

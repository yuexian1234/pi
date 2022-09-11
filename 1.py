import RPi.GPIO as GPIO                # 引入GPIO模块
from time import sleep                     # 引入time模块
GPIO.setmode(GPIO.BCM)            # 使用BCM编号方式
GPIO.setup(16,GPIO.OUT)            # 将GPIO19设置为输出模式
while True:                                     # 无限循环  
    GPIO.output(16,GPIO.HIGH)   # 将GPIO19设置为高电平，点亮LED  
    sleep(1)                                    # 等待1秒钟 
    GPIO.output(16,GPIO.LOW)  # 将GPIO19设置为低电平，熄灭LED 
    sleep(1)                              # 等待0.5秒钟 
input()                                      # 按下任意键退出
GPIO.cleanup()                     # 清理释放GPIO资源，将GPIO复位 


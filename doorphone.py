import time
import RPi.GPIO as GPIO
import logconf
import webhook

sw = 2
state = 0

def switch_callback(gpio_pin):
    global state
    print(time.time(), gpio_pin)
    #GPIO.output(led, GPIO.HIGH)
    if state:
        state = 0
    else:
        state = 1

def state_machine():
    global state
    if state == 0:
        pass
    elif state == 1:
        state = 2
    elif state == 2:
        if GPIO.input(sw) == 0:
            logconf.logger.debug("doorphone rang")
            webhook.post("doorphone rang!!!!")
        state = 0

if __name__ == "__main__":
    logconf.log_init()
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(sw, GPIO.FALLING, bouncetime=1000)
    GPIO.add_event_callback(sw, switch_callback)
    try:
        while True:
            state_machine()
            time.sleep(0.2)
    except KeyboardInterrupt:
        GPIO.cleanup()
        logconf.logger.info("Got SIGINT, exiting.")

import RPi.GPIO as GPIO
import time

# Pin definitions
TRIG = 23
ECHO = 24
LED = 17

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def distance():
    # Trigger a 10µs pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Measure echo time
    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    # Calculate distance in cm
    elapsed = stop_time - start_time
    dist = (elapsed * 34300) / 2
    return dist

try:
    while True:
        dist = distance()
        print(f"Distance: {dist:.1f} cm")
        
        # LED control
        if dist < 5:      # LED ON only if object is closer than 5 cm
            GPIO.output(LED, GPIO.HIGH)
        else:
            GPIO.output(LED, GPIO.LOW)

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Stopped by user")
    GPIO.cleanup()


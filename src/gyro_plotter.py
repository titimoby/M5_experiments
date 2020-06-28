import imu
import time

gyro = imu.IMU()
while True:
    print(gyro.ypr)
    time.sleep(0.1)

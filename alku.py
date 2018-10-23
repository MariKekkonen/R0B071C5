#!/usr/bin/env python3
#Mari Kekkonen/Robots of Ni
#Python code created during Robot Uprising 2018 hackathon, Helsinki, Finland 

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_3
from ev3dev2.sensor.lego import ColorSensor
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, MoveTank
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_2, INPUT_4

us=UltrasonicSensor(INPUT_2)
us2=UltrasonicSensor(INPUT_4)
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
cs = ColorSensor(INPUT_1)

cs.mode = 'COL-REFLECT'
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
cs1 = ColorSensor(INPUT_1)
cs2 = ColorSensor(INPUT_3)

#alifunktio alku, oranssi osa ongelma!!
def start():
    cs1.mode = 'COL-REFLECT'
    cs2.mode = 'COL-REFLECT'
    tank_drive.on_for_seconds(SpeedPercent(30), SpeedPercent(30), 3)
    while True:
        if cs1.reflected_light_intensity>20: #oikea sensori
            tank_drive.off()
            tank_drive.on_for_seconds(SpeedPercent(10), SpeedPercent(0), 1) #oik.m.
            break
        elif cs2.reflected_light_intensity>20: #vasen sensori
            tank_drive.off()
            tank_drive.on_for_seconds(SpeedPercent(10), SpeedPercent(0), 1) #oik.m.
            break
        else:
            tank_drive.run_forever(speed_sp=190)   # equivalent to power=20 in EV3-G
    
    while True:
        if cs1.reflected_light_intensity==0: #oikea sensori => pysahdy reunalla
            tank_drive.off()
            tank_drive.on(left_speed = -10, right_speed = -10)
            tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(0), 1)
        elif cs2.reflected_light_intensity==0: #vasen sensori => pysahdy reunalla
            tank_drive.off()
            tank_drive.on(left_speed = -10, right_speed = -10)
            tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(0), 1)
        else:
            tank_drive.run_forever(speed_sp=190)   # equivalent to power=20 in EV3-G

start()

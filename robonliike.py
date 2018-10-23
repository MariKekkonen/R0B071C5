#!/usr/bin/env python3
#Mari Kekkonen/Robots of Ni
##Python code created during Robot Uprising 2018 hackathon, Helsinki, Finland 

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

#koodi kolmostehtävää varten; jäi kesken 
tank_drive.on_for_seconds(left_speed = 33, right_speed = 36, seconds = 10) #oik loiva kaarre
tank_drive.on_for_seconds(left_speed = 38, right_speed = 32, seconds = 10) #vas loiva kaarre
tank_drive.on_for_seconds(left_speed = 36, right_speed = 0, seconds = 3) #tiukka mutka
tank_drive.off()
tank_drive.on_for_seconds(left_speed=18, right_speed=15, seconds=2)
tank_drive.on_for_seconds(left_speed=-15, right_speed=-20, seconds=2)

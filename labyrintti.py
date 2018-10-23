#!/usr/bin/env python3
#Mari Kekkonen/Robots of Ni
#Python code created during Robot Uprising 2018 hackathon, Helsinki, Finland 

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_3
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
cs1 = ColorSensor(INPUT_1) #oikea sensori
cs2 = ColorSensor(INPUT_3) #vasen sensori

#alifunktio keltaiselle laatalle
def yellowBadge():
    cs1.mode = 'COL-COLOR'
    cs2.mode = 'COL-COLOR'
    while True:
        if cs1.color==4:
            tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), 1.5)
            tank_drive.off()
            sleep(4.0)
            tank_drive.on_for_seconds(left_speed=-20, right_speed=-20, seconds=1.5) #peruutus
            tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(0), 2) #kaannos
            tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), 2)
            tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(74), 3.5) #kaantyminen
            break
        elif cs2.color==4:
            tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), 1.5)
            tank_drive.off()
            sleep(4.0)
            tank_drive.on_for_seconds(left_speed=-20, right_speed=-20, seconds=1.5) #peruutus
            tank_drive.on_for_seconds(SpeedPercent(70), SpeedPercent(0), 2) #kaannos
            tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), 2)
            tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(74), 3.5) #kaantyminen
            break
        else:
            tank_drive.run_forever(speed_sp=190)   # equivalent to power=20 in EV3-G

#alifunktio valkoisen viivan seuraamiselle kahden värisensorin avulla
def turn90():
    cs1.mode = 'COL-REFLECT'
    cs2.mode = 'COL-REFLECT'
    while True:
        if cs1.reflected_light_intensity<20: #oikea sensori
            tank_drive.off()
            tank_drive.on_for_seconds(SpeedPercent(10), SpeedPercent(0), 1) #vas.m.
        elif cs2.reflected_light_intensity<20: #vasen sensori
            tank_drive.off()
            tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(10), 1) #oik.m.
        elif cs1.reflected_light_intensity<10: #oikea sensori fix
            tank_drive.off()
            tank_drive.on_for_seconds(SpeedPercent(15), SpeedPercent(0), 0.2) #vas.m.
        elif cs2.reflected_light_intensity<10: #vasen sensori fix
            tank_drive.off()
            tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(15), 0.2) #oik.m.
        else:
            tank_drive.on_for_seconds(SpeedPercent(15), SpeedPercent(15), 1.0)


tank_drive.on_for_seconds(SpeedPercent(30), SpeedPercent(30), 4.3) #suora ajo
tank_drive.on_for_seconds(SpeedPercent(74), SpeedPercent(0), 3.5) #kaantyminen vasemmalle
tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), 2.6) #suora ajo
tank_drive.on_for_seconds(SpeedPercent(0), SpeedPercent(72), 3) #kaantyminen oikealle
yellowBadge()
turn90()

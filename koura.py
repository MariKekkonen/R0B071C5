#!/usr/bin/env python3
#Mari Kekkonen/Robots of Ni
#kolmatta tehtävää varten tehty koodi esineisiin tarttumista ja siirtämistä varten; jäi kesken 

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.motor import MediumMotor, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_3
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
mm = MediumMotor(OUTPUT_D)

#koura kiinni
mm.on_for_rotations(SpeedPercent(-10), 0.5)
#koura auki
mm.on_for_rotations(SpeedPercent(10), 2)

tank_drive.on_for_rotations(left_speed = -20, right_speed = -20, rotations = 3)

#koura kiinni
mm.on_for_rotations(SpeedPercent(-15), 1.3)

#liiku esineen kanssa
tank_drive.on_for_rotations(left_speed = 20, right_speed = 20, rotations = 3)

#koura auki
mm.on_for_rotations(SpeedPercent(10), 2)

#liiku pois
tank_drive.on_for_rotations(left_speed = 20, right_speed = 20, rotations = 3)

#koura kiinni
mm.on_for_rotations(SpeedPercent(-15), 2.5)

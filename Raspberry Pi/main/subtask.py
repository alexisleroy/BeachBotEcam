# /usr/bin/env
# -*- coding: Utf8 -*-
"""
@author: Louis Defauw
@date: 27.03.2015
@note: Sous taches a effectuees pour arriver a l objectif definit par tasks
"""

import logging
# import find_path
import param
import RPi.GPIO as GPIO
import time


def plot1(XYa):
    logging.info("fetch plot")
    # qqch du genre lancer un process/thread avec un cmpt en // qui l arrete si
    # ca devient trop long, sinon il se relance s il s est arreter
    #    find_path.findPath(XYa)
    #    param.BrasI2C.open()
    # changer 3
    # param.MotorsI2C.forward(50)
    # param.MotorsI2C.backward(50)
    #    param.BrasI2C.grab("plot")
    # param.BrasI2C.grabPlot()

    # correctionAngle = 360/335
    # param.BrasI2C.fermeTube()
    # param.BrasI2C.grabPlot()
    # param.BrasI2C.upPlot()
    # param.BrasI2C.release()
    # param.BrasI2C.down()

    # param.BrasI2C.grabBall()
    # param.BrasI2C.upBall()
    # param.BrasI2C.release()
    # param.BrasI2C.down()

    # param.BrasI2C.grabGlass()
    # param.BrasI2C.upTransport()
    # param.BrasI2C.down()
    # param.BrasI2C.release()

    # param.BrasI2C.prepaClap(0)
    # param.BrasI2C.upPlot()
    # param.BrasI2C.hitClap(0)
    # param.BrasI2C.down()
    # param.BrasI2C.prepaClap(1)
    # param.BrasI2C.upPlot()
    # param.BrasI2C.hitClap(1)
    # param.BrasI2C.down()
    # param.BrasI2C.ouvrirTube()
    if GPIO.input(param.pinStrategie) == 0:
        if param.teamColor is "Green":
            param.MotorsI2C.forward(8)
            time.sleep(0.5)
            param.MotorsI2C.turnLeft(31)
            time.sleep(0.5)
            param.MotorsI2C.forward(23)
            time.sleep(0.5)
            #param.MotorsI2C.forward(15)
            #time.sleep(0.5)
            param.BrasI2C.down()
            time.sleep(0.5)
            param.BrasI2C.release()
            time.sleep(1)
            param.BrasI2C.grabPlot()
            time.sleep(0.5)
            param.BrasI2C.upPlot()
            time.sleep(0.5)
            param.MotorsI2C.forward(22)
            time.sleep(0.5)
            param.MotorsI2C.turnRight(35)
            time.sleep(0.5)
            param.MotorsI2C.forward(11)
            time.sleep(0.5)
            param.BrasI2C.release()
            time.sleep(0.5)
            param.BrasI2C.down()
            time.sleep(1)
            param.BrasI2C.grabPlot()
            time.sleep(0.5)
            param.BrasI2C.upPlot()
            time.sleep(0.5)
            param.MotorsI2C.turnLeft(39)
            time.sleep(1)
            param.MotorsI2C.turnLeft(20)
            time.sleep(1)
            #param.MotorsI2C.turnLeft(42)
            #time.sleep(0.5)
            param.MotorsI2C.forward(9)
            time.sleep(0.5)
            param.BrasI2C.release()
            time.sleep(0.5)
            param.BrasI2C.down()
            time.sleep(1.5)
            param.BrasI2C.grabPlot()
            time.sleep(0.5)
            param.BrasI2C.upPlot()
            time.sleep(0.5)
            param.MotorsI2C.forward(5)
            time.sleep(0.5)
            param.MotorsI2C.turnRight(19)
            time.sleep(0.5)
            param.MotorsI2C.forward(5)
            time.sleep(1.5)
            param.BrasI2C.down()
            time.sleep(0.5)
            param.BrasI2C.ouvrirTube()
            time.sleep(0.5)
            param.BrasI2C.release()
            time.sleep(0.5)
            param.MotorsI2C.backward(15)
            time.sleep(0.5)
            param.MotorsI2C.turnRight(50)
            time.sleep(0.5)
            param.MotorsI2C.turnRight(50)
            time.sleep(0.5)
            param.MotorsI2C.turnRight(50)
            time.sleep(0.5)
            param.MotorsI2C.forward(20)
            time.sleep(0.5)
            param.MotorsI2C.forward(20)
            time.sleep(0.5)
        else:
            param.MotorsI2C.forward(8)
            time.sleep(0.5)
            param.MotorsI2C.turnRight(34)
            time.sleep(0.5)
            param.MotorsI2C.forward(18)
            time.sleep(0.5)
            param.MotorsI2C.forward(15)
            time.sleep(0.5)
            param.BrasI2C.down()
            time.sleep(0.5)
            param.BrasI2C.release()
            time.sleep(1.5)
            param.BrasI2C.grabPlot()
            time.sleep(0.5)
            param.BrasI2C.upPlot()
            time.sleep(0.5)
            param.MotorsI2C.forward(21)
            time.sleep(0.5)
            param.MotorsI2C.turnLeft(36)
            time.sleep(0.5)
            param.MotorsI2C.forward(18)
            time.sleep(0.5)
            param.BrasI2C.release()
            time.sleep(0.5)
            param.BrasI2C.down()
            time.sleep(1.5)
            param.BrasI2C.grabPlot()
            time.sleep(0.5)
            param.BrasI2C.upPlot()
            time.sleep(0.5)
            param.MotorsI2C.turnRight(43)
            time.sleep(1)
            param.MotorsI2C.turnRight(42)
            time.sleep(0.5)
            param.MotorsI2C.forward(15)
            time.sleep(0.5)
            param.BrasI2C.release()
            time.sleep(0.5)
            param.BrasI2C.down()
            time.sleep(1.5)
            param.BrasI2C.grabPlot()
            time.sleep(0.5)
            param.BrasI2C.upPlot()
            time.sleep(0.5)
            param.MotorsI2C.forward(5)
            time.sleep(0.5)
            param.MotorsI2C.turnLeft(19)
            time.sleep(0.5)
            param.MotorsI2C.forward(15)
            time.sleep(1.5)
            param.BrasI2C.down()
            time.sleep(0.5)
            param.BrasI2C.ouvrirTube()
            time.sleep(0.5)
            param.BrasI2C.release()
            time.sleep(0.5)
            param.MotorsI2C.backward(10)
            time.sleep(0.5)
    else:
        justeUnPoint()
    # param.MotorsI2C.forward(20)
    # param.MotorsI2C.turnLeft(90)
    # param.MotorsI2C.forward(50)
    # param.MotorsI2C.turnLeft(90)
    # param.MotorsI2C.forward(20)
    # param.MotorsI2C.turnLeft(90)
    # param.MotorsI2C.turnLeft(int(50*correctionAngle))
    return True


def glass(XYa):
    #    find_path.findPath(XYa)
    #    param.BrasI2C.open()
    # changer 3
    #    param.MotorsI2C.forward(3)
    return True


def release(XYa):
    pass


def clap(XYa):
    param.BrasI2C.hitClap(param.colorTeam)
    param.BrasI2C.amorcagePince()
    return True

def justeUnPoint():
    if param.teamColor is "Green":
        param.BrasI2C.release()
        time.sleep(0.5)
        param.MotorsI2C.forward(8)
        time.sleep(0.5)
        param.MotorsI2C.turnLeft(35)
        time.sleep(0.5)
        param.MotorsI2C.forward(18)
        time.sleep(0.5)
        param.MotorsI2C.forward(15)
        time.sleep(1.5)
        param.BrasI2C.down()
        time.sleep(1.5)
        param.BrasI2C.release()
        time.sleep(1.5)
        param.BrasI2C.grabPlot()
        time.sleep(0.5)
        param.BrasI2C.upPlot()
        time.sleep(0.5)
        param.MotorsI2C.turnRight(55)
        time.sleep(0.5)
        param.MotorsI2C.turnRight(55)
        time.sleep(0.5)
        param.MotorsI2C.turnRight(55)
        time.sleep(0.5)
        param.MotorsI2C.forward(20)
        time.sleep(0.5)
        param.BrasI2C.down()
        time.sleep(0.5)
        param.BrasI2C.release()
        time.sleep(0.5)
    else:
        param.BrasI2C.release()
        time.sleep(0.5)
        param.MotorsI2C.forward(8)
        time.sleep(0.5)
        param.MotorsI2C.turnRight(34)
        time.sleep(0.5)
        param.MotorsI2C.forward(18)
        time.sleep(0.5)
        param.MotorsI2C.forward(15)
        time.sleep(0.5)
        param.BrasI2C.down()
        time.sleep(0.5)
        param.BrasI2C.release()
        time.sleep(0.5)
        param.BrasI2C.grabPlot()
        time.sleep(0.5)
        param.BrasI2C.upPlot()
        time.sleep(0.5)
        param.MotorsI2C.turnLeft(51)
        time.sleep(0.5)
        param.MotorsI2C.turnLeft(51)
        time.sleep(0.5)
        param.MotorsI2C.turnLeft(51)
        time.sleep(0.5)
        param.MotorsI2C.forward(20)
        time.sleep(0.5)
        param.BrasI2C.down()
        time.sleep(1.5)
        param.BrasI2C.release()
        time.sleep(0.5)
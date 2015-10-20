#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: Louis Defauw & Alexis Paques
@date: 18.03.2015
@note: Test de la communication i2c
@todo: Vérifier la réception de l'array de bytes
"""

from struct import *
import time
import quick2wire.i2c as i2c

def send(data,self):
	d = liste(data)
	print("Envoi de donnees (%d,%d) a l'adresse %i" % (d[0], d[1], self.address))
	self.bus.transaction(i2c.writing_bytes(self.address,d[0],d[1]))

def read(self):
	print("Lecture de donnees a l'adresse %i" % (self.address))
	data = self.bus.transaction(i2c.reading(self.address,4))
	print(data)
	return data

def liste(xy):
	x = xy >> 8
	y = xy & 255
	return [x,y]

def pack(x, y):
	if x <= 15 and x >= 0:
		x = x << 12
	else:
		x = 0
	if y > 4095 or y < 0:
		y = 0
	return (x + y)

def unPack(data):
	d = unpack('bbbb',data[0])
	x = (d[0] << 8) + d[1]
	y = (d[2] << 8) + d[3]
	return [x,y]

class MotorsI2CFunctions():
	def __init__(self):
		self.address = 8
		self.bus = i2c.I2CMaster()

	def stop(self):
		data = pack(1,0)
		send(data,self)

	def forward(self, length):
		data = pack(2,length)
		send(data,self)

	def backward(self, length):
		data = pack(3,length)
		send(data,self)

	def turnLeft(self, angle):
		data = pack(4,angle)
		send(data,self)

	def turnRight(self, angle):
		data = pack(5,angle)
		send(data,self)

	def getXY(self):
		data = read(4,self)
		XY = unPack(data)
		return XY

mo = MotorsI2CFunctions()

mo.forward(10)

time.sleep(1)

mo.turnRight(10)

time.sleep(1)

print(mo.getXY())

time.sleep(1)
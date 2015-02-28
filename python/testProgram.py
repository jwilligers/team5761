import mcpi.minecraft as minecraft
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(11, GPIO.IN)


mc = minecraft.Minecraft.create()

mc.postToChat("Hello world")

x,y,z = mc.player.getPos()

print (x)
print (y)
print(z)

# mc.player.setPos(x + 10, y ,z)
x,y,z = mc.player.getPos()
print (x)

tnt = 46
stone = 1
dirt = 2
gold = 41
x1,y1,z1 = mc.player.getPos()

doIt = False
doIt2 = True
print(range(6, 2, -1))
if(doIt):
	for x in range(int(x1 + 1), int(x1 + 11)):
		for y in range(int(y1 + 1), int(y1 + 11)):
			for z in range(int(z1 + 1), int(z1 + 11)):
				mc.setBlock(x, y, z, 5)
if(doIt2):
	print range(int(y1 + 7), int(y1 + 2), -1)
	for y in range(int(y1 + 7), int(y1 + 2), -1):
		print("x: ")
		print(range(int(x1 - 5 + y - y1), int(x1 + 5 + y1 - y)))
		for x in range(int(x1- 5 + y - y1), int(x1 + 5 + y1 - y)):
			print("z: ")
			print(range(int(z1- 5 + y - y1), int(z1 + 5 + y1 - y)))
			for z in range(int(z1- 5 + y - y1), int(z1 + 5 + y1 - y)):
				mc.setBlock(x, y, z, 22)
while True:
	x, y, z = mc.player.getPos()
	if mc.getBlock(x, y-1, z) == dirt or mc.getBlock(x, y-1, z) == stone:
		mc.setBlock(x, y-1, z, tnt,1)
		
	if (mc.getBlock(9, 7, -13) == 50):
		GPIO.output(3, True)
	else:
		GPIO.output(3, False)

	if (mc.getBlock(10, 7, -13) == 50):
		GPIO.output(5, True)
	else:
		GPIO.output(5, False)
	if (GPIO.input(11)):
		mc.setBlock(x + 2, y + 2, z + 2, tnt, 1)
		
	
	time.sleep(0.05)



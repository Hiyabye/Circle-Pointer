import pyautogui
import math

def CalculateCircle(size, centerX, centerY):
  centerX = int(centerX)
  centerY = int(centerY)

  left = int(centerX - size)
  right = int(centerX + size)
  up = int(centerY - size)
  down = int(centerY + size)

  i = left
  j = up

  while True:
    while i >= left and i <= centerX: # Up Crust
      j = centerY - math.sqrt(size ** 2 - (i - centerX) ** 2)
      pyautogui.moveTo(i, j, 0.05)
      print(str(i) + " " + str(j))
      i+=5
    while j >= up and j <= centerY: # Right Crust
      i = math.sqrt(size ** 2 - (j - centerY) ** 2) + centerX
      pyautogui.moveTo(i, j, 0.05)
      print(str(i) + " " + str(j))
      j+=5
    while i >= centerX and i <= right: # Down Crust
      j = math.sqrt(size ** 2 - (i - centerX) ** 2) + centerY
      pyautogui.moveTo(i, j, 0.05)
      print(str(i) + " " + str(j))
      i-=5
    while j >= centerY and j <= down: # Left Crust
      i = centerX - math.sqrt(size ** 2 - (j - centerY) ** 2)
      pyautogui.moveTo(i, j, 0.05)
      print(str(i) + " " + str(j))
      j-=5

# Get screen size
screenWidth, screenHeight = pyautogui.size()
centerX, centerY = screenWidth / 2, screenHeight / 2
print("The size of the screen is " + str(screenWidth) + "x" + str(screenHeight))

# Get circle size
if screenWidth >= screenHeight:
  maxSize = (screenHeight / 2) - 50
else:
  maxSize = (screenWidth / 2) - 50
print("The max size recommended for you is " + str(maxSize))
size = int(input("Enter the size of the circle: "))
pyautogui.alert("The mouse will now move in a circle size of " + str(size) + ".\nTo stop press shift+f5.")
CalculateCircle(size, centerX, centerY)
import pyautogui
import math

def CalculateCircle(size, centerX, centerY):
  centerX = int(centerX)
  centerY = int(centerY)

  left = int(centerX - size)
  right = int(centerX + size)
  up = int(centerY - size)
  down = int(centerY + size)

  for i in range(left, centerX, 5): # Up Crust
    j = centerY - math.sqrt(size ** 2 - (i - centerX) ** 2)
    pyautogui.moveTo(i, j, 0.05)
    print(str(i) + " " + str(j))
    i+=5
  for j in range(up, centerY, 5): # Right Crust
    i = math.sqrt(size ** 2 - (j - centerY) ** 2) + centerX
    pyautogui.moveTo(i, j, 0.05)
    print(str(i) + " " + str(j))
  for i in range(right, centerX, -5):  # Down Crust
    j = math.sqrt(size ** 2 - (i - centerX) ** 2) + centerY
    pyautogui.moveTo(i, j, 0.05)
    print(str(i) + " " + str(j))
  for j in range(down, centerY, -5): # Left Crust
    i = centerX - math.sqrt(size ** 2 - (j - centerY) ** 2)
    pyautogui.moveTo(i, j, 0.05)
    print(str(i) + " " + str(j))

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
while True:
  CalculateCircle(size, centerX, centerY)
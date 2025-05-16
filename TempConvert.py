#TempConvert.py
#Name: Caden Cerny
#Date: Feb. 9, 2025
#Assignment: Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = int(input("Enter the temperature in Fahrenheit: "))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = (tempF - 32) * 5 / 9
  tempC = round(tempC, 1)
  #Output converted temperature.
  
  print(tempF, "degrees fahrenheit is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()

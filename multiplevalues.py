n=int(input("Enter the value of n:"))
for i in range (n):
  w=int(input("Enter the value of wind speed :"))
  t=int(input("Enter the value of wind temperature :"))
  h=int(input("Enter the value of humidity :"))

W=0.5*t**2-0.2*h+0.1*w-15
print(W)
if(W>300):
    print("Weather is Sunny")
elif(200<W<=300):
    print("Weather is Cloudy")
elif(100<W<=200):
        print("Weather is Rainy")
else:
     print("weather is stormy")

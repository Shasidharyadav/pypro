w=60
t=20
h=30
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

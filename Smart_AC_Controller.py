Temperature = float(input('Enter Temperature(in Celcius) : '))
Humidity = float(input('Enter Humidity(in %) : '))
manual_off = False
if(manual_off == False) and (Temperature > 30 or Humidity > 70) : 
    print('The AC Will Turn ON')
else:
    print('The AC Will Turn OFF')
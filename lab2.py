sec=int(input("Enter number of sec"))
sec=sec%(24*60*60)
hour=sec//3600
sec%=3600
min=sec//60
sec%=60
print("hour,sec,min")


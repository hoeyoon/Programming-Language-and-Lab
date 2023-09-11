s = int(input("Number : "))
sec = s % 60
hour = s / 3600
min = (s % 3600)/60
print("Hour : %d" % hour)
print("Minute : %d" % min)
print("Second :", sec)
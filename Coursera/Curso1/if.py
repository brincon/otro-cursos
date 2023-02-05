hrs = input("Enter Hours:")
h = float(hrs)
tarifa = input("Rate per Hours:")
t = float(tarifa)
if h > 40 :
    p = h * t
    res = (h-40)*(t*0.5)
    total = p + res
else : 
    total = h * t
print (total)



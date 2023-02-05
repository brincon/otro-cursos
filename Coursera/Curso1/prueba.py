def computepay (h, r):
    if h > 40 :
        p = h * r
        res = (h-40)*(r*0.5)
        total = p + res
    else : 
        total = h * r
    return (total)

hrs = input("Enter Hours:")
h = float (hrs)
tarifa = input("Rate per Hours:")
r = float (tarifa)
total = computepay (h, r)
print ("Pay", total)

print (total)
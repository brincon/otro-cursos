str = "X-DSPAM-Confidence:    0.8475"
punto = str.find(':')
print (punto)
fin=str[punto+1:]
print (float(fin))


x = len (str)
print (x)
import csv
import math

a = 0
z = 0

def cosine (var):
    return math.cos(math.radians(var))

def sine (var):
    return math.sin(math.radians(var))

def arc (var):
    return math.acos(var) * (180/math.pi)

def calc (year, hour, mn, lat=32, lng=-96, tz=-6):
    print("y,h,m: " + str(year) + "," + str(hour) + "," + str(mn))
    y = (2 * math.pi/365) * year - 1 + (hour - 12)/24
    eq = 229.18 * (0.000075 + 0.001868 * math.cos(y) - 0.032077 * math.sin(y) - 0.014615 * math.cos(2 * y) - 0.040849 * math.sin(2 * y))
    decl = 0.006918 - (0.399912 * math.cos(y)) + (0.070257 * math.sin(y)) - (0.006758 * math.cos(2 * y)) + (0.000907 * math.sin(2 * y)) - (0.002697 * math.cos(3 * y)) + (0.00148 * math.sin(3 * y))
    time_offset = eq + (4 * lng) - (60 * tz)
    tst = (hour * 60) + mn + time_offset
    ha = (tst/4) - 180
    coszenith = (sine(lat) * math.sin(decl)) + (cosine(lat) * math.cos(decl) * cosine(ha))
    z = arc(coszenith)
    a = arc(-(sine(lat) * coszenith - math.sin(decl))/(cosine(lat) * sine(z)))
    if (ha > 0):
        a = 360 - a
    print(a)
    print(z)
    return {"azimuth":round(a,2), "zenith":round(z,2)}

calc(327,20,48)

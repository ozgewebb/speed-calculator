"""
The knot is a unit of speed (not distance).
1 knot (kt) = 1.15077945 miles per hour (mph).
If your ship is traveling at 20 knots, that means it is going 23 miles per hour.
The program below measures and displays speed in knots, miles and feet.
"""

distance_in_mi = 60
time_in_hours = 3

distance_in_kn = distance_in_mi / 1.15078
distance_in_ft = distance_in_mi * 5280

time_in_seconds = time_in_hours * 3600

speed_in_knots = distance_in_kn / time_in_hours
speed_in_mph = distance_in_mi / time_in_hours
speed_in_ft = distance_in_ft / time_in_seconds

print("The speed in knots is:", speed_in_knots)
print("The speed in miles per hour is:", speed_in_mph)
print("The speed in feet per second is:", speed_in_ft)

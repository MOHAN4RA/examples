# Total no of cars
cars=100

# Space in a car
space_in_a_car=4.0

# Total no of drivers
drivers=30

# Total no of Passengers
passengers=90

# cars in shed 
cars_not_driven= cars - drivers

# cars in Roaming
cars_driven=drivers

# Total capacity in Driven car
carpool_capacity = cars_driven * space_in_a_car

# Average passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are", cars , "cars available."
print "There are only" , drivers, "drivers available."
print "There will be", cars_not_driven , "empty cars today."
print "We can Transport", carpool_capacity, "people Today."
print "We have" , passengers , "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

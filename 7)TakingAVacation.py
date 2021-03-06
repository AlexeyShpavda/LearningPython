# Contents:
# Before We Begin
# Planning Your Trip
# Getting There
# Transportation
# Pull it Together
# Hey, You Never Know!
# Plan Your Trip!

print("### Before We Begin ###")
def bigger(first, second):
  print(max(first, second))
  return True

bigger(1, 3)

print("### Planning Your Trip ###")
def hotel_cost(nights):
  return 140 * nights

print("### Getting There ###")
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

print("### Transportation ###")
def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

print("### Pull it Together ###")
# def trip_cost(city, days):
#   return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city)

print("### Hey, You Never Know! ###")
def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("### Plan Your Trip! ###")
print(trip_cost("Los Angeles", 5, 600))
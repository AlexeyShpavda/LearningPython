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
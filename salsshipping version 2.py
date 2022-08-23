# Weight of the Package Ordered - Write Package weight here
weight = 11

# Premium Shippin? (yes)True or (no)False
premium_shipping = True

# Ground Shipping or Drone Shipping
# Ground = false - Drone = True
drone_shipping = True

# Ground Shipping
Price_per_pound_1 = 1.5
Price_per_pound_2 = 3
Price_per_pound_3 = 4
Price_per_pound_4 = 4.75

flat_charge = 20
flat_charge_premium = 125

weight_price_1 = (weight * Price_per_pound_1)
weight_price_2 = (weight * Price_per_pound_2)
weight_price_3 = (weight * Price_per_pound_3)
weight_price_4 = (weight * Price_per_pound_4)

# Drone Shipping
Price_per_pound_drone_1 = 4.5
Price_per_pound_drone_2 = 9
Price_per_pound_drone_3 = 12
Price_per_pound_drone_4 = 14.25
weight_price_drone_1 = (weight * Price_per_pound_drone_1)
weight_price_drone_2 = (weight * Price_per_pound_drone_2)
weight_price_drone_3 = (weight * Price_per_pound_drone_3)
weight_price_drone_4 = (weight * Price_per_pound_drone_4)

if drone_shipping == False:
  if premium_shipping == False:
    if weight <= 2:
      print(f"Price for Shipping: {weight_price_1 + flat_charge}$")
    elif weight <= 6:
      print(f"Price for Shipping: {weight_price_2 + flat_charge}$")
    elif weight <= 10:
      print(f"Price for Shipping: {weight_price_3 + flat_charge}$")
    elif weight >= 10:
      print(f"Price for Shipping: {weight_price_4 + flat_charge}$")
    else:
      print("error")
  elif premium_shipping == True:
    if weight <= 2:
      print(f"Price for Shipping: {weight_price_1 + flat_charge_premium}$")
    elif weight <= 6:
      print(f"Price for Shipping: {weight_price_2 + flat_charge_premium}$")
    elif weight <= 10:
      print(f"Price for Shipping: {weight_price_3 + flat_charge_premium}$")
    elif weight >= 10:
      print(f"Price for Shipping: {weight_price_4 + flat_charge_premium}$")
    else:
      print("error")
elif drone_shipping == True:
    if weight <= 2:
      print(f"Price for Drone Shipping: {weight_price_drone_1}$")
    elif weight <= 6:
      print(f"Price for Drone Shipping: {weight_price_drone_2}$")
    elif weight <= 10:
      print(f"Price for Drone Shipping: {weight_price_drone_3}$")
    elif weight >= 10:
      print(f"Price for Drone Shipping: {weight_price_drone_4}$")
    else:
      print("error")

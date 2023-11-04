weight = float(input("Package weight: "))

# "Ground shipping"
if weight <= 2:
  cost_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.00 + 20.00
else:
  cost_ground = weight * 4.75 + 20.00
#print(cost_ground)

#Premium ground shipping
cost_premium = 125.00

#Drone shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

#Cheapest method
if cost_ground < cost_premium and cost_ground < cost_drone:
  print("Ground shipping is best choice: $", cost_ground)
elif cost_ground > cost_drone and cost_ground < cost_premium:
  print("Drone shipping is best choice: $", cost_drone)
elif cost_ground > cost_premium and cost_premium < cost_drone:
  print("Premium shipping is best choice: $", cost_premium)
else:
  print("Error")

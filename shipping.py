weight = 4.8
# Ground shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
print("Ground shipping $",cost_ground)

 # Ground shipping Premium
cost_ground_premium = 125.00 
print("Ground Shipping Premium $",cost_ground_premium)

# Drone Shipping
if weight <= 2:
  cost_drone_shipping = weight * 4.50
elif weight <= 6:
  cost_drone_shipping = weight * 9.00
elif weight <= 10:
  cost_drone_shipping = weight * 12.00
else:
  cost_drone_shipping = weight * 14.25

print("Drone Shipping $",cost_drone_shipping)

# This program calculates the shipping cost of a package when shipped one of three ways; ground shipping, premium ground shipping, and drone shipping
weight = 1.5
premium_shipping = 125

""" 
Weight of Package	                             Price per Pound	Flat Charge
2 lb or less	                                 $1.50	            $20.00
Over 2 lb but less than or equal to 6 lb         $3.00	            $20.00
Over 6 lb but less than or equal to 10 lb	     $4.00	            $20.00
Over 10 lb	$4.75	$20.00
"""

if weight <= 2 :
  ground_cost = 20 + (weight * 1.5)
elif weight <= 6 :
  ground_cost = 20 + (weight * 3)
elif weight <= 10 :
  ground_cost = 20 + (weight * 4)
else :
  ground_cost = 20 + (weight * 4.75)
print("Ground Shipping is",ground_cost)

# Premium Ground Shipping is a flat $125.00
print("Premium Ground Shipping is",premium_shipping)

""" Drone Shipping
 Weight of Package	                             Price per Pound	Flat Charge
2 lb or less	                                 $4.50	            $0.00
Over 2 lb but less than or equal to 6 lb	     $9.00	            $0.00
Over 6 lb but less than or equal to 10 lb	     $12.00	            $0.00
Over 10 lb	                                     $14.25	            $0.00
"""
if weight <= 2 :
  drone_cost  = weight * 4.5

elif weight <= 6 :
  drone_cost = weight * 9

elif weight <= 10 :
  drone_cost = weight * 12

else :
  drone_cost = weight * 14.25

print("Drone Shipping is", drone_cost)
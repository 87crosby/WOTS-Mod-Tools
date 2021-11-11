"""
Script to calculate armor penetration of different ship-fired projectiles
"""

weight = float(input("Enter the weight of the projectile (lbs): "))
velocity = float(input("Enter the velocity of the projectile (fps): "))
diameter = float(input("Enter the bore diameter of the gun (inches): "))


penetration = (.0004689 * (weight**0.55) * (velocity**1.1))/(diameter**0.65)
pen_mm = penetration * 25.4

# test = weight**0.55

print(pen_mm)
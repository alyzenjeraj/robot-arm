import math

# Geometric and kinematic parameters
L1 = 10.0  # l1
L2 = 8.0  # l2
L3 = 5.0  # l3
L4 = 4.0  # l4
L5 = 3.0  # l5

# inverse kin end effector position
def calculate_inverse_kinematics(x, y, z):
    
    theta1 = math.atan2(y, x)

    
    r = math.sqrt(x**2 + y**2) - L5
    d = math.sqrt(r**2 + z**2)

    
    cos_theta2 = (d**2 - L3**2 - L4**2) / (2 * L3 * L4)
    theta2 = math.atan2(math.sqrt(1 - cos_theta2**2), cos_theta2)

    
    cos_theta3 = (L3**2 + L4**2 - d**2) / (2 * L3 * L4)
    theta3 = math.atan2(math.sqrt(1 - cos_theta3**2), cos_theta3)

    
    theta4 = math.atan2(z, r)

    
    theta5 = 0

    #calc joint angles
    return theta1, theta2, theta3, theta4, theta5


x = 15.0  # x-coord
y = 10.0  # y-coord
z = 5.0  # z-coord

joint_angles = calculate_inverse_kinematics(x, y, z)


print("Joint angles:")
for i, angle in enumerate(joint_angles):
    print(f"Theta{i+1}: {math.degrees(angle)} degrees")

from eeecc import multiply_point, subtract_points, add_points

print("4*H = H+H+H+H")
multiply_point((32, 32), 4, print_tables=True)

print("C - F")
subtract_points((12, 2), (6, 39), print_out=True)

print("C + G")
add_points((12, 2), (12, 41), print_out=True)

print("2*M")
multiply_point((6, 39), 2, print_tables=True)

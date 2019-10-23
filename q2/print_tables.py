from eeecc import multiply_point, subtract_points, add_points

# print("Pulverizer tables for ")
multiply_point((32, 32), 4, print_tables=True)
subtract_points((12, 2), (6, 39), print_out=True)
add_points((12, 2), (12, 41), print_out=True)
multiply_point((6, 39), 2, print_tables=True)

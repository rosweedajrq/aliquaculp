# Sample collection of extents
extents_collection = [(1, 3), (2, 5), (-1, 4)]

# Initialize global min and max extents
global_min = float('inf')
global_max = float('-inf')

# Iterate through the collection of extents
for extent in extents_collection:
    min_val, max_val = extent
    if min_val < global_min:
        global_min = min_val
    if max_val > global_max:
        global_max = max_val

# Output the global min and max extents
print("Global min extent:", global_min)
print("Global max extent:", global_max)

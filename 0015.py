xy = [0, 0]
num_of_paths = {}
def get_paths(n, xy, num_of_paths):
    if xy[0] > n or xy[1] > n:
        return 0
    
    if xy[0] == n or xy[1] == n:
        return 1
    
    if num_of_paths.get(tuple(xy), None) is not None:
        return num_of_paths[tuple(xy)]
    
    right_path = get_paths(n, [xy[0] + 1, xy[1]], num_of_paths)
    num_of_paths[(xy[0] + 1, xy[1])] = right_path
    down_path = get_paths(n, [xy[0], xy[1] + 1], num_of_paths)
    num_of_paths[(xy[0], xy[1] + 1)] = down_path
    return right_path + down_path

print(get_paths(20, xy, num_of_paths)) # 137846528820
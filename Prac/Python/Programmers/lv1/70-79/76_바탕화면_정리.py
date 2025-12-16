def solution(wallpaper):
    y_arr = []
    x_arr = []
    for y_idx, y_wp in enumerate(wallpaper):
        for x_idx, x_wp in enumerate(y_wp):
            if x_wp == '#':
                y_arr.append(y_idx)
                x_arr.append(x_idx)   
    return [min(y_arr), min(x_arr), max(y_arr) + 1, max(x_arr) + 1]
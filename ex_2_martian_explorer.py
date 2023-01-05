def is_in_field(ro, co, fld):
    if 0 <= ro < fld and 0 <= co < fld:
        return True


def goes_out_of_field(ro, co, fld):
    if ro < 0:
        ro = fld - 1
    if ro > fld - 1:
        ro = 0
    if co < 0:
        co = fld - 1
    if co > fld - 1:
        co = 0
    return ro, co


def moving_positions():
    positions = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    return positions


def resources():
    resource = {
        'Water': 0,
        'Metal': 0,
        'Concrete': 0,
    }
    return resource


def is_suitable_to_start_colony(resource):
    result = True
    for k, v in resource.items():
        if v == 0:
            result = False
    return result


def find_rover_position(matrx):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrx[i][j] == 'E':
                return i, j


field = 6
matrix = []
water = 0
resources_volume = resources()
for _ in range(field):
    matrix.append(input().split(' '))

commands = input().split(', ')
current_row, current_col = find_rover_position(matrix)
for command in commands:
    ro_direction, co_direction = moving_positions()[command]
    current_row += ro_direction
    current_col += co_direction

    if not is_in_field(current_row, current_col, field):
        current_row, current_col = goes_out_of_field(current_row, current_col, field)
    current_symbol = matrix[current_row][current_col]
    if current_symbol == "W":
        resources_volume['Water'] += 1
        print(f'Water deposit found at {current_row, current_col}')
    elif current_symbol == "M":
        resources_volume['Metal'] += 1
        print(f'Metal deposit found at {current_row, current_col}')
    elif current_symbol == 'C':
        resources_volume['Concrete'] += 1
        print(f'Concrete deposit found at {current_row, current_col}')
    elif current_symbol == 'R':
        print(f'Rover got broken at {current_row, current_col}')
        break



if is_suitable_to_start_colony(resources_volume):
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')

print(matrix)
import pandas as pd
from pandas import DataFrame

def create_grouped_list(input_list):
    """
    convert list of list to list of set
    :param input_list: [[a,b],c,[d,e]]
    :return: [{a,b},{c},{d,e}]
    """
    output_list = []
    for item in input_list:
        current_group = set()
        if isinstance(item, list):
            current_group.update(item)
        else:
            current_group.add(item)
        output_list.append(current_group)
    return output_list

def calculate_distance_from_left(input_list):
    """
    calculate distance of all element in list to left side
    :param input_list:
    [['0', 80],
    ['a', 32],
    ['0', 8],
    ['b', 103],
    ['0', 379],
    ['c', 300],
    ['0', 379],
    ['d', 16],
    ['e', 88],
    ['0', 40]]
    :return:
    [['a', 80], ['b', 88], ['c', 467], ['d', 846], ['e', 846]]
    """
    cur_distance = 0
    res = []
    for e in input_list:
        if e[0] == '0':
            cur_distance += e[1]
        else:
            res.append([e[0], cur_distance])
    return res

def calculate_size(input_list):
    """
    remove space from input_list to create list of element's size
    :param input_list:
    [['0', 80],
    ['a', 32],
    ['0', 8],
    ['b', 103],
    ['0', 379],
    ['c', 300],
    ['0', 379],
    ['d', 16],
    ['e', 88],
    ['0', 40]]
    :return:
    [['a', 32],
    ['b', 103],
    ['c', 300],
    ['d', 16],
    ['e', 88]]
    """
    return [e for e in input_list if e[0] != '0']

def create_features(input_list,
                    output_list,
                    direction="horizontal",
                    idx=-1):
    """
    receive input list and output list and create distance and size features
    :param input_list:
    [['0', 80],
    ['a', 32],
    ['0', 8],
    ['b', 103],
    ['0', 379],
    ['c', 300],
    ['0', 379],
    ['d', 16],
    ['e', 88],
    ['0', 40]]
    :param output_list:
    [['a', 'b'], 'c', ['d', 'e']]
    :param direction
    "horizontal" or "vertical"
    :param idx
    index in dataframe
    :return:
    [(idx, 8, 71, True, direction),
     (idx, 387, 268, False, direction),
     (idx, 766, 16, False, direction),
     (idx, 766, 56, False, direction),
     (idx, 379, 197, False, direction),
     (idx, 758, 87, False, direction),
     (idx, 758, 15, False, direction),
     (idx, 379, 284, False, direction),
     (idx, 379, 212, False, direction),
     (idx, 0, 72, True)] d -> e
    """
    left_distances = calculate_distance_from_left(input_list)
    sizes = calculate_size(input_list)
    group_list = create_grouped_list(output_list)
    res = []
    for i in range(len(left_distances)):
        for j in range(i + 1, len(left_distances)):
            diff_distance = abs(left_distances[i][1] - left_distances[j][1])
            diff_size = abs(sizes[i][1] - sizes[j][1])
            is_same_group = False
            for e in group_list:
                if left_distances[i][0] in e and left_distances[j][0] in e:
                    is_same_group = True
                    break
            res.append([idx, diff_distance, diff_size, is_same_group, direction])
    return res


def create_features_df(input_list) -> DataFrame:
    left_distances = calculate_distance_from_left(input_list)
    sizes = calculate_size(input_list)
    features = []
    for i in range(len(left_distances)):
        for j in range(i + 1, len(left_distances)):
            diff_distance = abs(left_distances[i][1] - left_distances[j][1])
            diff_size = abs(sizes[i][1] - sizes[j][1])
            features.append([left_distances[i][0], left_distances[j][0], diff_distance, diff_size])
    df = pd.DataFrame(features, columns=["id_1", "id_2", "diff_distance", "diff_size"])
    return df[["id_1", "id_2", "diff_distance", "diff_size"]]

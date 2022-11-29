import math
import csv_to_list

[x,y] = csv_to_list.getList()
#x = [206260,206998,206807,206863,207599,208216,208457,208489,208945,209386,209231,209887,210691,209819,209840,209542,206685,206724,207523,207597,208883,208852,209181,209216,209502,209136,209179,209784,209761,209528,209433,209998,209951,210216,210230,209762,210331,210535,210859,211248,211329,211860,210546,210713,211018,211269,211235,211155,211488,211557,211581,211611,212326,212773,212868,212973,213487,209644,207829,208565,209929,210643,207093]
#y = [545664,545771,546335,546336,545772,545802,546587,546604,545994,546184,546565,546450,548163,547265,547267,545843,544960,544931,544674,544640,544871,544788,544976,544921,545133,543890,543895,544083,544120,543986,543993,544426,544399,541184,544018,544752,545378,544535,545056,545800,544763,544362,543711,543303,542578,541846,541194,543600,543783,544041,543194,543222,544042,543795,543963,544256,543730,543345,545015,544841,545599,546032,545318]
office = [209282, 545618]

def get_x():
    return x

def get_y():
    return y

def get_office():
    return office


def get_adjusted_value(value):
    return math.floor(value / 10)

def get_distance(x1, y1, x2, y2):
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return get_adjusted_value(distance)

def get_distance_list(x_list, y_list, index):
        distance_list = []

        for i in range(len(x_list)):
            distance = get_distance(x_list[i], y_list[i], x_list[index], y_list[index])
            distance_list.append(distance)
        
        return distance_list

def get_distance_matrix(x_list=x, y_list=y):
    distance_matrix = []

    for i in range(len(x_list)):
        distance_list = get_distance_list(x_list, y_list, i)
        distance_matrix.append(distance_list)

    return distance_matrix

def get_min_distance_index_from_office():
    x_list = x.copy()
    y_list = y.copy()
    x_list.append(office[0])
    y_list.append(office[1])

    office_index = len(x_list)-1

    distance_list = get_distance_list(x_list, y_list, office_index)
    distance_list.pop()

    min_index = 0
    min_distance = distance_list[min_index]

    for i in range(len(distance_list)):
        if distance_list[i] < min_distance:
            min_distance = distance_list[i]
            min_index = i
    
    #print(min_index, min_distance)
    return min_index

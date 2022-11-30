import matplotlib.pyplot as plt

img_margin = 0.2
data_reduce = 0.01

def get_reduced_axis_list(axis_list):
    return list(map(lambda x: x, axis_list))

def get_img_size_list(x, y):
    x_diff,y_diff = max(x)-min(x), max(y)-min(y)
    img_size = [
        min(x) - x_diff * img_margin, 
        max(x) + x_diff * img_margin, 
        min(y) - y_diff * img_margin, 
        max(y) + y_diff * img_margin, 
        ]
    return img_size

def draw(x, y, office):
    x = get_reduced_axis_list(x)
    y = get_reduced_axis_list(y)
    office = get_reduced_axis_list(office)

    img = plt.imread("bg.jpeg")
    plt.imshow(img, extent=get_img_size_list(x, y))
    plt.scatter(x, y)
    plt.scatter(office[0], office[1])
    plt.show()

def draw_model(x, y, office, route_list):
    for i in range(len(route_list)):
        x_route, y_route = [], []

        for depot in route_list[i]:
            depot_index = depot-1
            print(depot_index, x[depot_index], y[depot_index])
            x_route.append(x[depot_index])
            y_route.append(y[depot_index])

        x_route = get_reduced_axis_list(x_route)
        y_route = get_reduced_axis_list(y_route)
        
        plt.plot(x_route, y_route, linestyle='solid', label='route %d'%i)

    img = plt.imread("bg.jpeg")
    plt.imshow(img, extent=get_img_size_list(x, y))
    office = get_reduced_axis_list(office)
    plt.scatter(office[0], office[1])
    plt.show()
import matplotlib.pyplot as plt

img_margin = 0.2
data_reduce = 0.01

def get_img_size_list(x, y):
    x_diff,y_diff = max(x)-min(x), max(y)-min(y)
    img_size = [
        min(x) - x_diff * img_margin, 
        max(x) + x_diff * img_margin, 
        min(y) - y_diff * img_margin, 
        max(y) + y_diff * img_margin, 
        ]
    return img_size

def plt_add_office(office):
    plt.scatter(office[0], office[1], color="white", edgecolor="black", zorder=100, marker='D')

def plt_add_depot(x, y, depot_index):
    plt.scatter(x[depot_index], y[depot_index], color="white", edgecolor="black", zorder=100)


def draw(x, y, office, use_only=True):
    img = plt.imread("bg.jpeg")
    plt.imshow(img, extent=get_img_size_list(x, y))
    plt_add_office(office)
    plt.scatter(x, y)
    if use_only:
        plt.show()


def draw_model(x, y, office, route_list):
    for i in range(len(route_list)):
        x_route, y_route = [], []

        for node in route_list[i]:
            x_route.append(x[node])
            y_route.append(y[node])

        plt.plot(x_route, y_route, linestyle='solid', label='route %d'%i)

    img = plt.imread("bg.jpeg")
    plt_add_office(office)

    plt.imshow(img, extent=get_img_size_list(x, y))
    
    plt.show()

def draw_all(x, y, office, route_list, depot_index):
    plt.subplot(1,2,1)
    draw(x,y,office, False)
    plt.subplot(1,2,2)
    plt_add_depot(x, y, depot_index)
    draw_model(x, y, office,route_list)

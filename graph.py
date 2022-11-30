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

def plt_add_office(office_xy):
    plt.scatter(office_xy[0], office_xy[1], color="white", edgecolor="black", marker='D')

def plt_add_depot(x, y, depot_index):
    plt.scatter(x[depot_index], y[depot_index], color="white", edgecolor="black")

def plt_model(x, y, office_xy):
    img = plt.imread("bg.jpeg")
    plt.imshow(img, extent=get_img_size_list(x, y))
    plt_add_office(office_xy)
    plt.scatter(x, y, color="gray", edgecolor="white")

def plt_model_vrp(x, y, office_xy, route_list, depot_index):
    plt_model(x, y, office_xy)
    plt_add_depot(x, y, depot_index)

    for i in range(len(route_list)):
        x_route, y_route = [], []

        for node in route_list[i]:
            x_route.append(x[node])
            y_route.append(y[node])

        plt.plot(x_route, y_route, linestyle='solid', zorder=0, label='route %d'%i)
    
    plt.show()

def draw(x, y, office_xy, route_list, depot_index):
    plt.subplot(1,2,1)
    plt_model(x,y,office_xy)
    plt.subplot(1,2,2)
    plt_model_vrp(x, y, office_xy,route_list, depot_index)
    plt.show()

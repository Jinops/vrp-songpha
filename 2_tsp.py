import matplotlib.pyplot as plt

"""Simple Travelling Salesperson Problem (TSP) on a circuit board."""

import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def get_my_data():
    x = (-2.064791527,-1.628933174,-1.741736623,-1.708663361,-1.273986197,-0.909589715,-0.767256567,-0.74835756,-0.479046708,-0.218594766,-0.310136832,0.077292814,0.552130369,0.037132424,0.049534898,-0.126462106,-1.813789088,-1.790755923,-1.318871339,-1.275167384,-0.515663535,-0.533971948,-0.339666531,-0.318995742,-0.150085865,-0.36624326,-0.340847719,0.016461635,0.002877974,-0.134730422,-0.190836849,0.142848745,0.115090829,0.271598232,0.279866547,0.003468568,0.339516539,0.459997709,0.651350157,0.881091212,0.928929324,1.242534724,0.466494243,0.565123436,0.745254598,0.893493686,0.87341349,0.826165973,1.022833766,1.06358475,1.077759005,1.095476824,1.517751515,1.781747021,1.837853449,1.899865816,2.203431118,-0.066221521,-1.138149583,-0.703472418,0.102097761,0.523781858,-1.572826747)
    y = (0.668334236,0.746976204,1.161500224,1.162235196,0.747711176,0.769760326,1.346713084,1.359207602,0.910874886,1.050519502,1.330543707,1.246021966,2.50502843,1.845023874,1.846493817,0.799894164,0.150914182,0.129600004,-0.059287714,-0.084276751,0.085501704,0.024499056,0.162673729,0.122250287,0.278064281,-0.635505501,-0.631830643,-0.493655969,-0.466462018,-0.564948221,-0.559803419,-0.241560688,-0.261404923,-2.624338831,-0.541429128,-0.001959924,0.458132339,-0.161448776,0.221471462,0.768290382,0.006124764,-0.288598874,-0.767065429,-1.066933869,-1.599788328,-2.137787588,-2.616989114,-0.848647284,-0.714147469,-0.524524779,-1.147045781,-1.126466574,-0.523789808,-0.705327809,-0.581852569,-0.366505871,-0.753100968,-1.036065059,0.191337624,0.063452554,0.620561077,0.938803809,0.414034039)

    data = list(map(lambda x,y:(x,y), x, y))
    return data

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    # Locations in block units
    
    data['locations'] = get_my_data()
    # yapf: disable
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

def compute_euclidean_distance_matrix(locations):
    """Creates callback to return distance between points."""
    distances = {}
    for from_counter, from_node in enumerate(locations):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_counter:
                distances[from_counter][to_counter] = 0
            else:
                # Euclidean distance
                distances[from_counter][to_counter] = (int(
                    math.hypot((from_node[0] - to_node[0]),
                               (from_node[1] - to_node[1]))))
    return distances


def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print('Objective: {}'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Objective: {}m\n'.format(route_distance)


def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    distance_matrix = compute_euclidean_distance_matrix(data['locations'])

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(manager, routing, solution)


if __name__ == '__main__':
    main()
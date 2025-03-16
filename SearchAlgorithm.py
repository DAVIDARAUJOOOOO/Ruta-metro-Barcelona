# This file contains all the required routines to make an A* search algorithm.
#
__author__ = '1671077'
# _________________________________________________________________________________________
# Intel.ligencia Artificial
# Curs 2023 - 2024
# Universitat Autonoma de Barcelona
# _______________________________________________________________________________________

from SubwayMap import *
from utils import *
import os
import math
import copy


INF=9999
def expand(path, map):
    
    llista_path=[]
    ultim=path.last
    for i in map.connections[ultim].keys():
        auxiliar=copy.deepcopy(path)
        auxiliar.add_route(i)
        llista_path.append(auxiliar)
    return llista_path

    """
     It expands a SINGLE station and returns the list of class Path.
     Format of the parameter is:
        Args:
            path (object of Path class): Specific path to be expanded
            map (object of Map class):: All the information needed to expand the node
        Returns:
            path_list (list): List of paths that are connected to the given path.
    """
    


def remove_cycles(path_list):
   llista_path=[]
   for i in path_list:
       trobat=False
       for j in range (len(i.route)-1):
            if (i.last==i.route[j]):
               trobat=True 
       if(not trobat):
           llista_path.append(i)
   return llista_path     


"""
     It removes from path_list the set of paths that include some cycles in their path.
     Format of the parameter is:
        Args:
            path_list (LIST of Path Class): Expanded paths
        Returns:
            path_list (list): Expanded paths without cycles.
    """
    
    


def insert_depth_first_search(expand_paths, list_of_path):
    
    """
    
     expand_paths is inserted to the list_of_path according to DEPTH FIRST SEARCH algorithm
     Format of the parameter is:
        Args:
            expand_paths (LIST of Path Class): Expanded paths
            list_of_path (LIST of Path Class): The paths to be visited
        Returns:
            list_of_path (LIST of Path Class): List of Paths where Expanded Path is inserted
    """
    llista=[]
    list_of_path.pop(0)
    llista=expand_paths+list_of_path
    return llista
    


def depth_first_search(origin_id, destination_id, map):
    """
     Depth First Search algorithm
     Format of the parameter is:
        Args:
            origin_id (int): Starting station id
            destination_id (int): Final station id
            map (object of Map class): All the map information
        Returns:
            list_of_path[0] (Path Class): the route that goes from origin_id to destination_id
    """
    path=[Path([origin_id])]
    while(path[0].last!=destination_id and len(path)!=0):
        C=path[0]
        E=expand(C, map)
        E=remove_cycles(E)
        path=insert_depth_first_search(E, path)
    if(len(path)!=0):
        return path[0]
    else:
        print("NO EXISTEIX SOLUCIÓ")



def insert_breadth_first_search(expand_paths, list_of_path):
    """
        expand_paths is inserted to the list_of_path according to BREADTH FIRST SEARCH algorithm
        Format of the parameter is:
           Args:
               expand_paths (LIST of Path Class): Expanded paths
               list_of_path (LIST of Path Class): The paths to be visited
           Returns:
               list_of_path (LIST of Path Class): List of Paths where Expanded Path is inserted
    """
    llista=[]
    list_of_path.pop(0)
    llista=list_of_path+expand_paths
    return llista

def breadth_first_search(origin_id, destination_id, map):
    """
     Breadth First Search algorithm
     Format of the parameter is:
        Args:
            origin_id (int): Starting station id
            destination_id (int): Final station id
            map (object of Map class): All the map information
        Returns:
            list_of_path[0] (Path Class): The route that goes from origin_id to destination_id
    """
    path=[Path([origin_id])]
    while(path[0].last!=destination_id and len(path)!=0):
        C=path[0]
        E=expand(C, map)
        E=remove_cycles(E)
        path=insert_breadth_first_search(E, path)
    if(len(path)!=0):
        return path[0]
    else:
        print("NO EXISTEIX SOLUCIÓ")




def calculate_cost(expand_paths, map, type_preference):
    """
         Calculate the cost according to type preference
         Format of the parameter is:
            Args:
                expand_paths (LIST of Paths Class): Expanded paths
                map (object of Map class): All the map information
                type_preference: INTEGER Value to indicate the preference selected:
                                0 - Adjacency
                                1 - minimum Time
                                2 - minimum Distance
                                3 - minimum Transfers
            Returns:
                expand_paths (LIST of Paths): Expanded path with updated cost
    """
    if (type_preference==0):
        for path in expand_paths:
            path.update_g(1)
            
    elif(type_preference==1):
        for path in expand_paths:
            penultim=path.penultimate
            ultim=path.last
            temps=map.connections[penultim][ultim]
            path.update_g(temps)
        
    elif(type_preference==2):
        for path in expand_paths:
            penultim=path.penultimate
            ultim=path.last
            if (map.stations[penultim]['line'] == map.stations[ultim]['line']):    
                path.update_g(map.connections[penultim][ultim]*map.velocity[map.stations[ultim]['line']])
                    
                
    elif(type_preference==3):
        for path in expand_paths:
            penultim=path.penultimate
            ultim=path.last
            if(map.stations[penultim]['line']!=map.stations[ultim]['line']):
                path.update_g(1)
                
    return (expand_paths)
    


def insert_cost(expand_paths, list_of_path):
    """
        expand_paths is inserted to the list_of_path according to COST VALUE
        Format of the parameter is:
           Args:
               expand_paths (LIST of Path Class): Expanded paths
               list_of_path (LIST of Path Class): The paths to be visited
           Returns:
               list_of_path (LIST of Path Class): List of Paths where expanded_path is inserted according to cost
    """
    list_of_path.pop(0)
    sorted_path=list_of_path+expand_paths
    return(sorted (sorted_path, key=lambda x:x.g))


def uniform_cost_search(origin_id, destination_id, map, type_preference):
    """
     Uniform Cost Search algorithm
     Format of the parameter is:
        Args:
            origin_id (int): Starting station id
            destination_id (int): Final station id
            map (object of Map class): All the map information
            type_preference: INTEGER Value to indicate the preference selected:
                            0 - Adjacency
                            1 - minimum Time
                            2 - minimum Distance
                            3 - minimum Transfers
        Returns:
            list_of_path[0] (Path Class): The route that goes from origin_id to destination_id
    """
    path=[Path([origin_id])]
    while(path[0].last!=destination_id and len(path)!=0):
        C=path[0]
        E=expand(C, map)
        E=remove_cycles(E)
        E=calculate_cost(E,map,type_preference)
        path=insert_cost(E, path)
    if(len(path)!=0):
        return path[0]
    else:
        print("NO EXISTEIX SOLUCIÓ")


def calculate_heuristics(expand_paths, map, destination_id, type_preference):
    """
     Calculate and UPDATE the heuristics of a path according to type preference
     WARNING: In calculate_cost, we didn't update the cost of the path inside the function
              for the reasons which will be clear when you code Astar (HINT: check remove_redundant_paths() function).
     Format of the parameter is:
        Args:
            expand_paths (LIST of Path Class): Expanded paths
            map (object of Map class): All the map information
            destination_id (int): Final station id
            type_preference: INTEGER Value to indicate the preference selected:
                            0 - Adjacency
                            1 - minimum Time
                            2 - minimum Distance
                            3 - minimum Transfers
        Returns:
            expand_paths (LIST of Path Class): Expanded paths with updated heuristics
    """
    if (type_preference==0):
        for path in expand_paths:
            ultim=path.last
            
            if(ultim!=destination_id):
                path.update_h(1)
            else:
                path.update_h(0)
                
    elif(type_preference==1):
        for path in expand_paths:
            ultim=path.last
            coord_ultim=[map.stations[ultim]['x'],map.stations[ultim]['y']]
            destination=[map.stations[destination_id]['x'],map.stations[destination_id]['y']]
            distancia=euclidean_dist(coord_ultim,destination)
            velocitat=max(map.velocity.values())
            temps=distancia/velocitat
            path.update_h(temps)
            
    elif(type_preference==2):
        for path in expand_paths:
            ultim=path.last
            coord_ultim=[]
            destination=[]
            coord_ultim.append(map.stations[ultim]['x'])
            coord_ultim.append(map.stations[ultim]['y'])
            destination.append(map.stations[destination_id]['x'])
            destination.append(map.stations[destination_id]['y'])
            distancia=euclidean_dist(coord_ultim, destination)
            path.update_h(distancia)
            
           
    elif(type_preference==3):
        for path in expand_paths:
            ultim=path.last
            if (map.stations[ultim]['line']!=map.stations[destination_id]['line']):
                path.update_h(1)
            else:
                path.update_h(0)
                
    return(expand_paths)
            
            


def update_f(expand_paths):
    """
      Update the f of a path
      Format of the parameter is:
         Args:
             expand_paths (LIST of Path Class): Expanded paths
         Returns:
             expand_paths (LIST of Path Class): Expanded paths with updated costs
    """
    for path in expand_paths:
        path.update_f()
    return(expand_paths)


def remove_redundant_paths(expand_paths, list_of_path, visited_stations_cost):
    """
      It removes the Redundant Paths. They are not optimal solution!
      If a station is visited and have a lower g-cost at this moment, we should remove this path.
      Format of the parameter is:
         Args:
             expand_paths (LIST of Path Class): Expanded paths
             list_of_path (LIST of Path Class): All the paths to be expanded
             visited_stations_cost (dict): All visited stations cost
         Returns:
             new_paths (LIST of Path Class): Expanded paths without redundant paths
             list_of_path (LIST of Path Class): list_of_path without redundant paths
             visited_stations_cost (dict): Updated visited stations cost
    """
    for path in expand_paths:
        ultim=path.last
        cost=path.g
        if(ultim in visited_stations_cost):
            if(cost>=visited_stations_cost[ultim]):
                expand_paths.remove(path)
            else:
                visited_stations_cost[ultim]=cost
                for i in list_of_path:
                    for k in i.route:
                        if ultim==k:
                            list_of_path.remove(i)
        else:
            visited_stations_cost[ultim]=cost
            
    return expand_paths, list_of_path, visited_stations_cost

def insert_cost_f(expand_paths, list_of_path):
    """
        expand_paths is inserted to the list_of_path according to f VALUE
        Format of the parameter is:
           Args:
               expand_paths (LIST of Path Class): Expanded paths
               list_of_path (LIST of Path Class): The paths to be visited
           Returns:
               list_of_path (LIST of Path Class): List of Paths where expanded_path is inserted according to f
    """
    list_of_path.pop(0)
    sorted_list=list_of_path+expand_paths
    return(sorted(sorted_list, key=lambda x:x.f))


def distance_to_stations(coord, map):
    diccionari1={}
    for i,k in map.stations.items():
        stations=[]
        stations.append(k["x"])
        stations.append(k["y"])
        diccionari1[i]=euclidean_dist(coord,stations)
    diccionari2=dict(sorted(diccionari1.items(),key=lambda item:(item[1], item[0])))
    return diccionari2
    """
        From coordinates, it computes the distance to all stations in map.
        Format of the parameter is:
        Args:
            coord (list):  Two REAL values, which refer to the coordinates of a point in the city.
            map (object of Map class): All the map information        Returns:
            (dict): Dictionary containing as keys, all the Indexes of all the stations in the map, and as values, the
            distance between each station and the coord point
    """
    


def Astar(origin_id, destination_id, map, type_preference):
    """
     A* Search algorithm
     Format of the parameter is:
        Args:
            origin_id (int): Starting station id
            destination_id (int): Final station id
            map (object of Map class): All the map information
            type_preference: INTEGER Value to indicate the preference selected:
                            0 - Adjacency
                            1 - minimum Time
                            2 - minimum Distance
                            3 - minimum Transfers
        Returns:
            list_of_path[0] (Path Class): The route that goes from origin_id to destination_id
    """
    path=[Path([origin_id])]
    stations_cost={}
    for i in range(len(map.stations)):
        stations_cost[i]=INF
    while(path[0].last!=destination_id and len(path)!=0):
        C=path[0]
        E=expand(C, map)
        E=remove_cycles(E)
        E=calculate_cost(E,map,type_preference)
        E=calculate_heuristics(E,map,destination_id,type_preference)
        E=update_f(E)
        E, path,stations_cost= remove_redundant_paths(E, path, stations_cost)
        path=insert_cost_f(E, path)
    if(len(path)!=0):
        return path[0]
    else:
        print("NO EXISTEIX SOLUCIÓ")


def Astar_improved(origin_coord, destination_coord, map):
    
    map.add_station(0,"origin",0,origin_coord[0],origin_coord[1])
    map.add_station(-1,"destination",0, destination_coord[0], destination_coord[1])
    temps_origen=distance_to_stations(origin_coord, map)
    temps_desti=distance_to_stations(destination_coord, map)
    for i, j in temps_origen.items():
        temps_origen[i]=j/5
    for i, j in temps_desti.items():
        temps_desti[i]=j/5
    map.connections[0]=temps_origen
    map.connections[-1]=temps_desti
    for i in temps_origen.keys():
        map.connections[i][0] = temps_origen[i]
        map.connections[i][-1] = temps_desti[i]
    return Astar(0,-1,map,1)
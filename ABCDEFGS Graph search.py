from collections import deque
def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])  # Queue stores (current node, path taken) # O(1)
    visited = set([start])  # Mark node as visited # O(1)

    while queue: # O(V)
        vertex, path = queue.popleft() # grabs graph to check based on input # O(1)
        if vertex == end: # check of that node is the "end" node # O(1)
            return path  # Return first path found # O(1)

        for neighbor in graph.get(vertex, []): #get adjacent nodes # O(adjacent(vertex))
            if neighbor not in visited: # check if visited # O(1)
                visited.add(neighbor) # O(1)
                queue.append((neighbor, path + [neighbor])) #add back to queue # O(V)

    return None  # If no path


def main():
    graph = { # nodes and its adjacent # O(1)
        'A': ['S', 'B'],
        'B': ['A', 'C'],
        'C': ['S', 'D'],
        'D': ['S', 'C', 'F', 'G'],
        'E': ['S', 'F', 'G'],
        'F': ['E', 'D', 'G'],
        'G': ['E', 'D', 'F'],
        'S': ['A', 'C', 'D', 'E']
    }

    try:
        start = input("Enter the starting vertex: ").strip().upper() #uppercase user input # O(1)
        end = input("Enter the ending vertex: ").strip().upper() # O(1)
    except:
        return

    if start not in graph or end not in graph: # O(1)
        print("Invalid input!") # O(1)
        return

    shortest_path = bfs_shortest_path(graph, start, end) #set variables after algorithm for use # O(1)
    if shortest_path:
        print("Shortest path from {} to {} is: {}".format(start, end, " --> ".join(shortest_path))) # O(1)
    else:
        print("No path found")

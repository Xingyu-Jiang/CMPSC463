from DecisionMazeAdventure import *


def main():
    # Usage
    maze = Maze()
    maze.generate_maze()
    graph_representation = maze.to_graph()
    for key, value in graph_representation.items():
        print(key, ":", value)

    # print(graph_representation)
    maze.print_edges()

    # Test shortest path from node 1 to node 6
    path = maze.shortest_path(1, 6)
    if path:
        print(f"Shortest path from node 1 to node 6: {path}")
    else:
        print("No path found from node 1 to node 6")



if __name__ == "__main__":
    main()

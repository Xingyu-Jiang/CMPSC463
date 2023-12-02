from DecisionMazeAdventure import *

def main():
    maze_instance = Maze()
    maze_instance.generate_maze()
    maze_graph = maze_instance.maze_to_graph()

    # Print nodes with prompts
    for node, data in maze_graph.nodes(data=True):
        print(f"Node {node}: {data.get('prompt')}")

    # Print edges
    for edge in maze_graph.edges():
        print(f"Edge: {edge}")


if __name__ == "__main__":
    main()
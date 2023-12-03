from DecisionMazeAdventure import *
# Create a DecisionMazeAdventure instance
game = DecisionMazeAdventure()

# Generate the maze
game.start_game()

# Print edges
game.maze.print_edges()
print()

# Find the shortest path between nodes 1 and 12
shortest_path = game.maze.shortest_path(1, 12)
print("Shortest Path:", shortest_path)
print()

# Perform breadth-first search starting from node 1
bfs_result = game.maze.breath_first_search(1)
print("BFS Result:", bfs_result)
print()

# Perform depth-first search starting from node 1
dfs_result = game.maze.depth_first_search(1)
print("DFS Result:", dfs_result)
print()
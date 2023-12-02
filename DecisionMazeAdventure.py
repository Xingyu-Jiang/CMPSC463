from collections import deque


class MazeNode:
    def __init__(self):
        self.left_node = None
        self.right_node = None
        self.parent_node = None
        self.is_decision_node = False
        self.prompt = ""
        self.node_id = int()

    # Setter
    def set_left_node(self, node):
        self.left_node = node

    def set_right_node(self, node):
        self.right_node = node

    def set_parent_node(self, node):
        self.parent_node = node

    def set_decision_node(self, is_decision):
        self.is_decision_node = is_decision

    def set_prompt(self, prompt):
        self.prompt = prompt

    def set_node_id(self, node_id):
        self.node_id = node_id

    # Getter
    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node

    def get_parent_node(self):
        return self.parent_node

    def is_decision(self):
        return self.is_decision_node

    def get_prompt(self):
        return self.prompt

    def get_node_id(self):
        return self.node_id


def set_node_info(node, is_decision, prompt, node_id):
    node.set_decision_node(is_decision)
    node.set_prompt(prompt)
    node.set_node_id(node_id)


class Maze:
    def __init__(self):
        self.root_node = None

    def get_root_node(self):
        return self.root_node

    def set_root_node(self, node):
        self.root_node = node

    def generate_maze(self):
        node6 = MazeNode()
        node6.set_decision_node(False)
        node6.set_prompt("Node 6: End")
        node6.set_node_id(6)

        node7 = MazeNode()
        node7.set_decision_node(False)
        node7.set_prompt("Node 7: End")
        node7.set_node_id(7)

        node4 = MazeNode()
        node4.set_decision_node(True)
        node4.set_prompt("Node 4: left(node 6) or right (node 7)")
        node4.set_left_node(node6)
        node4.set_right_node(node7)
        node6.set_parent_node(node4)
        node7.set_parent_node(node4)
        node4.set_node_id(4)

        node5 = MazeNode()
        node5.set_decision_node(False)
        node5.set_prompt("Node 5: End")
        node5.set_node_id(5)

        node2 = MazeNode()
        node2.set_decision_node(False)
        node2.set_prompt("Node 2: End")
        node2.set_node_id(2)

        node3 = MazeNode()
        node3.set_decision_node(True)
        node3.set_prompt("Node 3: left(node 4) or right (node 5)")
        node3.set_left_node(node4)
        node3.set_right_node(node5)
        node4.set_parent_node(node3)
        node5.set_parent_node(node3)
        node3.set_node_id(3)

        node1 = MazeNode()
        node1.set_decision_node(True)
        node1.set_prompt("Node 1: left(node 2) or right(node 3)")
        node1.set_left_node(node2)
        node1.set_right_node(node3)
        node3.set_parent_node(node1)
        node2.set_parent_node(node1)
        node1.set_node_id(1)

        self.root_node = node1

    def to_graph(self):
        graph = {}

        def traverse(node):
            if node:
                graph[node.get_node_id()] = {
                    "prompt": node.get_prompt(),
                    "left_node": node.get_left_node().get_node_id() if node.get_left_node() else None,
                    "right_node": node.get_right_node().get_node_id() if node.get_right_node() else None,
                    "parent_node": node.get_parent_node().get_node_id() if node.get_parent_node() else None,
                    "is_decision_node": node.is_decision()
                }
                traverse(node.get_left_node())
                traverse(node.get_right_node())

        traverse(self.root_node)
        return graph

    def print_edges(self):
        graph = self.to_graph()
        for node_id, data in graph.items():
            left_node = data["left_node"]
            right_node = data["right_node"]
            parent_node = data["parent_node"]

            if left_node is not None:
                print(f"Edge: {node_id} -> {left_node}")
            if right_node is not None:
                print(f"Edge: {node_id} -> {right_node}")
            if parent_node is not None:
                print(f"Edge: {node_id} -> {parent_node}")

    def shortest_path(self, start_node_id, end_node_id):
        graph = self.to_graph()

        # Check if start_node_id or end_node_id not in the graph
        if start_node_id not in graph or end_node_id not in graph:
            return None

        visited = set()
        queue = deque([(start_node_id, [start_node_id])])

        while queue:
            current_node, path = queue.popleft()
            visited.add(current_node)

            if current_node == end_node_id:
                return path

            neighbors = [graph[current_node]['left_node'],
                         graph[current_node]['right_node'],
                         graph[current_node]['parent_node']]

            for neighbor in neighbors:
                if neighbor and neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return None


class DecisionMazeAdventure:
    def __init__(self):
        self.maze = Maze()
        self.endings = []
        self.path_taken = []

    def start_game(self):
        self.maze.generate_maze()
        self.path_taken.append(self.maze.root_node)

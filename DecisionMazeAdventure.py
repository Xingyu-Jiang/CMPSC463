import pickle


class MazeNode:
    def __init__(self):
        self.left_node = None
        self.right_node = None
        self.parent_node = None
        self.is_decision_node = False
        self.prompt = ""
        self.node_id = int()

    def get_left_node(self):
        return self.left_node

    def set_left_node(self, node):
        self.left_node = node

    def get_right_node(self):
        return self.right_node

    def set_right_node(self, node):
        self.right_node = node

    def get_parent_node(self):
        return self.parent_node

    def set_parent_node(self, node):
        self.parent_node = node

    def is_decision(self):
        return self.is_decision_node

    def set_decision_node(self, is_decision):
        self.is_decision_node = is_decision

    def get_prompt(self):
        return self.prompt

    def set_prompt(self, prompt):
        self.prompt = prompt

    def get_node_id(self):
        return self.node_id

    def set_node_id(self, node_id):
        self.node_id = node_id


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

        node7 = MazeNode()
        node7.set_decision_node(False)
        node7.set_prompt("Node 7: End")

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


class DecisionMazeAdventure:
    def __init__(self):
        self.maze = Maze()
        self.endings = []
        self.path_taken = []

    def start_game(self):
        self.maze.generate_maze()
        self.path_taken.append(self.maze.root_node)

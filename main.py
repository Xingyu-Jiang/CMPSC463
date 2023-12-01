import pickle

class MazeNode:
    def __init__(self):
        self.left_node = None
        self.right_node = None
        self.is_decision_node = False
        self.prompt = ""

    def get_left_node(self):
        return self.left_node

    def set_left_node(self, node):
        self.left_node = node

    def get_right_node(self):
        return self.right_node

    def set_right_node(self, node):
        self.right_node = node

    def is_decision(self):
        return self.is_decision_node

    def set_decision_node(self, is_decision):
        self.is_decision_node = is_decision

    def get_prompt(self):
        return self.prompt

    def set_prompt(self, prompt):
        self.prompt = prompt




class Maze:
    def __init__(self):
        self.root_node = None

    def get_root_node(self):
        return self.root_node

    def set_root_node(self, node):
        self.root_node = node

    def generate_maze(self):
        node7 = MazeNode()
        node7.set_prompt("You've reached End A.")

        node8 = MazeNode()
        node8.set_prompt("You've reached End B.")

        node4 = MazeNode()
        node4.set_decision_node(True)
        node4.set_prompt("Go left or right?")

        node5 = MazeNode()
        node5.set_prompt("You've reached End C.")

        node6 = MazeNode()
        node6.set_prompt("You've reached End D.")

        node3 = MazeNode()
        node3.set_decision_node(True)
        node3.set_prompt("Do you want to go left or right?")
        node3.set_left_node(node7)
        node3.set_right_node(node8)

        node2 = MazeNode()
        node2.set_decision_node(True)
        node2.set_prompt("Do you want to go left or right?")
        node2.set_left_node(node5)
        node2.set_right_node(node6)

        node1 = MazeNode()
        node1.set_decision_node(True)
        node1.set_prompt("Go left or right?")
        node1.set_left_node(node3)
        node1.set_right_node(node4)
        self.root_node = node1


class DecisionMazeAdventure:
    def __init__(self):
        self.maze = Maze()
        self.endings = []
    ''' 
        self.visitied_nodes=[]
        self.score = 0
    ''' 

    def start_game(self):
        '''
        try:
            with open('savegame.pkl', 'rb') as f:
                self.visited_nodes = pickle.load(f)
        except FileNotFoundError:
            pass
        '''

        self.maze.generate_maze()
        self.navigate_maze(self.maze.get_root_node())

    def navigate_maze(self, current_node):
        while True:

            '''
            self.visited_nodes.append(current_node)
            '''


            if current_node.is_decision():
                print(current_node.get_prompt())
                choice = input("Enter your choice (l/r/b), b for undo: ").lower()
                if choice == 'l':
                    current_node = current_node.get_left_node()
                elif choice == 'r':
                    current_node = current_node.get_right_node()

                '''    
                elif choice == 'b':
                    self.visited_nodes.pop()  # remove current node
                    current_node = self.visited_nodes.pop()  # set previous node as current'''

                else:
                    print("Invalid choice. Please choose again.")
                    continue
            else:
                self.endings.append(current_node.get_prompt())
                print(f"You've reached an ending: {current_node.get_prompt()}")
                # print(f"Your score: {self.score}")
                break
        '''
        # Save progress
        with open('savegame.pkl', 'wb') as f:
            pickle.dump(self.visited_nodes, f)  
        '''


def main():
    # Instantiate and start the game
    game = DecisionMazeAdventure()
    game.start_game()


if __name__ == "__main__":
    main()

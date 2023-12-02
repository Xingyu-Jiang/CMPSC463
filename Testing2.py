import tkinter as tk
from Testing import *


class MazeGUI:
    def __init__(self, master):
        self.master = master
        self.game = DecisionMazeAdventure()
        self.game.start_game()
        self.current_node = self.game.maze.get_root_node()

        self.master.title("Maze Game")

        self.label = tk.Label(master, text=self.current_node.get_prompt())
        self.label.pack()

        self.left_button = tk.Button(master, text="Left", command=self.go_left)
        self.left_button.pack(side=tk.LEFT)

        self.right_button = tk.Button(master, text="Right", command=self.go_right)
        self.right_button.pack(side=tk.LEFT)

        self.back_button = tk.Button(master, text="Back", command=self.go_back)
        self.back_button.pack(side=tk.LEFT)

    def go_left(self):
        self.navigate('l')

    def go_right(self):
        self.navigate('r')

    def go_back(self):
        self.navigate('b')

    def navigate(self, choice):
        if choice == 'b':
            if self.current_node.get_parent_node() is not None:
                temp = self.current_node
                self.current_node = temp.get_parent_node()
                self.update_prompt()
            else:
                print("Cannot backtrack further.")
        else:
            if choice in ['l', 'r']:
                next_node = self.current_node.get_left_node() if choice == 'l' else self.current_node.get_right_node()
                if next_node:
                    temp = next_node
                    self.current_node = temp
                    self.game.path_taken.append(self.current_node)
                    self.update_prompt()

    def update_prompt(self):
        if self.current_node.is_decision():
            self.label.config(text=self.current_node.get_prompt())
        else:
            self.label.config(text=f"You've reached an ending: {self.current_node.get_prompt()}")


def main():
    root = tk.Tk()
    maze_gui = MazeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

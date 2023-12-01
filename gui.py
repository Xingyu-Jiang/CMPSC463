import tkinter as tk
import maze


class MazeGUI:
    def __init__(self, maze):
        self.maze = maze
        self.current_node = maze.root_node

        self.window = tk.Tk()
        self.prompt_text = tk.StringVar()
        self.prompt_label = tk.Label(self.window, textvariable=self.prompt_text)
        self.left_button = tk.Button(self.window, text="Go left", command=self.go_left)
        self.right_button = tk.Button(self.window, text="Go right", command=self.go_right)
        self.restart_button = tk.Button(self.window, text="Start over", command=self.start_over)

        self.prompt_label.pack()
        self.left_button.pack()
        self.right_button.pack()
        self.restart_button.pack()

        self.update_prompt()

    def go_left(self):
        if self.current_node.get_left_node():
            self.current_node = self.current_node.get_left_node()
            self.update_prompt()

    def go_right(self):
        if self.current_node.get_right_node():
            self.current_node = self.current_node.get_right_node()
            self.update_prompt()

    def start_over(self):
        self.current_node = self.maze.root_node
        self.update_prompt()

    def update_prompt(self):
        self.prompt_text.set(self.current_node.get_prompt())

    def run(self):
        self.window.mainloop()

"""
# need to finish up
maze = main.Maze()
gui = MazeGUI(maze)
gui.run()
"""
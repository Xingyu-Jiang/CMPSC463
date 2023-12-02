import tkinter as tk
from tkinter import messagebox
from DecisionMazeAdventure import *


class MazeGUI:
    def __init__(self, master):
        self.master = master
        self.game = DecisionMazeAdventure()
        self.game.start_game()
        self.current_node = self.game.maze.get_root_node()

        self.master.title("Decision Maze Adventure")
        self.master.geometry("325x270")

        self.text_box = tk.Text(master, height=5, width=40)
        self.text_box.insert(tk.END, self.current_node.get_prompt())
        self.text_box.config(state=tk.DISABLED)
        self.text_box.grid(row=0, column=0, columnspan=3)

        self.left_button = tk.Button(master, text="<-- Left ", command=self.go_left)
        self.left_button.grid(row=1, column=0, padx=10, pady=10)

        self.back_button = tk.Button(master, text=" - Back - ", command=self.go_back)
        self.back_button.grid(row=1, column=1, padx=10, pady=10)

        self.right_button = tk.Button(master, text=" Right -->", command=self.go_right)
        self.right_button.grid(row=1, column=2, padx=10, pady=10)

        self.show_path_button = tk.Button(master, text=" Show Shortest Path ", command=self.show_shortest_path)
        self.show_path_button.grid(row=2, column=0, columnspan=3, pady=10)

        self.show_path_button = tk.Button(master, text=" Show BFS ", command=self.show_breath_first_search)
        self.show_path_button.grid(row=3, column=0, columnspan=3, pady=10)

        self.show_dfs_button = tk.Button(master, text=" Show DFS ", command=self.show_depth_first_path)
        self.show_dfs_button.grid(row=4, column=0, columnspan=3, pady=10)

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
            self.text_box.config(state=tk.NORMAL)
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, self.current_node.get_prompt())
            self.text_box.config(state=tk.DISABLED)
        else:
            self.text_box.config(state=tk.NORMAL)
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, self.current_node.get_prompt())
            self.text_box.config(state=tk.DISABLED)

    def show_shortest_path(self):
        start_node_id = 1
        end_node_id = 6
        shortest_path = self.game.maze.shortest_path(start_node_id, end_node_id)

        if shortest_path:
            path_str = ' -> '.join(str(node_id) for node_id in shortest_path)
            tk.messagebox.showinfo("Shortest Path", f"Shortest Path: {path_str}", icon='info')
        else:
            tk.messagebox.showinfo("Shortest Path", "No valid path found.", icon='info')

    def show_breath_first_search(self):
        start_node_id = 1
        breath_first_search = self.game.maze.breath_first_search(start_node_id)

        if breath_first_search:
            path_str = ' -> '.join(str(node_id) for node_id in breath_first_search)
            tk.messagebox.showinfo("Breath First Search", f"Breath First Search: {path_str}", icon='info')
        else:
            tk.messagebox.showinfo("Breath First Search", "No valid path found.", icon='info')

    def show_depth_first_path(self):
        start_node_id = 1
        depth_first_path = self.game.maze.depth_first_search(start_node_id)

        if depth_first_path:
            path_str = ' -> '.join(str(node_id) for node_id in depth_first_path)
            tk.messagebox.showinfo("Depth-First Path", f"Depth-First Path: {path_str}", icon='info')
        else:
            tk.messagebox.showinfo("Depth-First Path", "No path found", icon='info')


def main():
    root = tk.Tk()
    MazeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

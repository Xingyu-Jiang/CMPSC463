# Decision-Making Maze

## Project Goals
The primary objective of Decision-Making Maze is to create a simple text-based adventure game that serves as a foundation for users to develop their own Choose Your Own Adventure-style games.

## Significance of the Project
This application, developed within a relatively short period, doesn't aim to revolutionize or entertain extensively. Rather, it's intended to inspire individuals encountering it to embark on their journey of creating simple applications or games that contribute positively to others' well-being. For us, as developers, it was a fulfilling experience turning a rough idea into reality, bringing joy and satisfaction as each function began working after hours of troubleshooting.

## Installation and Usage Instructions
### Recommended Software
- GitHub Desktop
- PyCharm
- Python 3.10

### Installation
1. Ensure Python 3.10 is installed.
2. Clone the repository.
3. Install necessary libraries (such as tkinter if not available).
4. Run the Python script MazeGUI.py.
5. Follow the GUI instructions to interact with the prebuilt maze sample.

### Usage
- Launch the application to open the graphical interface.
- Ensure tkinter is installed if the interface doesn't appear.
- Verify that DecisionMazeAdventure.py and MazeGUI.py are in the same directory.
- Use the provided buttons ("<-- Left", " - Back -", " Right -->") to navigate within the maze.
- Explore additional functionalities like finding the shortest path, BFS, and DFS using the corresponding buttons.

## Code Structure
### UML Diagram
![MazeUML](MazeUML.png)

### Explanations
- `MazeNode`: Represents nodes in the maze.
- `Maze`: Generates and operates on the maze structure.
- `DecisionMazeAdventure`: Manages game aspects.
- `MazeGUI`: Creates the graphical interface for maze navigation.

## List of Functionalities and Test Results
### Functionalities
- `MazeNode` Class: Methods for setting and getting node attributes.
- `Maze` Class: Maze generation, traversal methods (shortest path, BFS, DFS), and printing edges.
- `DecisionMazeAdventure` Class: Game instance initialization and path recording.
- `MazeGUI`: Methods for setting up tkinter GUI elements and interactions.

## Discussion and Conclusions
We identified two key issues in our application that we aim to address with more time. Firstly, the manual maze creation process is tedious; we're exploring a solution using a function to parse maze data from a CSV file. Secondly, to enhance engagement, we plan to introduce a point-based system and create more complex mazes, offering a specific path for traversal.
Throughout development, we applied knowledge gained from previous assignments, notably graph traversal algorithms (BFS, DFS) used for finding the shortest path. Our choice of a tree data structure was influenced by the realization that, akin to representing a graph as an array of linked lists, something similar to a linked list could also be utilized in maze creation.


Polyline x Offset App
=====================

Overview
--------
The Polyline x Offset App is a Python-based application designed to visualize a polyline from a CSV file and calculate geometric properties interactively. The application allows users to:
- Load a polyline from a CSV file containing X and Y coordinates.
- Visualize the polyline and interact with it by clicking on the graph.
- Calculate the offset (distance from a user-defined point to the closest point on the polyline).
- Calculate the station (cumulative distance along the polyline from the start to the closest point).
- Display these metrics in the graph's legend.

The project is structured into two main modules:
- ui.py: Handles the graphical user interface (GUI) using Tkinter.
- backend.py: Manages data loading, calculations, and graph generation using Pandas, NumPy, and Matplotlib.

Features
--------
- Load CSV: Import a CSV file with two columns (X and Y coordinates) to define the polyline.
- Interactive Graph: Visualize the polyline and click anywhere on the graph to calculate the offset and station.
- Visual Feedback:
  - The polyline is displayed as a solid line with points (-o).
  - The offset is shown as a dashed black line (--k) with its value in the legend.
  - The station is plotted as a blue line (-b) up to the closest point, with its value in the legend.
  - The user point and closest point are marked with red (ro) and green (go) dots, respectively.
- Metrics Display: The total polyline size, offset, and station are displayed in the graph's legend after interaction.

Requirements
------------
- Python 3.6+ (Tested with Python 3.11 in Anaconda environment)
- Operating System: Windows (can be adapted for Linux/macOS with minor changes)

Dependencies
------------
The project relies on the following Python libraries:
- tkinter: For the graphical user interface (GUI). Included with Python.
- pandas: For loading and processing CSV files.
- matplotlib: For generating interactive graphs.
- numpy: For numerical calculations (e.g., Euclidean distances).

Installation
------------
1. Set Up Anaconda Environment
   - Install Anaconda if you haven't already: https://www.anaconda.com/products/distribution.
   - Open Anaconda Prompt and create a new environment.
   - Activate the environment.

2. Install Dependencies
   - Install the required libraries in the created environment:
     pip install pandas matplotlib numpy
   - Tkinter is included with Python, so no additional installation is needed.

3. Clone or Download the Project
   - If using Git, clone the repository:
     git clone <repository-url>
     cd polyline-offset-app
   - Alternatively, download the project files (ui.py and backend.py) and place them in a folder.

Usage
-----
1. Prepare the CSV File
   - The application expects a CSV file (e.g., polyline_sample.csv) with at least two columns containing X and Y coordinates of the polyline points.
   - Example CSV format:
     X,Y
     0,0
     3,4
     6,0

2. Run the Application
   - Navigate to the project directory in the Anaconda Prompt:
   - Run the application:
     python ui.py

3. Interact with the Application
   - A window titled "Polyline x Offset App" will open.
   - Click "Load CSV" to select your CSV file.
   - The name of the loaded file will appear below the button.
   - Click "Generate Graph" to display the polyline in a Matplotlib window.
   - Click anywhere on the graph to:
     - Mark a user point (red dot).
     - Calculate and display the closest point on the polyline (green dot).
     - Show the offset (distance from the user point to the closest point) as a dashed black line.
     - Show the station (cumulative distance along the polyline to the closest point) as a blue line, ending at the closest point.
   - The legend will display the polyline size, offset, and station values.

Generating an Executable
------------------------
To create a standalone executable (.exe) for Windows, you can use PyInstaller:

1. Install PyInstaller in your environment:
   pip install pyinstaller
2. Generate the executable:
   pyinstaller --onefile --windowed --hidden-import=tkinter --hidden-import=matplotlib --hidden-import=matplotlib.backends.backend_tkagg ui.py
3. Find the executable (ui.exe) in the dist/ folder.
4. Run ui.exe to use the application without needing Python installed.

Project Structure
-----------------
- ui.py: Contains the Tkinter-based GUI, including buttons to load the CSV and generate the graph.
- backend.py: Handles data loading, calculations (offset and station), and graph generation.



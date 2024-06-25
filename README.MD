# Hybrid Dijkstra's and Bellman-Ford Algorithms

This Python project implements a sequential hybrid approach combining Dijkstra's and Bellman-Ford algorithms for finding shortest paths in graphs. It allows users to either generate a new graph with specified nodes and edges or use prepared graphs from a dataset or any other source.

## Project Structure

```
.
├── LICENSE
├── README.md
├── decorators.py
├── graph_parser.py
├── main.py
├── requirements.txt
├── sample_filepaths.py
└── sample_graph_generator.py
```

### Files:

- **`decorators.py`**: Contains decorators for measuring execution time and handling errors.
- **`graph_parser.py`**: Parses graph data from files.
- **`main.py`**: Main script where users can choose to generate a new graph or use a prepared graph to apply the sequential hybrid algorithm.
- **`requirements.txt`**: Contains the required Python packages. (Note: This file is empty as all packages used are standard built-in.)
- **`sample_filepaths.py`**: Template file for setting dataset paths.
- **`sample_graph_generator.py`**: Generates random graphs for testing purposes.

## Getting Started

### Prerequisites

Ensure Python 3.x is installed on your machine.

### Setting Up Your Dataset

1. **Rename the File**:
   - Rename `sample_filepaths.py` to `filepaths.py`.

2. **Set the Dataset Path**:
   - Open `filepaths.py` and set the `DATASET_PATH` variable to the location of your graph files.

## Usage

1. **Running the Program**:
   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Execute `main.py`:

     ```bash
     python main.py
     ```

2. **Choose Your Option**:
   - You will be prompted to choose:
     ```
     Choose an option:
     1. Generate a new graph
     2. Use a prepared graph
     Option:
     ```

3. **Generating a New Graph (`1`)**:
   - If you choose `1`, enter the number of nodes and edges for the new graph when prompted.

4. **Using a Prepared Graph (`2`)**:
   - If you choose `2`, enter the path to the folder containing the graph files and the name of the graph files.

5. **Running the Sequential Hybrid Algorithm**:
   - After choosing or generating a graph, enter the source vertex from which to compute shortest paths.

6. **Example Output**:
   - Upon completion, the program will display the computed distances from the source vertex to all other vertices.

### How It Works

- **`decorators.py`**: Provides decorators for measuring execution time and handling errors.
- **`graph_parser.py`**: Parses graph data from specified files.
- **`main.py`**: Offers an interactive interface for users to select graph generation or usage, applying the sequential hybrid algorithm accordingly.
- **`sample_graph_generator.py`**: Generates random graphs for testing purposes.

## Graph Data Sources

This project was developed using various graph datasets for testing and experimentation. You can use prepared datasets from the project, generate random graphs with `sample_graph_generator.py`, or integrate any other graph dataset of your choice.

- **9th DIMACS Implementation Challenge - Shortest Paths**:
  - Dataset downloaded from [DIMACS](https://www.diag.uniroma1.it/challenge9/download.shtml).
  - Provides various graph instances suitable for testing shortest path algorithms.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to explore and utilize this tool for analyzing various graph datasets or testing different scenarios with the hybrid Dijkstra's and Bellman-Ford algorithms. Whether for educational purposes or practical applications, we hope you find this project valuable and adaptable to your needs. Happy pathfinding with the hybrid algorithm!
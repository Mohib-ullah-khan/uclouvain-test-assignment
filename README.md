# Graph Algorithms Implementation

This repository contains two Python implementations of graph algorithms:

1. Matrix to List Conversion
2. Reachable Nodes Computation

## Project Structure

```
.
├── mat-to-list/
│   ├── mat_to_list.py
│   └── test_mat_to_list.py
└── reachable-nodes/
    ├── reachable.py
    └── test_reachable.py
```

## Matrix to List Conversion
The `mat-to-list` module converts an adjacency matrix representation of a graph to an adjacency list representation.


## Reachable Nodes Computation
The `reachable-nodes` module computes the set of nodes reachable from a given start node in a graph represented as an adjacency list.


## Testing
Both modules include test cases. You can run the tests using Python's unittest framework:

```bash
# Run tests for matrix to list conversion
python -m unittest mat-to-list/test_mat_to_list.py -v

# Run tests for reachable nodes computation
python -m unittest reachable-nodes/test_reachable.py -v
```

## Requirements
- Python 3.x
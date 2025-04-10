# DFA String Matching
This project implements a string matching algorithm using **Deterministic Finite Automata (DFA)** in Python. The program builds a transition function based on a given pattern and processes an input string to determine if the pattern appears as a substring.
## Features

- Accepts a user-defined pattern and input string
- Constructs the DFA transition table
- Simulates the DFA to determine acceptance
- Displays the DFA transitions in a console-readable format
- Visualizes the DFA using `matplotlib`

---
## Requirements
- `matplotlib` (only required for visualization)

---
## How to run 

### 1. Clone the repository
```bash
git clone https://github.com/your-username/dfa-string-matching.git
cd dfa-string-matching
```
### 2. Create a Virtual Environment 
```bash
python3 -m venv venv
source venv/bin/activate (MacOS)
or
venv\Scripts\activate (Windows)
```

### Install Dependencies 
```bash
pip install matplotlib
```
### Running the Program
```bash
python dfa.py
```

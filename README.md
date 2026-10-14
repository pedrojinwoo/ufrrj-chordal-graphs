# Chordal Graphs Recognition and Structural Analysis Suite

[![UFRRJ](https://img.shields.io/badge/UFRRJ-Computer%20Science-blue)](https://portal.ufrrj.br/)
[![License](https://img.shields.io/badge/license-MIT-green)](#)

## 🎓 Academic Context & Overview
This repository contains a comprehensive collection of graph-theoretic algorithms developed for the **Graph Theory** course at **Universidade Federal Rural do Rio de Janeiro (UFRRJ)**. 

The primary objective of this project is to analyze the structural properties of **Chordal Graphs** (a major subclass of perfect graphs) and implement an efficient, linear-time recognition pipeline from scratch. By engineering these algorithms without third-party graph libraries, this suite demonstrates how theoretical characterizations can be translated into precise, predictable software components.

---

## 🛠️ Tech Stack & Skills Demonstrated
*   **Programming Languages:** Python 3.x (Pure implementation).
*   **Algorithmic Paradigms:** Lexicographic Breadth-First Search (Lex-BFS) and Greedy Vertex Elimination.
*   **Mathematical Modeling:** Translating combinatorial theorems (e.g., Dirac's characterization) into discrete data structures (adjacency sets, partition lists).
*   **Version Control Integrity:** Utilizing structured, incremental git commits to map out mathematical development milestones over time.

---

## 🚀 Implemented Methods & Pipeline

The repository is structured into distinct functional modules, each mapping a mandatory theoretical milestone of the project's scope:

### 1. Linear-Time Recognition Pipeline
*   **Lexicographic BFS (Lex-BFS):** A specialized search algorithm that processes graph vertices in a lexicographical order, guaranteeing the generation of a valid elimination ordering if the graph is chordal.
*   **Perfect Elimination Ordering (PEO) Verifier:** A discrete validation mechanism that checks if the neighborhood of every vertex higher in the generated ordering forms a complete clique, ensuring correctness in $O(n + m)$ time.

### 2. Hierarchical Class Classification
*   **Perfect Graphs Embedding:** Documentation and validation of chordal graph properties as a foundational subclass of perfect graphs.
*   **Subclass Relations:** Exploration of tight structural bounds, mapping how specific instances isolate or embed adjacent subclasses such as **Split Graphs** (clique/independent set partitions) and **Interval Graphs**.

### 3. Complexity Optimization (NP-Hard to P)
Algorithms leveraging the Perfect Elimination Ordering (PEO) to solve traditionally NP-Complete problems in linear time:
*   **Maximum Clique:** Polynomial-time identification of the largest complete subgraph by inspecting candidates restricted by the PEO.
*   **Optimal Graph Coloring:** A greedy vertex coloring pipeline running on the reverse PEO, guaranteeing a minimal chromatic number ($\chi(G)$).

### 4. Real-World Applied Systems
*   **Relational Database Query Optimization:** Evaluating chordal structures in query hypergraphs to eliminate cyclical joins and prevent infinite processing loops.
*   **Sparse Linear Systems (Cholesky Factorization):** Simulating variable elimination matrices where a chordal elimination scheme prevents the *fill-in* phenomenon, protecting runtime memory thresholds.

---

## 📊 Continuous Versioning & Diagnostics
To ensure total academic transparency, this suite avoids monolithic code delivery. The repository architecture mirrors a traceable timeline where:
*   Every algorithm module is tied to structured, incremental Git commits.
*   The test engine includes verification suites running both chordal archetypes and non-chordal chordless cycles ($C_k$ for $k \ge 4$) to validate false-positive rejection rates.

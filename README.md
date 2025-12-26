# Big Ten Fight Song Topological Analysis

## Overview

This project applies Topological Data Analysis (TDA) to visualize structural relationships between Big Ten fight songs. Each school is represented as a point in high-dimensional feature space, and the output is a network graph where nodes cluster based on song similarity metrics including tempo, lyrical characteristics, and other audio features.

The visualization identifies structural patterns in the data, including the "Winning Manifold"—a connected loop of schools with both high spirit scores and high win rates—as well as "Dead Zones" representing feature combinations that historically fail.

### Features
* **Network Visualization:** Interactive HTML network graph with schools as nodes connected by similarity relationships
* **Topological Analysis:** TDA identifies manifold structures and clustering patterns in high-dimensional feature space
* **Winning Manifold:** A connected loop of schools that have both high spirit scores and high win rates
* **Dead Zones:** Feature combinations that historically fail, appearing as isolated regions or disconnected components in the visualization
* **Interactive Exploration:** Hover interactions display school statistics including Win %, BPM, and Vibe Score
* **Color Encoding:** Nodes are colored by historical win percentage

---

## Methodology

This project uses KeplerMapper, a Python library for TDA, to construct a mapper graph from high-dimensional feature vectors. The input data consists of fight song characteristics from the FiveThirtyEight dataset, enriched with additional metrics for aggression, complexity, and cliché scores derived from lyrical analysis.

## Documentation

* **[SETUP.md](SETUP.md):** Installation, environment configuration, and startup 
instructions.
* **[ARCHITECTURE.md](docs/ARCHITECTURE.md):** System design, data flow, and technical implementation details.
* **[STYLE.md](docs/STYLE.md):** Coding standards, testing guidelines, and repository 
conventions.

## License

See **[LICENSE](LICENSE)** file for details.

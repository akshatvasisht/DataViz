# Environment Setup Instructions

## Prerequisites

* Python 3.x
* pip (Python package manager)

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd DataViz
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Data Preparation

Ensure the FiveThirtyEight fight songs dataset (`fight-songs.csv`) is placed in the `data/` directory. The dataset is available from FiveThirtyEight's GitHub repository.

## Running the Application

### Step 1: Preprocess Data

```bash
python src/preprocess.py
```

This script:
* Filters the dataset to Big Ten conference schools
* Adds historical win percentage data
* Engineers features (energy_score, aggression_score, cliche_score, complexity_score)
* Outputs `data/processed_fight_songs.csv`

### Step 2: Generate Visualization

```bash
python src/visualize.py
```

This script:
* Loads the processed dataset
* Applies topological data analysis using KeplerMapper
* Generates an interactive HTML visualization
* Outputs `docs/index.html`

## Deployment

The visualization can be deployed to GitHub Pages by:

1. Pushing the repository to GitHub
2. Enabling GitHub Pages in repository settings
3. Setting the source to the `docs/` directory

Alternatively, use the provided `deploy.sh` script to initialize a git repository and prepare for deployment.

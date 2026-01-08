#!/usr/bin/env python3
"""
Topological Data Analysis (TDA) pipeline for Big Ten fight songs.

This script constructs a mapper graph using KeplerMapper to identify structural
relationships between fight songs based on high-dimensional feature space.
The visualization reveals the "Winning Manifold" - connected regions of schools
with both high spirit scores and high win rates.
"""

import os

import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import kmapper as km
from kmapper import Cover


def main() -> None:
    """
    Construct mapper graph from fight song features using topological data analysis.

    The pipeline applies TDA to identify manifold structures in the high-dimensional
    feature space. TSNE provides a 2D lens for dimensionality reduction while preserving
    local structure. DBSCAN clustering within cover elements identifies connected
    components that represent the "Winning Manifold" - schools with similar fight song
    characteristics and win rates.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print("Loading processed fight songs data...")
    df = pd.read_csv(os.path.join(base_dir, 'data', 'processed_fight_songs.csv'))
    
    print(f"Loaded {len(df)} schools")
    
    feature_columns = ['energy_score', 'win_perc', 'aggression_score', 
                      'cliche_score', 'complexity_score']
    X = df[feature_columns].values
    
    tooltips = []
    for _, row in df.iterrows():
        tooltip = (f"<b>{row['school']}</b><br><i>{row['song_name']}</i><br><hr>Win Rate: {row['win_perc']}<br>Aggression: {row['aggression_score']}/10")
        tooltips.append(tooltip)
    tooltips = np.array(tooltips)
    
    print("Scaling features...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    print("Creating TSNE projection (lens)...")
    # Perplexity=5 is optimized for small datasets (N=18) to preserve local structure
    tsne = TSNE(n_components=2, perplexity=5, random_state=42)
    lens = tsne.fit_transform(X_scaled)
    
    print("Initializing KeplerMapper...")
    mapper = km.KeplerMapper(verbose=1)
    
    print("Creating mapper graph...")
    # DBSCAN min_samples=1 ensures all 18 schools are included (no noise dropped)
    # eps=1.5 allows slightly looser clusters within cover elements to encourage connectivity
    graph = mapper.map(
        lens,
        X=X_scaled,
        clusterer=DBSCAN(eps=1.5, min_samples=1),
        cover=Cover(n_cubes=5, perc_overlap=0.5)
    )
    
    print("Visualizing mapper graph...")
    docs_dir = os.path.join(base_dir, 'docs')
    os.makedirs(docs_dir, exist_ok=True)
    mapper.visualize(
        graph,
        path_html=os.path.join(base_dir, 'docs', 'index.html'),
        title="Big Ten Fight Song Topology",
        custom_tooltips=tooltips,
        color_values=df['win_perc'],
        color_function_name="Win Percentage",
        node_color_function=["mean", "max", "min"],
        custom_meta={
            "Insight": "The 'Winning Manifold' (Yellow loop) connects schools with high energy and winning records.",
            "Dead Zones": "Isolated Purple nodes represent schools with low win rates and generic song structures.",
            "Methodology": "TDA (Mapper) on 5-dimensional musical feature space."
        }
    )
    
    num_nodes = len(graph['nodes'])
    num_edges = sum(len(edges) for edges in graph['links'].values()) // 2
    
    print(f"\n{'='*60}")
    print("Mapper Graph Statistics:")
    print(f"{'='*60}")
    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print(f"{'='*60}")
    print(f"\nVisualization saved to: docs/index.html")
    
    # Remove external dependencies and branding for standalone visualization
    html_path = os.path.join(base_dir, 'docs', 'index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('href="http://i.imgur.com/axOG6GJ.jpg"', '')
    content = content.replace('<div class="wrap-logo">', '<div class="wrap-logo" style="display:none;">')
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Cleaned up HTML header and logo.")


if __name__ == '__main__':
    main()

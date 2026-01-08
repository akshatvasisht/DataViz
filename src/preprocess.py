#!/usr/bin/env python3
"""
Process fight-songs.csv to create Big Ten dataset with win percentages and feature engineering.

This script transforms the FiveThirtyEight fight songs dataset by:
1. Updating conference affiliations to reflect recent Big Ten expansion
2. Filtering to Big Ten conference schools only
3. Adding historical win percentage data (not present in original dataset)
4. Engineering features for topological data analysis (TDA)

The output dataset is used for mapper graph construction to identify structural
relationships between fight songs based on lyrical and musical characteristics.
"""

import os

import numpy as np
import pandas as pd

# Historical win percentage data (all-time records)
# Source: https://en.wikipedia.org/wiki/Big_Ten_Conference#All-time_school_records
WIN_PERC = {
    'Ohio State': 0.735, 'Michigan': 0.732, 'USC': 0.694, 'Penn State': 0.691, 'Nebraska': 0.677,
    'Washington': 0.620, 'Michigan State': 0.596, 'Wisconsin': 0.584, 'UCLA': 0.586, 'Oregon': 0.582,
    'Minnesota': 0.573, 'Iowa': 0.546, 'Maryland': 0.520, 'Purdue': 0.513, 'Illinois': 0.507,
    'Rutgers': 0.491, 'Northwestern': 0.448, 'Indiana': 0.421
}


def normalize_to_1_10(values: pd.Series) -> pd.Series:
    """
    Normalize a pandas Series to a 1-10 scale using min-max normalization.
    
    This normalization ensures all engineered features are on a consistent scale
    for topological data analysis, where feature magnitude differences can affect
    distance calculations in high-dimensional space.
    
    Args:
        values: Pandas Series of numeric values to normalize
        
    Returns:
        Pandas Series with values normalized to 1-10 range
    """
    min_val = values.min()
    max_val = values.max()
    
    # Return midpoint value when all inputs are identical to avoid division by zero
    if max_val == min_val:
        return pd.Series([5.5] * len(values), index=values.index)
    
    normalized = 1 + ((values - min_val) / (max_val - min_val)) * 9
    return normalized

def main() -> None:
    """
    Main processing pipeline for Big Ten fight songs dataset.
    
    Processes the original FiveThirtyEight dataset to create a Big Ten-specific
    dataset with win percentages and engineered features suitable for topological
    data analysis. The original dataset is not modified; output is written to
    a separate file to maintain data integrity.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print("Loading fight-songs.csv...")
    df = pd.read_csv(os.path.join(base_dir, 'data', 'fight-songs.csv'))
    
    # Update conference affiliations to reflect 2024 Big Ten expansion
    print("Remapping conferences...")
    schools_to_remap = ['USC', 'UCLA', 'Oregon', 'Washington']
    df.loc[df['school'].isin(schools_to_remap) & (df['conference'] == 'Pac-12'), 'conference'] = 'Big Ten'
    
    print("Filtering to Big Ten conference...")
    df_big10 = df[df['conference'] == 'Big Ten'].copy()
    
    print(f"Found {len(df_big10)} Big Ten schools")
    
    # Add win percentages (required for "Winning Manifold" identification in TDA)
    print("Adding win percentages...")
    df_big10['win_perc'] = df_big10['school'].map(WIN_PERC)
    
    missing = df_big10[df_big10['win_perc'].isna()]
    if len(missing) > 0:
        print(f"Warning: Missing win percentages for: {missing['school'].tolist()}")
    
    # Feature engineering for mapper graph construction
    print("Creating feature engineering columns...")
    
    # Cliché Score: Lyrical conventionality (trope_count)
    df_big10['cliche_score'] = df_big10['trope_count']
    
    # Aggression Score: Composite metric weighting fight frequency and victory language
    df_big10['aggression_score'] = (df_big10['number_fights'] * 2) + \
                                    df_big10['victory_win_won'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_big10['aggression_score'] = normalize_to_1_10(df_big10['aggression_score'])
    
    # Complexity Score: Duration as proxy for compositional complexity
    df_big10['complexity_score'] = normalize_to_1_10(df_big10['sec_duration'])
    
    # Energy Score: Tempo (BPM) measures musical energy
    df_big10['energy_score'] = normalize_to_1_10(df_big10['bpm'])
    
    print("Saving processed data...")
    df_big10.to_csv(os.path.join(base_dir, 'data', 'processed_fight_songs.csv'), index=False)
    
    print(f"\nProcessing complete!")
    print(f"Saved {len(df_big10)} Big Ten schools to data/processed_fight_songs.csv")
    print(f"\nSchools included:")
    for school in sorted(df_big10['school'].tolist()):
        print(f"  - {school}")

if __name__ == '__main__':
    main()

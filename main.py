import os
import glob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from src.data_loader import load_conllu_trees
from src.tree_generator import generate_random_dag
from src.metrics import compute_metrics

def main():
    data_dir = "data"
    results_dir = "results"
    
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        
    conllu_files = glob.glob(os.path.join(data_dir, "*.conllu"))
    if not conllu_files:
        print(f"No .conllu files found in {data_dir}!")
        return

    print(f"Discovered {len(conllu_files)} dataset(s). Loading natural language trees...")
    
    real_metrics_list = []
    rand_metrics_list = []
    
    valid_trees = 0
    for conllu_path in conllu_files:
        print(f"Processing {os.path.basename(conllu_path)}...")
        for real_dag in load_conllu_trees(conllu_path):
            N = real_dag.number_of_nodes()
            if N <= 1:
                continue
                
            valid_trees += 1
            # Compute metrics for real language DAG
            real_metrics = compute_metrics(real_dag)
            real_metrics_list.append(real_metrics)
            
            # Generate random matched DAG and compute metrics
            rand_dag = generate_random_dag(N)
            rand_metrics = compute_metrics(rand_dag)
            rand_metrics_list.append(rand_metrics)
        
    print(f"\nSuccessfully processed {valid_trees} valid dependency trees across all languages.")
    
    if valid_trees == 0:
        print("No valid trees found. Exiting.")
        return

    # Convert to DataFrames for easier plotting
    real_df = pd.DataFrame(real_metrics_list)
    real_df['Label'] = 'Natural Language'
    
    rand_df = pd.DataFrame(rand_metrics_list)
    rand_df['Label'] = 'Random DAG'
    
    combined_df = pd.concat([real_df, rand_df], ignore_index=True)
    
    # Print summary statistics
    for metric in ['max_arity', 'tree_depth', 'density']:
        print(f"\n--- {metric.replace('_', ' ').title()} ---")
        real_mean = real_df[metric].mean()
        rand_mean = rand_df[metric].mean()
        print(f"Natural Language Mean: {real_mean:.4f}")
        print(f"Random DAG Mean:       {rand_mean:.4f}")
        
    # Plotting
    sns.set_theme(style="whitegrid")
    
    metrics_to_plot = [
        ('max_arity', 'Tree Arity (Max Out-degree)'),
        ('tree_depth', 'Tree Depth (Max root-to-leaf path)'),
        ('density', 'Graph Density')
    ]
    
    for metric_col, metric_label in metrics_to_plot:
        plt.figure(figsize=(10, 6))
        
        # We use a KDE plot or histogram
        sns.histplot(
            data=combined_df, 
            x=metric_col, 
            hue="Label", 
            kde=True, 
            element="step", 
            stat="density", 
            common_norm=False,
            bins=30
        )
        
        plt.title(f"Cross-Linguistic Distribution of {metric_label} (N={valid_trees})")
        plt.xlabel(metric_label)
        plt.ylabel("Density")
        plt.tight_layout()
        
        outfile = os.path.join(results_dir, f"crosslingual_{metric_col}_distribution.png")
        plt.savefig(outfile, dpi=150)
        plt.close()
        print(f"Saved plot to {outfile}")

if __name__ == "__main__":
    main()

from src.clustering import load_and_cluster
from src.visualize import plot_clusters

# load data and apply k-means
clustered_df = load_and_cluster("data/sample_wnba_stats.csv")

# plot points vs assists with cluster coloring
plot_clusters(clustered_df)

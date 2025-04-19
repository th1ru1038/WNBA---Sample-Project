import matplotlib.pyplot as plt

# make a scatter plot of 2P vs 3P with styled markers
def plot_clusters(df):
    plt.figure(figsize=(8,6))

    # define marker styles and labels
    markers = {
        0: ("D", "Sharpshooter"),
        1: ("s", "Slasher"),
        2: ("o", "All-Around Scorer"),
        3: ("^", "Low Offensive Impact")
    }

    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

    for cluster_id, (marker, label) in markers.items():
        cluster_data = df[df["Cluster"] == cluster_id]
        plt.scatter(
            cluster_data["2P_Made"],
            cluster_data["3P_Made"],
            label = label,
            marker = marker,
            color = colors[cluster_id],
            edgecolor = 'black',
            s = 80
        )

    plt.xlabel("Avg twos made")
    plt.ylabel("Avg threes made")
    plt.title("Scoring Clusters for Guards")
    plt.legend(title="Scoring Archetype")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
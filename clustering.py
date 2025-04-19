import pandas as pd
from sklearn.cluster import KMeans

# load data and apply k-means clustering
def load_and_cluster(filepath):
    df = pd.read_csv(filepath)
    
    # select features
    features = ["2P_Made", "3P_Made"]
    X = df[features]

    # cluster into 4 groups
    kmeans = KMeans(n_clusters=4, random_state=42)
    df["Cluster"] = kmeans.fit_predict(X)

    return df

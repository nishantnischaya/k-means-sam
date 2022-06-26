import kmeans_sam as ks
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans


## Create data for clustering
X, _ = make_blobs(n_samples=10, centers=3, n_features=4)
df = pd.DataFrame(X, columns=['Feat_1', 'Feat_2', 'Feat_3', 'Feat_4'])

## Create KMeans model
kmeans = KMeans(n_clusters=3)
kmeans.fit(df[['Feat_1', 'Feat_2', 'Feat_3', 'Feat_4']])

## Create KMeansSam object
kmeans_sam = ks.KMeansSam()

## Create KMeansSam clusters
clusters = kmeans_sam.clusterize(kmeans, df, ['Feat_1', 'Feat_2', 'Feat_3', 'Feat_4'])
print(clusters)

## Get cluster by id
cluster2 = kmeans_sam.get_cluster(2)
print("---------------------------")
print(cluster2)

## Merge clusters by list of cluster ids
print(kmeans_sam.merge_cluster([0, 2]))

## Get all clusters
clusters = kmeans_sam.get_all_clusters()
print("---------------------------")
print(clusters)

## Subclusterize KMeansSam cluster by cluster id
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
kmeans = KMeans(n_clusters=2)
kmeans.fit(df[['Feat_1', 'Feat_2', 'Feat_3', 'Feat_4']])
print(kmeans_sam.subclusterize(kmeans, 0, ['Feat_1', 'Feat_2', 'Feat_3', 'Feat_4']))

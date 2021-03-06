# k-means-sam
k-means sub-clustering and merging library for strong control and flexibility over k-means clustering

The operations provided in k-means-sam are :
1. Making k-means clusters 
2. Querying clusters by id
3. Sub-clustering k-means clusters by specifying cluster id
4. Merging k-means clusters by specifying cluster ids


**USAGE -**

### Import kmeans-sam

~~~~
import kmeans_sam as ks
~~~~

### Making clusters 

Steps - 
1. Create a k-means model and perform .fit() operations
2. Create a kmeans-sam object 
3. kmeans-sam.clusterize(model = kmeans_mode, dataframe = df, predictors = [column_names])

Code: 
~~~~
## Create data for clustering
X, _ = make_blobs(n_samples=10, centers=3, n_features=4)
df = pd.DataFrame(X, columns=['Feat_1', 'Feat_2', 'Feat_3', 'Feat_4'])
## Create KMeans model
kmeans = KMeans(n_clusters=3)
kmeans.fit(df[['Feat_1', 'Feat_2', 'Feat_3', 'Feat_4']])
## Create KMeansSam object
kmeans_sam = ks.KMeansSam()
## Create KMeansSam clusters. parameters : kmeans model, dataframe, list of column names
clusters = kmeans_sam.clusterize(kmeans, df, ['Feat_1', 'Feat_2', 'Feat_3', 'Feat_4'])
print(clusters)
~~~~


### Querying cluster by id

Code:
~~~~
## Fetched all the clusters with id
clusters = kmeans_sam.get_all_clusters()
print(kmeans_sam.get_cluster(2))
~~~~

### Sub-clustering k-means clusters by specifying cluster id

~~~~
kmeans = KMeans(n_clusters=2)
kmeans.fit(df[['Feat_1', 'Feat_2', 'Feat_3', 'Feat_4']])
## parameters : kmeans model, cluster_id, list of column names
print(kmeans_sam.subclusterize(kmeans, 0, ['Feat_1', 'Feat_2', 'Feat_3', 'Feat_4']))
~~~~

### Merging clusters by cluster_ids
Code:
~~~~
print(kmeans_sam.merge_cluster([0, 2]))
~~~~

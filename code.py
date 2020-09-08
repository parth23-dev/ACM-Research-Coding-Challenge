import pandas as pd
from numpy import unique
from numpy import where
from sklearn.cluster import KMeans
from matplotlib import pyplot
from yellowbrick.cluster import KElbowVisualizer

# Shift data from csv to array
dp = pd.read_csv (r'/Users/Parth/Downloads/Coding-Challenge-master/ClusterPlot.csv')
dp_array = dp[['V1', 'V2']].to_numpy()

# Find the number of clusters
model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,15), timings=False)

# Fit the data to the graph
visualizer.fit(dp_array)
visualizer.show()

# The KMean algorithim below shows the graph with 3 clusters

# Choose the clustering algo
model = KMeans(n_clusters=3)
model.fit(dp_array)

# Find the clusters
cluster_samp = model.predict(dp_array)
clusters = unique(cluster_samp)

# Make scatter plot using clusters
for cluster in clusters:
	find_rows = where(cluster_samp == cluster)
	pyplot.scatter(dp_array[find_rows, 0], dp_array[find_rows, 1])

# Show plot
pyplot.show()

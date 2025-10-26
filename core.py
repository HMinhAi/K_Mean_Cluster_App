import random 
import numpy as np

def random_centroid(num_centroid= 2, x_max= 20, y_max= 20):
    centroid_pos = {}
    for _ in range(num_centroid):
        centroid_x = random.uniform(0, x_max)
        centroid_y = random.uniform(0, y_max)
        cluster = {
            'center': [centroid_x, centroid_y],
            'point': []
        }
        centroid_pos[_]= cluster
    return centroid_pos

# Using Euclidean Distance   
def Euclidean_distance(a, b):
    return np.sqrt(np.sum((a-b) ** 2))

def assign_clusters(X, clusters, k= 3):
    for idx in range(X.shape[0]):
        dist = []
        
        curr_x = X[idx]
        
        for i in range(k):
            dis = Euclidean_distance(curr_x,clusters[i]['center'])
            dist.append(dis)
        curr_cluster = np.argmin(dist)
        clusters[curr_cluster]['points'].append(curr_x)
    return clusters

def update_clusters(clusters, k= 3):
    for i in range(k):
        points = np.array(clusters[i]['points'])
        if points.shape[0] > 0:
            new_center = points.mean(axis =0)
            clusters[i]['center'] = new_center
            
            clusters[i]['points'] = []
    return clusters

def data():
    raw_data = [[2, 10], [4, 5], [3, 2], [9, 4], [3, 7], [5, 5], [6, 4], [1, 9], [1, 2], [4,9]]

    
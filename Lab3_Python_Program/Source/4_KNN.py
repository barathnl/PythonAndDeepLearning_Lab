from collections import OrderedDict
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

i = []
s = []
def get_data(filename):
    with open(filename,'r') as csvdocument:
        csvFileContent = csv.reader(csvdocument)
        next(csvFileContent)  # skipping column names
        for row in csvFileContent:
            i.append(int(row[3]))
            s.append(int(row[4]))
    return
get_data('BankDetail.csv')
data = list(zip(i,s))
print("Data:")
print(data)
#Kmean
kmeans = KMeans(n_clusters=20)
kmeans.fit(data)
#Finding centroids
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
print("Centroids:")
print(centroids)
colors = ["y","m","b","r","c","m","y","g","b","r","m","y","g","b","r","c","y","g","m","r"]
label = ["Cluster-1","Cluster-2","Cluster-3","Cluster-4","Cluster-5","Cluster-6","Cluster-7","Cluster-8","Cluster-9","Cluster-10","Cluster-11","Cluster-12","Cluster-13","Cluster-14","Cluster-15","Cluster-16","Cluster-17","Cluster-18","Cluster-19","Cluster-20"]
#plot points
for i in range(len(data)):
    print("coordinate:",data[i], "label:", labels[i])
    plt.scatter(data[i][0], data[i][1], c = colors[labels[i]], label = label[labels[i]])
#plot centroids
plt.scatter(centroids[:, 0],centroids[:, 1], label = "Centroids",marker = "x", s=150, linewidths = 10, zorder = 15)
plt.title('clusters of Bank customers')
plt.xlabel('Annual Income(k$)')
plt.ylabel('Credit Score')
#remove duplicates of labels
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())
plt.show()
#predictions
print("Predicted Class:")
print(kmeans.predict([(20,40)]))
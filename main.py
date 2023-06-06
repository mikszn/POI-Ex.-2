import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from fun import *

clusters = []
# Zaimportowanie wygenerowanych chmur
def cloud_reader1():
    with open('PlaskaPozioma.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x, y, z in reader:
            yield (float(x), float(y), float(z))

def cloud_reader2():
    with open('PlaskaPionowa.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x, y, z in reader:
            yield (float(x), float(y), float(z))
def cloud_reader3():
    with open('Walec.xyz', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for x, y, z in reader:
            yield (float(x), float(y), float(z))

# Połączenie chmur w jedną
for p in cloud_reader1():
    clusters.append(p)
for p in cloud_reader2():
    clusters.append(p)
for p in cloud_reader3():
    clusters.append(p)

x, y, z = zip(*clusters) # wydzielenie współrzędnych punktów do osobnych list
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, s = 1)  #Rysowanie wykresu punktowego
plt.title('Points scattering in 3D')
ax.set_xlabel('x', fontsize = 14)
ax.set_ylabel('y', fontsize = 14)
ax.set_zlabel('z', fontsize = 14)
ax.axis('equal')


clusterer = KMeans(n_clusters=3, n_init=10)  # Konstruktor; n_init - licza iteracji
X = np.array(clusters) # utworzenie tablicy krotek będących współrzędnymi kolejnych punktów

y_pred = clusterer.fit_predict(X) # Klasteryzacja przez wpisanie 0/1/2 na pozycjach poszczególnych punktów

# Wektory oznaczające czy na danej pozycji znajduje się punkt należący do określonego klastra
red = y_pred == 0
blue = y_pred == 1
cyan = y_pred == 2

fig2 = plt.figure()
f2 = fig2.add_subplot(projection='3d')
f2.scatter(X[red, 0], X[red, 1], X[red, 2], c="r", s = 1)
f2.scatter(X[blue, 0], X[blue, 1], X[blue, 2], c="b", s = 1)
f2.scatter(X[cyan, 0], X[cyan, 1], X[cyan, 2], c="c", s = 1)
plt.title('Points scattering in 3D')
f2.set_xlabel('x', fontsize = 14)
f2.set_ylabel('y', fontsize = 14)
f2.set_zlabel('z', fontsize = 14)
f2.axis('equal')


ransac(X[red])
ransac(X[blue])
ransac(X[cyan])

plt.show()
from sklearn.cluster import KMeans
from scipy.stats import norm

import matplotlib.pyplot as plt
import numpy as np

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Generacja trzech zbiorów punktów, które zostają połączone,
# a następnie przy pomocy KMeans podzielone na klastry
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Środki klastrów w przestrzeni 2D
mns = [(5, 3), (15, 4), (10, 8)]

# Odchylenia standardowe
scales = [(2, 1), (1, 1), (1, 2)]

params = zip(mns, scales)  # Parametry zagregowane w celu uproszczenia iteracji

clusters = []

# Generacja punktow i połączenie ich w jedną listę
for parset in params:
    dist_x = norm(loc=parset[0][0], scale=parset[1][0])
    dist_y = norm(loc=parset[0][1], scale=parset[1][1])
    cluster_x = dist_x.rvs(size=100)
    cluster_y = dist_y.rvs(size=100)
    cluster = zip(cluster_x, cluster_y)
    clusters.extend(cluster)

    # append dodaje kolejny pojedynczy element (wartość, listę...)
    # extend dodajne kolejne elementy (np. umieszczone w liście)
    # W efekcie, w clusters znajduje lista punktów, a nie klastrów

# Wydzielenie współrzędnych x i y do osobnych list ("rozpakowanie")
x, y = zip(*clusters)

#plt.figure()
plt.scatter(x, y)  #Rysowanie wykresu punktowego
plt.title('Points scattering in 2D')
#plt.tight_layout()
plt.xlabel('x', fontsize = 14)
plt.ylabel('y', fontsize = 14)


clusterer = KMeans(n_clusters=3)
# 1) Wyznaczane są centra (tyle ile wynosi n_clusters)
# 2) Obliczane są odległości wszystkich punktów do centrów
# 3) Następuje przypisanie punktów do klastrów, w zależności od tego,
#    które centrum znajduje się najbliżej
# 4) Liczona jest średnia współrzędnych x i y wszystkich punktów w danych klastrach
#    i w ten sposób zostają wyznaczone nowe centra klastrów
# Powrót do punktu 2)
#
# Kolejne iteracje następują do spełnienia określonego warunku, np. liczby iteracji lub braku zmiany położenia centrów

# Domyślnie KMeans wykonuje się 8-krotnie, a tolerancja...

# Przekształcenie listy krotek na tablicę 2D
X = np.array(clusters)

# Dopasowanie do danych (fit; "nauczenie" - znalezienie reguł)
# i przewidzenie etykiet dla każdego punktu (etykiety to liczby naturalne).
y_pred = clusterer.fit_predict(X)

# Utworzenie list z wartościami false/true, w zależności od etykiety przypisanej danemu punktowi
red = y_pred == 0
blue = y_pred == 1
cyan = y_pred == 2

plt.figure()
plt.scatter(X[red, 0], X[red, 1], c="r")
plt.scatter(X[blue, 0],X[blue, 1], c="b")
plt.scatter(X[cyan, 0], X[cyan, 1], c="c")
plt.show()
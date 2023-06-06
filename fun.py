import numpy as np
import random

def ransac(points, maxIter: int = 10):
    iter = 1
    modelPoints = []
    for i in range(0, 10):
        modelPoints.append(((0,0,0),(0,0,0),(0,0,0)))

    modelSize = np.zeros(10)

    while True:
        # Wylosowanie 3 punktów
        randPts = np.zeros((3, 3))
        for i in range(3):
            rnd = random.randint(0, len(points) - 1)
            randPts[i] = (points[rnd][0], points[rnd][1], points[rnd][2])

        vA = randPts[0] - randPts[2]
        vB = randPts[1] - randPts[2]

        if np.linalg.norm(vA) == 0 or np.linalg.norm(vB) == 0:
            print("ERROR")
            break
        uA = vA / np.linalg.norm(vA)
        uB = vB / np.linalg.norm(vB)

        w = np.cross(uA, uB)  # wektor W (normalny do płaszczyzny)
        d = -np.sum(np.multiply(w, randPts[2]))  # odległość od początku układu wspólrzędnych

        distance_all_points = np.zeros(len(points))
        for i in range(0, len(points)):
            distance_all_points[i] = (np.sum(np.multiply(w,points[i])) + d) / np.linalg.norm(w)

        thresh = 3
        inliers = np.where(np.abs(distance_all_points) <= thresh)[0]  # Zwraca elementy dla których spełniony jest warunek (inlierów)
        modelSize[iter-1] = len(inliers) # liczba inlierów
        modelPoints[iter-1] = (randPts[0], randPts[1], randPts[2])

        iter += 1
        if iter > maxIter or modelSize[iter-2] == len(points): # przerwanie jeśli wykonano maksymalna liczbe iteracji lub gdy wszystkie punkty to inliery

            bestModelIndex = np.array(modelSize).argmax()      # Analiza dla najlepszego przypadku ze wszystkich iteracji
            a = modelPoints[bestModelIndex][0]
            b = modelPoints[bestModelIndex][1]
            c = modelPoints[bestModelIndex][2]
            vA = a - c
            vB = b - c

            if np.linalg.norm(vA) == 0 or np.linalg.norm(vB) == 0:
                print("ERROR")
                break
            uA = vA / np.linalg.norm(vA)
            uB = vB / np.linalg.norm(vB)

            w = np.cross(uA, uB)  # wektor W (normalny do płaszczyzny)
            d = -np.sum(np.multiply(w, c))  # odległość od początku układu wspólrzędnych

            distance_all_points = np.zeros(len(points))
            for i in range(0, len(points)):
                distance_all_points[i] = (np.sum(np.multiply(w, points[i])) + d) / np.linalg.norm(w)

            print("Wektor normalny:", w)
            distance_all_points_sum = np.sum(abs(distance_all_points))
            if distance_all_points_sum < 1:
                print("Plaszczyzna ", end="")
                if w[2] == 0:  # z == 0
                    print("pionowa.")
                elif w[0] == 0 and w[1] == 0:  # x == 0 i y == 0
                    print("pozioma.")
                else:
                    print("[bład]")
            else:
                print("To nie jest plaszczyzna.")
            break

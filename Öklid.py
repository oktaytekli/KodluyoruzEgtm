import math

points=[(1, 2), (4, 6), (5, 1), (2, 3), (7, 5)] #2D uzayında tanımlı beş nokta

def euclideanDistance(point1, point2): #bu bölüm iki nokta arasındaki Öklid msf. hesaplar
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

distances = []

for i in range (len(points)): #mesafeleri hesaplar ve distance listesine ekler. Daha sonrasında ekrana yazdırır.
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        print(f"{points[i]} ve {points[j]} arasındaki mesafe: {distance: .2f}")

min_distance = min(distances)
print(f"\nEn küçük mesafe: {min_distance: .2f}")

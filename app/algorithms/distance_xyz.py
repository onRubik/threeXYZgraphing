import math


def distance_xyz(x0, y0, z0, x1, y1, z1):
    deltaX = x1 - x0
    deltaY = y1 - y0
    deltaZ = z1 - z0
    
    distance = math.sqrt(deltaX * deltaX + deltaY * deltaY + deltaZ * deltaZ)
    
    return distance


if __name__ == '__main__':
    distance_xyz()
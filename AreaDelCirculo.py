import math
def areas(r, a):
    """
    :param r: (float) The radius of the circle.
    :param a: (float) The angle of the segment.
    :returns: (list) (A list of two elements containing the area inside, and area outside the circle, in that order.)
    """
    pi = math.pi
    area = pi * (r**2)

    op2 = (a*(pi/180))-(math.sin(a*(pi/180)))
    op1 = (r**2)/2
    segmento = op1 - op2
    return (area, segmento)

print(areas(10, 90))

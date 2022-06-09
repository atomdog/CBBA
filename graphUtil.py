#graphUtil.py
import matplotlib.pyplot as plt
import numpy as np
import math
import random
def colormap(k):
    better_colors = []

    for coloriterator in range(0, k):
        f = random.random()
        f2 = random.random()
        f3 = random.random()
        cv = coloriterator+random.randint(0, 20)
        red = (cv+f) % 1.0
        blue = (cv+f2) % 1.0
        green = (cv+f3) % 1.0
        color_insert=(red, blue, green)
        better_colors.append(color_insert)
    return(better_colors)

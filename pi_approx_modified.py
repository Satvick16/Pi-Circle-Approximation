import random
from math import sqrt
from matplotlib import pyplot as plt
import numpy as np

# TODO consider adding animations


def makePi(accuracy: int) -> float:
    """"""
    radius = 1

    x_pts = []
    y_pts = []

    pi = 0
    pts = 0

    for i in range(accuracy + 1):
        x = random.uniform(-1.0, 1.0)
        x_pts.append(x)

        y = random.uniform(-1.0, 1.0)
        y_pts.append(y)

        dist = sqrt(x**2 + y**2)

        if dist <= radius:
            pi += 1

        pts += 1

    # ensures matplotlib window is 1:1 (preserves proportions of circle function)
    plt.figure(figsize=(6, 6))

    # plot all points
    plt.scatter(x_pts, y_pts, s=0.2, color='black', marker='o')

    # set axes limits
    plt.xlim(-1.1, 1.1)
    plt.ylim(-1.1, 1.1)

    ax = plt.gca()

    # graph circle of radius 1
    circle1 = plt.Circle((0, 0), 1.0, color='r', alpha=0.2)
    ax.add_artist(circle1)

    # place the axes in the middle of the window
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    # show grid lines at intervals of 1
    plt.xticks(np.arange(-1, 1, 1.0))
    plt.yticks(np.arange(-1, 1, 1.0))

    # set label sizes
    ax.tick_params(axis='both', labelsize=10)

    # write calculation information to a file
    writing_to_file(pts, pi)

    plt.title(f"Points = {str(pts)}, π = {str(4 * pi / pts)} (see pi.txt)")
    plt.tight_layout()
    plt.show()

    return 4 * pi / pts


def writing_to_file(pts, pi):
    with open('pi.txt', 'w') as f:
        file_text = f"This iteration uses {pts} points.\n" \
                    f"{pi} of them fell inside the unit circle shown in red.\n" \
                    f"The approximation was formulated by dividing those two figures.\n" \
                    f"See https://en.wikipedia.org/wiki/Approximations_of_%CF%80#Summing_a_circle's_area for more " \
                    f"information.\n "
        f.write(file_text)


def main():
    print(makePi(9999))


if __name__ == "__main__":
    main()

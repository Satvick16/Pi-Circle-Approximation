import random
from math import sqrt
from matplotlib import pyplot as plt
import numpy as np

# TODO add comments and documentation
# TODO consider adding animations


def makePi(accuracy: int) -> float:
    """"""
    radius = 1

    x_pts = []
    y_pts = []

    pi = 0
    pts = 0

    for i in range(accuracy + 1):
        x = random.uniform(0.0, 1.0)
        x_pts.append(x)

        y = random.uniform(0.0, 1.0)
        y_pts.append(y)

        dist = sqrt(x**2 + y**2)

        if dist <= radius:
            pi += 1

        pts += 1

    # ensures matplotlib window is 1:1 (preserves circle function)
    plt.figure(figsize=(7, 7))

    plt.plot(np.linspace(0, 1, 9999), (1 - np.linspace(0, 1, 9999)**2)**0.5, c='r', linewidth='1')
    plt.fill_between(np.linspace(0, 1, 9999), (1 - np.linspace(0, 1, 9999)**2)**0.5, color='#f7dfdf')
    plt.scatter(x_pts, y_pts, s=0.05, color='black', marker='o')

    plt.xlim(0, 1)
    plt.ylim(0, 1)

    writing_to_file(pts, pi)

    plt.title(f"Points = {str(pts)}, π = {str(4 * (pi / pts))} (see pi.txt)")
    plt.tight_layout()
    plt.show()

    return 4 * (pi / pts)


def writing_to_file(pts, pi):
    with open('pi.txt', 'w') as f:
        file_text = f"This iteration uses {pts} points.\n" \
                    f"{pi} of them fell inside the unit circle shown in red.\n" \
                    f"The approximation was formulated by dividing those two figures.\n" \
                    f"See https://en.wikipedia.org/wiki/Approximations_of_%CF%80#Summing_a_circle's_area for more " \
                    f"information.\n "
        f.write(file_text)


def main():
    # Most accurate iteration to date: 3.142292
    print(makePi(99999))


if __name__ == "__main__":
    main()

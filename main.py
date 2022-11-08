import matplotlib.pyplot as plt
import random

if __name__ == "__main__":
    N = 100000
    x_yes = []
    y_yes = []
    x_no = []
    y_no = []
    for i in range(N):
        x = random.random() * 4
        y = random.random() * 4
        if (x >= 0 and x <= 2 and y >= 0 and y <= 3) or (x > 2 and x <= 4 and y >= 1 and y <= 2):
            x_yes.append(x)
            y_yes.append(y)
            print(f"({x}, {y}) - yes")
        else:
            x_no.append(x)
            y_no.append(y)
            print(f"({x}, {y}) - no")
    res = (len(x_yes)/N)*16
    print(res)
    plt.scatter(x_yes, y_yes, color= "green", marker= ".", s=10)
    plt.scatter(x_no, y_no, color= "red", marker= ".", s=10)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
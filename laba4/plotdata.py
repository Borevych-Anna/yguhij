import matplotlib.pyplot as plt


def plot_data():
    x = [1, 2 ,3 ,4 ,5]
    y = [10, 20, 15, 30, 25]

    plt.plot(x, y, marker="o")
    plt.title("Графік")
    plt.xlabel("Номер")
    plt.ylabel("Значення")
    plt.grid(True)

    plt.savefig("output/graph.png")

    plt.show()
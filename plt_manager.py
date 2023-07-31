import matplotlib.pyplot as plt


def plt_manager(title, xlabel, ylabel, rotation=90):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.show()

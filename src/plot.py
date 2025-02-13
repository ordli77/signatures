import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot(wealths,inventories,speeds):
    plt.figure(figsize=(16, 4))
    plt.subplot(1, 3, 1)
    sns.histplot(wealths,stat="count")
    plt.xlabel("Terminal wealth")
    plt.ylabel("Frequency")


    plt.subplot(1, 3, 2)
    for Q in inventories:
        plt.plot(np.linspace(0, 1, len(Q)), Q, "b", alpha=0.1)
    plt.ylabel("Inventory")
    plt.xlabel("Time")

    plt.subplot(1, 3, 3)
    for speed in speeds:
        plt.plot(speed, "b", alpha=0.1)
    plt.ylabel("Speed")

    plt.show()

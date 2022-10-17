from matplotlib import pyplot as plt



def Cdl( C1, C2, C3, C4, l):
    fig, ax = plt.subplots()
    ax.grid()
    plt.title("C/dl")
    ax.set_ylabel("С")
    ax.set_xlabel("l")

    ax.plot(l, C1, color="green", alpha=0.3, label="C1")
    ax.plot(l, C2, color="orange", alpha=0.3, label="C2")
    ax.plot(l, C3, color="red", alpha=0.3, label="C3")
    ax.plot(l, C4, color="black", alpha=0.3, label="C4")

    plt.legend()
    plt.show()
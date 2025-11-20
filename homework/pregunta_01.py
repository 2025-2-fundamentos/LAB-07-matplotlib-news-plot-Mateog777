import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():
    df = pd.read_csv("files/input/news.csv")
    x = df.iloc[:, 0]
    cols = df.columns[1:]

    os.makedirs("files/plots", exist_ok=True)

    plt.figure(figsize=(8, 5))
    for c in cols:
        plt.plot(x, df[c], marker="o", label=c)

    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.title("News consumption by medium")
    plt.legend()
    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.close()


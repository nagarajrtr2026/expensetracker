import matplotlib.pyplot as plt

def show_category_chart(summary):
    cats = summary.keys()
    values = summary.values()

    plt.bar(cats, values)
    plt.title("Category Spending")
    plt.show()
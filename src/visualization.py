import matplotlib.pyplot as plt
import seaborn as sns

def plot_rating_distribution(df):
    plt.figure(figsize=(6, 4))
    sns.histplot(df['rating'], bins=5, kde=False)
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.show()

def plot_top_products(df, top_n=10):
    top_products = df['productId'].value_counts().head(top_n)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_products.values, y=top_products.index)
    plt.title("Top Rated Products by Count")
    plt.xlabel("Number of Ratings")
    plt.ylabel("Product ID")
    plt.show()

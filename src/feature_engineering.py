def filter_active_users_products(df, min_ratings=50):
    product_counts = df['productId'].value_counts()
    user_counts = df['userId'].value_counts()

    df = df[df['productId'].isin(product_counts[product_counts >= min_ratings].index)]
    df = df[df['userId'].isin(user_counts[user_counts >= min_ratings].index)]
    return df

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def cluster_spending(df, n_clusters=4):
    features = df[['amount_scaled', 'day_of_week', 'hour']]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(features)
    plt.scatter(df['day_of_week'], df['amount_scaled'], c=df['cluster'])
    plt.title('Spending Clusters')
    plt.xlabel('Day of Week')
    plt.ylabel('Scaled Amount')
    plt.show()
    return df
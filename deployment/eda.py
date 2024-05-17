import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def app():
    df = pd.read_csv('listings_clustered.csv')
    st.title('Exploratory Data Analysis pada Dataset US Airbnb')

    mean_data = df.groupby('cluster')['price'].mean().reset_index()
    mean_data['cluster'] = mean_data['cluster'].astype(int) 
    mean_data = mean_data.round(0).astype(int)

    st.write(mean_data)

    # Plot stacked bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(mean_data['cluster'], mean_data['price'], color='orange')

    # Add labels and title
    ax.set_title('Average Price by Cluster')
    ax.set_xlabel('Cluster')
    ax.set_ylabel('Mean Price')
    ax.set_xticks(mean_data['cluster'])
    ax.grid(True)

    st.pyplot(fig)

    st.write("Berdasarkan grafik diatas menunjukkan bahwa cluster 1 memiliki harga yang jauh lebih tinggi dibandingkan cluster 0")
    st.write("Sehingga cluster 1 dapat digolongkan ke cluster mewah dan cluster 0 merupakan cluster ekonomis")

    # Calculate the average price for each city
    avg_price_by_city = df.groupby('city')['price'].mean()

    # Filter data for the top 5 citys
    top_5_avg_price = avg_price_by_city.sort_values(ascending=False).head(5)
    filtered_data = df[df['city'].isin(top_5_avg_price.index)]

    # Group by 'city' and 'cluster', then calculate the average price for each group
    avg_price_by_city_cluster = filtered_data.groupby(['city', 'cluster'])['price'].mean().unstack()

    # Plot stacked bar chart for top 5 citys
    fig, ax = plt.subplots(figsize=(12, 8))
    avg_price_by_city_cluster.plot(kind='bar', stacked=True, ax=ax)

    # Add labels and title
    ax.set_title('Average highest price by city and cluster (Top 5)')
    ax.set_xlabel('city')
    ax.set_ylabel('Average Price')
    ax.set_xticklabels(avg_price_by_city_cluster.index, rotation=0)
    ax.legend(title='Cluster', loc='upper left')

    st.pyplot(fig)

    st.write("Berdasarkan grafik diatas menunjukkan bahwa di kota Oakland mempunyai harga yang paling tinggi dan di kota tersebut memang lebih banyak terdapat cluster 1 / cluster mewah dibandingkan cluster ekonomis")

    # Calculate the average price for each city
    avg_price_by_city = df.groupby('city')['price'].mean()

    # Filter data for the top 5 citys
    top_5_avg_price = avg_price_by_city.sort_values(ascending=True).head(5)
    filtered_data = df[df['city'].isin(top_5_avg_price.index)]

    # Group by 'city' and 'cluster', then calculate the average price for each group
    avg_price_by_city_cluster = filtered_data.groupby(['city', 'cluster'])['price'].mean().unstack()

    # Plot stacked bar chart for top 5 citys
    fig, ax = plt.subplots(figsize=(12, 8))
    avg_price_by_city_cluster.plot(kind='bar', stacked=True, ax=ax)

    # Add labels and title
    ax.set_title('Average lowest price by city and cluster (Top 5)')
    ax.set_xlabel('city')
    ax.set_ylabel('Average Price')
    ax.set_xticklabels(avg_price_by_city_cluster.index, rotation=0)
    ax.legend(title='Cluster', loc='upper left')

    st.pyplot(fig)

    # Calculate the average price for each accommodates
    avg_price_by_accommodates = df.groupby('accommodates')['price'].mean()

    # Filter data for the top 5 accommodatess
    top_5_avg_price = avg_price_by_accommodates.sort_values(ascending=False).head(5)
    filtered_data = df[df['accommodates'].isin(top_5_avg_price.index)]

    # Group by 'accommodates' and 'cluster', then calculate the average price for each group
    avg_price_by_accommodates_cluster = filtered_data.groupby(['accommodates', 'cluster'])['price'].mean().unstack()

    # Plot stacked bar chart for top 5 accommodatess
    fig, ax = plt.subplots(figsize=(12, 8))
    avg_price_by_accommodates_cluster.plot(kind='bar', stacked=True, ax=ax)

    # Add labels and title
    ax.set_title('Average price by accommodates and cluster (Top 5)')
    ax.set_xlabel('accommodates')
    ax.set_ylabel('Average Price')
    ax.set_xticklabels(avg_price_by_accommodates_cluster.index, rotation=0)
    ax.legend(title='Cluster', loc='upper left')

    st.pyplot(fig)

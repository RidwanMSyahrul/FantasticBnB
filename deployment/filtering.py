import streamlit as st
import pandas as pd

def app():
    # Load your data
    df = pd.read_csv('listings_clustered.csv')

    # Sidebar for user inputs
    st.header('Filter Options')

    # Filter for city
    city_options = df['city'].unique().tolist()
    selected_city = st.selectbox('City', city_options)

    # Filter for accommodates
    min_accommodates = st.slider('Minimum Accommodates', min_value=0, max_value=int(df['accommodates'].max()), value=0)
    max_accommodates = st.slider('Maximum Accommodates', min_value=min_accommodates, max_value=int(df['accommodates'].max()), value=int(df['accommodates'].max()))

    # Filter for number_of_reviews
    min_reviews = st.slider('Minimum Number of Reviews', min_value=0, max_value=int(df['number_of_reviews'].max()), value=0)
    max_reviews = st.slider('Maximum Number of Reviews', min_value=min_reviews, max_value=int(df['number_of_reviews'].max()), value=int(df['number_of_reviews'].max()))

    # Filter for bedrooms
    min_bedrooms = st.slider('Minimum Bedrooms', min_value=0, max_value=int(df['bedrooms'].max()), value=0)
    max_bedrooms = st.slider('Maximum Bedrooms', min_value=min_bedrooms, max_value=int(df['bedrooms'].max()), value=int(df['bedrooms'].max()))

    # Filter for beds
    min_beds = st.slider('Minimum Beds', min_value=0, max_value=int(df['beds'].max()), value=0)
    max_beds = st.slider('Maximum Beds', min_value=min_beds, max_value=int(df['beds'].max()), value=int(df['beds'].max()))

    # Filter for price
    min_price = st.slider('Minimum Price', min_value=0, max_value=int(df['price'].max()), value=0)
    max_price = st.slider('Maximum Price', min_value=min_price, max_value=int(df['price'].max()), value=int(df['price'].max()))

    # Filter for review_scores_rating
    min_rating = st.slider('Minimum Review Score Rating', min_value=0, max_value=int(df['review_scores_rating'].max()), value=0)
    max_rating = st.slider('Maximum Review Score Rating', min_value=min_rating, max_value=int(df['review_scores_rating'].max()), value=int(df['review_scores_rating'].max()))

    # Filter for bathrooms
    min_bathrooms = st.slider('Minimum Bathrooms', min_value=0, max_value=int(df['bathrooms'].max()), value=0)
    max_bathrooms = st.slider('Maximum Bathrooms', min_value=min_bathrooms, max_value=int(df['bathrooms'].max()), value=int(df['bathrooms'].max()))

    # Filter the dataframe based on user inputs
    filtered_df = df[(df['city'] == selected_city) &
                    (df['accommodates'] >= min_accommodates) & (df['accommodates'] <= max_accommodates) &
                    (df['number_of_reviews'] >= min_reviews) & (df['number_of_reviews'] <= max_reviews) &
                    (df['bedrooms'] >= min_bedrooms) & (df['bedrooms'] <= max_bedrooms) &
                    (df['beds'] >= min_beds) & (df['beds'] <= max_beds) &
                    (df['price'] >= min_price) & (df['price'] <= max_price) &
                    (df['review_scores_rating'] >= min_rating) & (df['review_scores_rating'] <= max_rating) &
                    (df['bathrooms'] >= min_bathrooms) & (df['bathrooms'] <= max_bathrooms)]

    # Display the filtered dataframe
    for idx, accommodation in filtered_df.iterrows():
        st.subheader(f'Recommended Accommodation {idx}')
        st.markdown(f"## [{accommodation['name']}]({accommodation['listing_url']})")
        st.markdown("Accommodation Description: " + accommodation['description'], unsafe_allow_html=True)
        st.markdown("Accommodation City: " + accommodation['city'])
        st.markdown("Accommodates: " + str(accommodation['accommodates']))
        st.markdown("Number of Reviews: " + str(accommodation['number_of_reviews']))
        st.markdown("Bedrooms: " + str(accommodation['bedrooms']))
        st.markdown("Beds: " + str(accommodation['beds']))
        st.markdown("Price: " + str(accommodation['price']))
        st.markdown("Review Scores Rating: " + str(accommodation['review_scores_rating']))
        st.markdown("Bathrooms: " + str(accommodation['bathrooms']))
        
        # Display image if picture_url is available
        if 'picture_url' in accommodation:
            st.image(accommodation['picture_url'], caption='Accommodation Image', use_column_width=True)

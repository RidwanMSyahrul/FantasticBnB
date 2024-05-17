import pickle
import streamlit as st
import pandas as pd

def app():
    st.header('FantasticBnB')
    st.subheader('AirBnB Accommodation Recommender System')

    df = pd.read_csv('listings_clustered.csv', low_memory=False)
    similarity = pickle.load(open('rec_sys.pkl','rb'))

    df_rec = pd.DataFrame(similarity, index=df['name'], columns=df['name'])

    def sorting(name, city=None):
        if city:
            tmp = df_rec[(df['city'] == city) & (df['name'] != name)].nlargest(5, name)
        else:
            tmp = df_rec[df['name'] != name].nlargest(5, name)
        return tmp.index.tolist()

    # Select box for choosing name
    name_options = df['name'].tolist()
    selected_name = st.selectbox('Select your preferred accommodation:', name_options)

    # Dropdown list for city
    city_options = ['None'] + df['city'].unique().tolist()
    selected_city = st.selectbox('Select your preferred city:', city_options)

    # Button to trigger recommendation
    if st.button('Show Recommendation'):
        recommended_accommodations = sorting(selected_name, selected_city if selected_city != 'None' else None)
        for idx, accommodation in enumerate(recommended_accommodations, start=1):
            st.subheader(f'Recommended Accommodation {idx}')
            st.text("Accommodation Description: " + accommodation['description'])
            st.text("Accommodation City: " + accommodation['city'])
            st.text("Accommodates: " + str(accommodation['accommodates']))
            st.text("Number of Reviews: " + str(accommodation['number_of_reviews']))
            st.text("Bedrooms: " + str(accommodation['bedrooms']))
            st.text("Beds: " + str(accommodation['beds']))
            st.text("Price: " + str(accommodation['price']))
            st.text("Review Scores Rating: " + str(accommodation['review_scores_rating']))
            st.text("Bathrooms: " + str(accommodation['bathrooms']))
            
            # Display image if picture_url is available
            if 'picture_url' in accommodation:
                st.image(accommodation['picture_url'], caption='Accommodation Image', use_column_width=True)
# FantasticBnB
## Fantastic 4 - Final Project (Batch RMT-029, Group 02)

![logo](https://github.com/FTDS-assignment-bay/p2-final-project-fantastic-four/blob/main/f4_logo.png)

## By:
- Data Scientist:
    1. Lukas Djajakirana - [Github](https://github.com/lukasadk) - [LinkedIn](https://www.linkedin.com/in/lukas-adiwijaya-djajakirana-66b20720a/)
    2. Rizqy Agusta Primananda - [Github](https://github.com/rizqyagusta) - [LinkedIn](https://www.linkedin.com/in/rizqy-agusta-primananda-968a70141/)
- Data Engineering:
    1. Ridwan Muhammad Syahrul - [Github](https://github.com/RidwanMSyahrul) - [LinkedIn](https://www.linkedin.com/in/ridwan-muhammad-syahrul-4419ba300/)
- Data Analyst:
    1. Siti Sofiah Ramadhany - [Github](https://github.com/sofiahra) - [LinkedIn](https://www.linkedin.com/in/sofiah-ramadhany-85980a2aa/)

# Introduction
Travelers around the world is always looking for a place for them to rest their body and soul after such a long day doing their activities and thus they will find a comfortable place to completely recharge their energy back for better tomorrow. Although the amount of choices available are vast and vary that sometimes makes them confused to choose a place to stay. With FantasticBnB, travelers won't need to worry about where to stay because in this app, you could search the best place you can stay based on your preference! We will recommend you to the best offer we can find for you!

## Objective
The objective of this project is to create an accurate recommender system based on user input preference of AirBnB description with the help of clustering to determine which AirBnB is for low-cost and high-cost.


## Jobdesk
### Data Scientist (DS)
- Model creation is where DS creates models; Recommeder System and Clustering.
- Model deployment is where DS deploys the models that were made into HuggingFace for it to be used by user.

### Data Engineer (DE)
- Data Collecting is where DE collects USA AirBnB data from Kaggle. The data itself contains AirBnB list from 31 different cities in the USA from the year 2023.
- Data Cleaning is where DE clean the data; handling inconsistency of the data, handling duplicate data, filtering features that will be used by DA or DS, and handling missing values.

### Data Analyst (DA)
- Visualization is where DA visualize the data features that affect the clusters.
- Reporting is where DA make a deep analysis and give insights from the collected data.

Dashboard: [Click Here!](https://lookerstudio.google.com/reporting/10246f2e-ef11-4fb1-bd99-9dfefe9a0d69)

Deployment - FantasticBNB: [Click Here!](https://huggingface.co/spaces/ragprim/FantasticBNB)

## File info
### Main Folder:
- clustering.ipynb: This script consist of clustering model for the dataset and app.
- recommender_system.ipynb: This script consist of recommender system model for the dataset and app.
- de_data_baru.ipynb: This script consist of code for cleaning the dataset acquired.
- listings_cleaned_new.csv: This is the cleaned dataset acquired from de_data_baru.ipynb script.
- listings_clustering.csv: This is the dataset after being used in clustering.ipynb script.
- EDA_after_2_clustering.ipynb: This script consist of Exploratory Analysis of the data after it being clustered into 2 classes.
- EDA_after_3_clustering.ipynb: This script consist of Exploratory Analysis of the data after it being clustered into 3 classes.
- f4_logo.png: This is the logo picture for the app.
- url.txt: This text consist of links for deployment, dashboard, and powerpoint.
### Deployment Folder:
- app.py: This script will launch the application by calling other scripts such as eda.py, filtering.py, and prediction.py.
- eda.py: This script consist of Exploratory Analysis of the data that will be shown in the app.
- filtering.py: This script will act as the filter for users input on the app to give AirBnB recommandation based on it.
- listing_clustered.csv: This is the cleaned and clustered AirBnB dataset for the app to use.
- requirements.txt: This is the library list for huggingface to use for the app to work.
### dags Folder:
-F4_FP_DAG.py: This script consist of Directed Acyclic Graph, pipeline to do ETL on the dataset in Apache Airflow.

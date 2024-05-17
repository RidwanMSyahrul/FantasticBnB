# libraries
import pandas as pd
import numpy as np
import psycopg2 as db
import datetime as dt
from airflow import DAG
from elasticsearch import Elasticsearch
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def fetch_data(database, table):
	'''
		Fungsi ini digunakan untuk mengambil data dari postgreSQL

		Parameters:
		database : string - nama database dimana data disimpan
		table : string - nama table dimana data disimpan

		Output
		file dari hasil query

		Contoh penggunaan :
		df = fecthData('final_project', 'teacher_salary')
	'''
	conn_string=(f"dbname='{database}' host='postgres' user='airflow' password='airflow' port='5432'")
	# try:
	conn=db.connect(conn_string)

	df=pd.read_sql(f"select * from {table}", conn)
	df.to_csv('fetch_data.csv',index=False)
	# except Exception as e:
	# 	print(f"Connection failed: {e}")

def cleaning_data():
	'''
		Fungsi ini digunakan untuk filter data (pemilihan kolom) dan data cleaning, seperti handling missing value, duplicate, dan penamaan kolom
		dataset yang tidak konsisten (seperti terdapat huruf yang uppercase, memiliki spasi antar kata yang akan
		diganti dengan tanda '_'. Akan tetapi, pada dataset ini, yang menjadi problem hanya uppercase saja)

		Parameters:
		- 

		Output :
		Data dari query SQL yang sudah melewati proses data cleaning

		Contoh penggunaan :
		file_name = cleaning_data(df)
	'''
	# try :
	df=pd.read_csv('fetch_data.csv')

	# Handling data duplicate
	dup_data = df.duplicated().sum()
	if dup_data == 0:
		print(f"Data memiliki {dup_data} duplicate")
	else:
		print(f"Data memiliki {dup_data} duplicate")

		df.drop_duplicates(inplace=True)
		dup_clean = df.duplicated().sum()

		print(f"Data memiliki {dup_clean} duplicate setelah data cleaning")
	
	# Filter data yang akan digunakan ke dalam dataframe baru
	dataset = df[['id', 'listing_url', 'picture_url', 'name', 'description','city',
       'property_type', 'room_type', 'accommodates', 'bathrooms_text', 'bedrooms', 
	   'beds', 'price', 'instant_bookable','number_of_reviews','review_scores_rating', 
       'latitude', 'longitude']].copy()

	# Mengelompokan kolom numerik atau kategorik
	numerik = dataset.select_dtypes(exclude=['object', 'datetime64']).columns.tolist()
	kategorik = dataset.select_dtypes(include=['object']).columns.tolist()

	# Handling data missing values
	miss_val = dataset.isnull().sum()

	if miss_val.sum() == 0:
		print(f"Data memiliki {miss_val.sum()} missing values")
	else:
		print(f"Data memiliki {miss_val.sum()} missing values")
		dataset.dropna(inplace=True)
		# for col in numerik:
		# 	dataset[col].fillna(dataset[col].median(), inplace=True)
		
		# for col in kategorik:
		# 	dataset[col].fillna("None", inplace=True)

		print(f"Data memiliki {miss_val.sum()} missing values setelah data cleaning")

	# Replace text values dalam kolom 'bathrooms_text' dengan numeric values pada kolom 'bathrooms'
	dataset['bathrooms'] = dataset['bathrooms_text'].str.extract(r'(\d+\.?\d?)').astype(float)

	# Drop kolom original 'bathrooms_text' 
	dataset.drop(columns=['bathrooms_text'], inplace=True)

	# Replace text '$' dan ',' pada kolom 'price' serta mengganti tipe data dari 'object' menjadi 'float'
	dataset['price'] = dataset['price'].str.replace('[$,]', '', regex=True).astype(float)

	# Replace null value pada kolom 'bathrooms' menjadi 0.5
	'''
		Hal ini dilakukan karena pada kolom bathroom_text, terdapat value 'half-bath' dan 'shared half-bath'
		dan diindikasikan sebagai value 0.5
	'''
	dataset['bathrooms'].replace(np.nan, 0.5, inplace=True)	

	# Handling nama kolom yang tidak konsisten
	df_collist_clean = []

	df_collist = dataset.columns.tolist()

	for column in df_collist:
		column = column.lower()

		df_collist_clean.append(column)

	n = 0  

	for column in df_collist:
		dataset.rename(columns={column:df_collist_clean[n]}, inplace=True)
		n+=1

	dataset.to_csv('/opt/airflow/dags/FP_listings_data_cleaned.csv', index = False)
		# dfClean = dataset.copy()
		# dfClean.to_csv(file_name)
	# except Exception as e:
	# 	print(f"Data Cleaning failed: {e}")

def upload_data(url):
	'''
		Fungsi ini digunakan untuk upload data dari hasil data cleaning ke elasticsearch

		Parameters:
		url : string - link tujuan upload
		file : string - nama file yang ingin diupload 

		Output
		File di upload ke elasticsearch

		Contoh penggunaan :
		upload_status = upload_data('http://elasticsearch:9200', dataset.csv)
	'''
	es = Elasticsearch(url) 
	df=pd.read_csv('/opt/airflow/dags/FP_listings_data_cleaned.csv')
	# try:
	for i,r in df.iterrows():
		doc=r.to_json()
		res=es.index(index="data_fp", doc_type="doc", body=doc)
		print(res)
	# except Exception as e:
	# 	print(f"Upload to elasticsearch failed: {e}")

default_args = {
    'owner': 'fantastic_four',
    'start_date': dt.datetime(2024, 5, 8),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}


with DAG('final_project',
        default_args=default_args,
        schedule_interval='0 0 1 * *'       
        ) as dag:

    print_start = BashOperator(task_id='starting',
                               bash_command='echo "Start Proses DAG....."')
    
    load_data = PythonOperator(task_id='fetch_data_postgres',
                                 python_callable=fetch_data,
								 op_args=['airflow', 'table_fp2'])

    print_clean = BashOperator(task_id='cleaning',
                               bash_command='echo "Cleaning Data now....."')

    clean_data = PythonOperator(task_id='data_cleaning',
                                 python_callable=cleaning_data)

    print_upload = BashOperator(task_id='uploading',
                               bash_command='echo "Upload Data now....."')

    uploading_data = PythonOperator(task_id='data_uploading',
                                 python_callable=upload_data,
								 op_args=['http://elasticsearch:9200'])
	
print_start >> load_data >> print_clean >> clean_data >> print_upload >> uploading_data
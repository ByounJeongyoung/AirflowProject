# 완성
from airflow import DAG
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.models import BaseOperator
from airflow.hooks.base_hook import BaseHook
from create.CreateS3Orders import S3_WriteData
from read.ReadS3Orders import ReadS3OrdersData
import pendulum
import pandas_gbq
from google.oauth2 import service_account
from datetime import datetime
from pandas.core.frame import DataFrame
import json
import os


with DAG(
    dag_id='test01',
    schedule_interval='00 00 * * *',
    start_date=pendulum.datetime(2023, 9, 10, tz="Asia/Seoul"),
    catchup=False,
    tags=['OrdersRetention']
) as dag:
    t1 = PythonOperator(
        task_id ='S3Write',
        python_callable = S3_WriteData
    )
    t2 = PythonOperator(
        task_id='S3Read',
        python_callable= ReadS3OrdersData
    )
    end = DummyOperator(task_id="end")

    t1 >> t2 >> end


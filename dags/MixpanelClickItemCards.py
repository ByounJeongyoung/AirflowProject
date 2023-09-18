# 완성
from airflow import DAG
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.models import BaseOperator
from airflow.hooks.base_hook import BaseHook
import pendulum
from airflow.decorators import task, dag
from create.CreateS3Orders import S3_WriteData
from read.ReadS3Orders import ReadS3OrdersData
from read.Mixpanel.ReadClickItemCard import ClickItemCardReport
from google.oauth2 import service_account
#import pandas_gbq
from datetime import datetime
from pandas.core.frame import DataFrame
import json
import os


with DAG(
    dag_id='MixpanelData',
    schedule_interval='* * * * *',
    start_date=pendulum.datetime(2023, 9, 10, tz="Asia/Seoul"),
    catchup=False,
    tags=['OrdersRetention']
) as dag:
    @task(task_id ='Mixpanel')
    def Mixpanel():
        clickItemData = ClickItemCardReport()
        return clickItemData

    Mixpanel = Mixpanel()



import pandas_gbq
import pandas as pd
from datetime import datetime
from google.oauth2 import service_account
from google.cloud import bigquery
import sys
import os
from ReadS3Orders import ReadS3OrdersData

current_dir = os.path.dirname(__file__)
airflow_work_dir = os.path.abspath(os.path.join(current_dir, '../files/voltaic-triode-347814-58f14c2bf11d.json'))  # 상위 디렉토리


def updateToBigQuery():

    data = ReadS3OrdersData()
    data = pd.DataFrame(data)

    cd = service_account.Credentials.from_service_account_file(
        airflow_work_dir,
    )
    data['createdAt'] = pd.to_datetime(data['createdAt']) #S3에서 읽을때 변환을 해줘야 함

    project_id = 'voltaic-triode-347814'
    dataset_id = 'personal'
    table_id = 'wingeat_data_dateTime'

    # DB 저장소
    destination_table = f"{project_id}.{dataset_id}.{table_id}"
    # 업로드
    data.to_gbq(destination_table, project_id=project_id, if_exists='replace', credentials=cd)

    print('migration complete')
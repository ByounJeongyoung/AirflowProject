import pandas_gbq
from google.oauth2 import service_account
from datetime import datetime
from pandas.core.frame import DataFrame
import json
from glob import glob
import os

# 현재 파일의 경로를 기반으로 작업 디렉토리 설정
current_dir = os.path.dirname(__file__)
airflow_work_dir = os.path.abspath(os.path.join(current_dir, '../files/voltaic-triode-347814-58f14c2bf11d.json'))  # 상위 디렉토리

project_id = 'voltaic-triode-347814'
dataset_id = 'personal'
table_id = 'wingeat_data_dateTime'

#권한 설정
cd = service_account.Credentials.from_service_account_file(
    airflow_work_dir
    )
# data를 사용하여 작업 수행
def MaxCreatedAtFunc() -> datetime:

    pandas_gbq.context.credentials = cd
    pandas_gbq.context.project = project_id

    #테이블 read (최신값)
    df = pandas_gbq.read_gbq(f"""
    SELECT MAX(createdAt) FROM `{project_id}.{dataset_id}.{table_id}` 
    """)

    #컬럼 지정, deafault F0
    df.columns = ['max_createdAt']
    max_createdAt = df.loc[0,'max_createdAt'] #DataFrame에서 value추출
    date_string = f"{max_createdAt}"
    date_obj = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")

    return date_obj


import boto3
import pandas as pd
import io
import sys
import os
from io import StringIO
from pandas.core.frame import DataFrame
from google.oauth2 import service_account
from google.cloud import bigquery
import pandas_gbq


def ReadS3OrdersData(fileName): #-> DataFrame:

    year = fileName.year
    month = fileName.month
    day = fileName.day
    hour = fileName.hour

    s3 = boto3.client('s3',
                      region_name="ap-northeast-2",
                      aws_access_key_id="AKIA2EHO5GXPEW2W5S37",
                      aws_secret_access_key="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",)
    bucket = 'wingeatdata'
    obj = s3.get_object(Bucket=bucket, Key= f"practice/{year}-{month}-{day}-{hour}.csv")
    df = pd.read_csv(io.BytesIO(obj["Body"].read()))
    print("S3에서 파일을 읽었습니다.아래는 다운받은 데이터 입니다.")

    current_dir = os.path.dirname(__file__)
    airflow_work_dir = os.path.abspath(
        os.path.join(current_dir, '../files/voltaic-triode-347814-58f14c2bf11d.json'))  # 상위 디렉토리

    data = pd.DataFrame(df)

    cd = service_account.Credentials.from_service_account_file(
            airflow_work_dir,
        )
    data['createdAt'] = pd.to_datetime(data['createdAt'])  # S3에서 읽을때 변환을 해줘야 함

    project_id = 'voltaic-triode-347814'
    dataset_id = 'personal'
    table_id = 'wingeat_data_dateTime'

    # DB 저장소
    destination_table = f"{project_id}.{dataset_id}.{table_id}"
    # 업로드
    data.to_gbq(destination_table, project_id=project_id, if_exists='append', credentials=cd)

    print('migration complete')

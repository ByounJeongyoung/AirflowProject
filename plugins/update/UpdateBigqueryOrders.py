from google.oauth2 import service_account
import pandas_gbq
import pandas as pd
from datetime import datetime
from google.oauth2 import service_account
from google.cloud import bigquery
import sys
import os
a_py_path = os.path.join('/plugins/read') # 파일의 절대 경로 계산
sys.path.append(a_py_path)
from ReadS3Orders import ReadS3OrdersData

data = ReadS3OrdersData()
# print(data)
# print(type(data))
data = pd.DataFrame(data)
#json key 경로
# json key 경로
cd = service_account.Credentials.from_service_account_file(
    "../files/voltaic-triode-347814-58f14c2bf11d.json",
)
data['createdAt'] = pd.to_datetime(data['createdAt']) #S3에서 읽을때 변환을 해줘야 함
#data.info()

project_id = 'voltaic-triode-347814'
dataset_id = 'personal'
table_id = 'wingeat_data_timeStamp'

# DB 저장소
destination_table = f"{project_id}.{dataset_id}.{table_id}"

# 업로드
data.to_gbq(destination_table, project_id=project_id, if_exists='append', credentials=cd)
cd = service_account.Credentials.from_service_account_file(
    "../files/voltaic-triode-347814-58f14c2bf11d.json",
    )

project_id = 'voltaic-triode-347814'
dataset_id = 'personal'
table_id = 'wingeat_data_dateTime'

# DB 저장소
destination_table = f"{project_id}.{dataset_id}.{table_id}"

# 업로드
data.to_gbq(destination_table, project_id=project_id, if_exists='replace', credentials=cd)
print('migration complete')
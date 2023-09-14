# 쓰기
import boto3
from io import StringIO
import pandas as pd
from datetime import datetime
from read.ReadMongoOrders import DataLoad


# df = DataLoad()
# S3LoadTime = pd.to_datetime(df['createdAt'].max())
# S3LoadTimeString = datetime.strptime(f'{S3LoadTime}', "%Y-%m-%d %H:%M:%S.%f")
#
#     # 각 부분 추출
# year = S3LoadTimeString.year
# month = S3LoadTimeString.month
# day = S3LoadTimeString.day
# hour = S3LoadTimeString.hour

def S3_Connection():
    try:
        # s3 클라이언트 생성
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id="AKIA2EHO5GXPEW2W5S37",
            aws_secret_access_key="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",
        )
    except Exception as e:
        print(e)
    else:
        print("s3 bucket connected!")
        return s3

def S3_WriteData():
    df = DataLoad()
    S3LoadTime = pd.to_datetime(df['createdAt'].max())
    S3LoadTimeString = datetime.strptime(f'{S3LoadTime}', "%Y-%m-%d %H:%M:%S.%f")

    # 각 부분 추출
    year = S3LoadTimeString.year
    month = S3LoadTimeString.month
    day = S3LoadTimeString.day
    hour = S3LoadTimeString.hour

    s3 = S3_Connection()
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    task = csv_buffer.getvalue()

    bucket_name = "wingeatdata"  # 사용할 S3 버킷 이름 입력
    s3_key = f"practice/{year}-{month}-{day}-{hour}.csv"  # S3 버킷 내 저장할 경로 및 파일 이름 입력
    # print(s3_key)
    # print(df)
    try:
    # 문자열로 변환한 데이터를 S3에 업로드
        s3.put_object(Bucket=bucket_name, Key=s3_key, Body=task.encode())
        print(f'데이터가 S3 버킷 {bucket_name}의 {s3_key} 위치에 저장되었습니다.')
    except Exception as e:
        print(e)

    print(f'----------------------------------------------------------{S3LoadTimeString}')
    return S3LoadTimeString





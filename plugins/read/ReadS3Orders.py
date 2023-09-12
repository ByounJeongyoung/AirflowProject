import boto3
import pandas as pd
import io
from io import StringIO
from pandas.core.frame import DataFrame

def ReadS3OrdersData(): #-> DataFrame:

    # fileName = FileInformation()
    # print(fileName)
    # year = fileName.year
    # month = fileName.month
    # day = fileName.day
    # hour = fileName.hour

    s3 = boto3.client('s3',
                      region_name="ap-northeast-2",
                      aws_access_key_id="****************",
                      aws_secret_access_key="****************",)
    bucket = 'wingeatdata'
    obj = s3.get_object(Bucket=bucket, Key= f"practice/{year}-{month}-{day}-{hour}.csv")
    df = pd.read_csv(io.BytesIO(obj["Body"].read()))
    print("S3에서 파일을 읽었습니다.아래는 다운받은 데이터 입니다.")
    print(df)

    return df

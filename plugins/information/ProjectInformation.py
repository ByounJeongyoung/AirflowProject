from enum import Enum

class Mixpanel_information(Enum):

    authorization = 'Basic amVvbmd5b3VuZy42ZWY4YzAubXAtc2VydmljZS1hY2NvdW50OjAwWUZ4eWVWa3VvZ0JvQ1YyMmVYRE4xRjcwVmxrTDZx'
    clickItemCardInsightBoard = 'https://mixpanel.com/api/2.0/insights?project_id=1353777&bookmark_id=44284676'

class S3_information(Enum):

    service_name = "s3"
    region_name = "ap-northeast-2"
    aws_access_key_id = "AKIA2EHO5GXPEW2W5S37"
    aws_secret_access_key = "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"

class Bigquery_information(Enum):

    project_id = 'voltaic-triode-347814'
    dataset_id = 'personal'
    table_id = 'wingeat_data_dateTime'
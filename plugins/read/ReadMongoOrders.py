import pandas as pd
from datetime import datetime
from pandas.core.frame import DataFrame
from read.ReadBigqueryOrders import MaxCreatedAtFunc
from pymongo import MongoClient

order_inform = [] #DB조회 값을 저장

def DataLoad() -> DataFrame:

    MaxCreatedAt = MaxCreatedAtFunc()
    # 각 부분 추출
    year = MaxCreatedAt.year
    month = MaxCreatedAt.month
    day = MaxCreatedAt.day
    hour = MaxCreatedAt.hour
    minute = MaxCreatedAt.minute
    second = MaxCreatedAt.second
    microsecond = MaxCreatedAt.microsecond

    client = MongoClient(
        '************************************')
    db = client.fresh

    start_date = datetime(year, month, day,hour,minute,second,microsecond)    #임의 지정
    orders_collection = db.orders.find({'createdAt': {"$gte": start_date}},
                                       {'_id': 1,
                                        'realPaidPrice': 1,
                                        'payment': 1,
                                        'state': 1,
                                        "createdAt": 1}
                                       )
    for order in orders_collection:
        order_inform.append(order)

    df = pd.DataFrame(order_inform)

    df_flatten = df.join(pd.json_normalize(df['payment']).add_prefix('payment_')).drop(columns=['payment'])
    dfColumn = df_flatten[['_id', 'createdAt', 'payment_state', 'state', 'realPaidPrice']]
    DfColumnFiltering = dfColumn[dfColumn['payment_state'] == 'PAID']
    print(DfColumnFiltering)

    return DfColumnFiltering

DataLoad()
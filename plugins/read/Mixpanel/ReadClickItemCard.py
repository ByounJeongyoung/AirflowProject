import requests
import pandas as pd
import json
import pprint
from pandas import json_normalize
from information.ProjectInformation import Mixpanel_information

def ClickItemCardReport():

    url = Mixpanel_information.clickItemCardInsightBoard.value
    headers = {
        "accept": "application/json",
        "authorization": Mixpanel_information.authorization.value
    }

    response = requests.get(url, headers=headers).json()
    information = response["series"]['상품 카드 클릭 - Total']

    df_list = []

    for product_id, dates in information.items():
        for date, clicks in dates.items():
            df_list.append((product_id, date, clicks))

    clickitemCardsData = pd.DataFrame(df_list, columns=['상품명', '일자', '상품 클릭수'])
    return clickitemCardsData

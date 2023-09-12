FROM ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.7.0}

RUN pip install pandas \
    && pip install boto3 \
    && pip install google-auth \
    && pip install google-auth-oauthlib \
    && pip install google-cloud-bigquery \
    && pip install google-cloud-bigquery-storage \
    && pip install google-cloud-core \
    && pip install google-crc32c \
    && pip install google-resumable-media \
    && pip install googleapis-common-protos \
    && pip install pandas-gbq \
    && pip install pymongo \


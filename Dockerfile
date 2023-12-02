# https://airflow.apache.org/docs/docker-stack/build.html#adding-new-pypi-packages-individually
FROM apache/airflow:2.7.3
COPY requirements.txt /
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt
RUN ipython kernel install --name "python3" --user

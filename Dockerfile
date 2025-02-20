# https://github.com/Kaggle/docker-python/releases
FROM gcr.io/kaggle-private-byod/python:v158

RUN pip install --no-cache-dir \
    hydra-core 
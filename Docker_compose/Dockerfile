FROM python:3.11-slim as base

ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} \
     && useradd -r -g ${APP_USER} ${APP_USER}

WORKDIR /opt/app


FROM base as python_smit_base
WORKDIR /opt/app/python_smit_api

COPY --chown=${APP_USER}:${APP_USER} --chmod=755 ./backend .

RUN  pip install -r requirements.txt --no-cache-dir

USER ${APP_USER}:${APP_USER}


FROM python_smit_base as python_smit_dev

CMD ["python", "main.py"]


FROM python_smit_base as python_smit_prod

ARG FASTAPI_PORT
ENV ENV_FASTAPI_PORT $FASTAPI_PORT

CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$ENV_FASTAPI_PORT


FROM base as tests
WORKDIR /opt/app/tests

COPY --chown=${APP_USER}:${APP_USER} --chmod=755 ./tests .
RUN  pip install -r requirements.txt --no-cache-dir

USER ${APP_USER}:${APP_USER}

CMD [ "pytest" ]
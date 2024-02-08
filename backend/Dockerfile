FROM python:3.12
# ARG DB_HOST
# ARG DB_PORT
# ARG DB_USER
# ARG DB_PASS
# ARG DB_NAME

# ENV DB_HOST=$DB_HOST
# ENV DB_PORT=$DB_PORT
# ENV DB_USER=$DB_USER
# ENV DB_PASS=$DB_PASS
# ENV DB_NAME=$DB_NAME

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY ./app /backend/app
COPY ./__init__.py /backend/__init__.py

# RUN python /code/app/database/db_init.py 

EXPOSE 8000
COPY ./entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]

CMD ["sh"]

# CMD [ "python", "/code/app/database/db_init.py" ]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


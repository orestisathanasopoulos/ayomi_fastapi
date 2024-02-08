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
COPY --from=web /ayomi-calculator/dist /backend/dist
EXPOSE 80
COPY ./entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]

CMD ["sh"]
#!/bin/sh

python /backend/app/database/db_init.py 

uvicorn app.main:app --host "0.0.0.0" --port "8000"      
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from config import config
from database.models import Base

# File: __init__.py.py
# Author: Zhou
# Date: 2023/5/18
# Copyright: 2023 Zhou
# License:
# Description:  Database
base_dir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(base_dir, '../db.sqlite')
db_url = f'sqlite:///{os.path.join(base_dir, db_file)}'
if not os.path.exists(db_file):
    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    models = config.ai_models.split(' ')
    for index, model in enumerate(models, 1):
        sql = text(f"INSERT INTO ai_model (name,is_default,is_available) VALUES ('{model}',{1 if index == 1 else 0},1)")
        session.execute(sql)
    session.commit()
    session.close()
else:
    engine = create_engine(db_url, echo=False)

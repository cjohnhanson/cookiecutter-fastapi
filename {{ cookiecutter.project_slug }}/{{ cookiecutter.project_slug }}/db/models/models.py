# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2019 Cody J. Hanson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, Boolean, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Connection(Base):
    __tablename__ = "connections"
    id = Column(Integer, primary_key=True, index=True)
    conn_id = Column(String, unique=True)
    conn_type = Column(String)
    host = Column(String)
    port = Column(Integer)
    login = Column(String)
    password = Column(String)
    is_encrypted = Column(Boolean)
    is_extra_encrypted = Column(Boolean)
    extra = Column(String)

class RedshiftTableColumn(Base):
    NotImplemented

class RedshiftTable(Base):
    __tablename__ = "redshift_tables"
    schemaname = Column(String)
    tablename = Column(String)
    #TODO

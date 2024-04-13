import datetime
import sqlalchemy
from sqlalchemy import orm


from db_session import SqlAlchemyBase


class Task(SqlAlchemyBase):
    __tablename__ = 'goods'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    amount = sqlalchemy.Column(sqlalchemy.Integer)
    category_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("categories.id"))
    summa = sqlalchemy.Column(sqlalchemy.Integer)

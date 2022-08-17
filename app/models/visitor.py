from sqlalchemy import Column, String, Integer, orm
from app.models.base import Base


class Visitor(Base):
    seq = Column(Integer, primary_key=True, autoincrement=True) # id自增长
    id = Column(String(18), unique = True, nullable=False) # 身份证号码
    _password = Column('password', String(12))
    name = Column(String(15), nullable=False)
    gender = Column(String(2), nullable=False)
    teleNum = Column(String(11), nullable=False)
    homeAddress = Column(String(80), nullable=False)

	# def __init__(self, seq, id, password, name, gender, teleNum, homeAddress):
	# 	self.seq = seq
	# 	self.id = id
	# 	self.password = password
	# 	self.name = name
	# 	self.gender = gender
	# 	self.teleNum = teleNum
	# 	self.homeAddress = homeAddress
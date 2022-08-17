from sqlalchemy import Column, String, Integer, DateTime, orm
from app.models.base import Base

class VisitHistory(Base):
	recordID = Column(Integer, primary_key=True, autoincrement=True) # id自增长
	seq = Column(Integer, nullable=False)
	arrivalTime = Column(DateTime, nullable=False)
	depatureTime = Column(DateTime, nullable=True)

	# def __init__(self, recordID, seq, arrivalTime, depatureTime):
	# 	self.recordID = recordID
	# 	self.seq = seq
	# 	self.arrivalTime = arrivalTime
	# 	self.depatureTime = depatureTime
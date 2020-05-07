from sqlalchemy import create_engine,Column,String,Float,Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Momo(Base):
        __tablename__ = 'momo'
        id = Column('Mobile Number',Integer,primary_key=True)
        name = Column('Full Name',String,nullable=False)
        bal = Column('Account Balance',Float,default=0.0)
        pin = Column('Secret Code',Integer,nullable=False)


engine = create_engine('sqlite:///momo.db',echo=True)


if __name__ == '__main__':
        
    Base.metadata.create_all(bind=engine)

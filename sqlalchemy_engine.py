from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column
from sqlalchemy import create_engine
import settings

Base = declarative_base()


class Engine:

    @staticmethod
    def create_engine():
        engine = create_engine(settings.connection, echo=True)
        return engine


class Ticket(Base):

    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    redmine_id = Column(Integer)
    tracker = Column(String(255))
    status = Column(String(100))
    priority = Column(String(10))
    subject = Column(String(255))
    assigned_to = Column(String(100))

    def __init__(self, redmine_id, tracker, status, priority, subject, assigned_to):
        self.redmine_id = redmine_id
        self.tracker = tracker
        self.status = status
        self.priority = priority
        self.subject = subject
        self.assigned_to = assigned_to

    def __repr__(self):
        return "<Ticket(redmine_id=%s, subject=%s, status=%s, assigned_to=%s)>" % (self.redmine_id, self.subject, self.status, self.assigned_to)


if __name__ == '__main__':
    ticket_table = Ticket.__tablename__
    metadata = Base.metadata
    metadata.create_all(Engine.create_engine())

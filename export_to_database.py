from sqlalchemy_engine import Ticket, Engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=Engine.create_engine())()


def update_database(data):
    tickets = []
    for item in data:
        redmine_id = item.get('id')
        tracker = item.get('tracker')
        status = item.get('status')
        priority = item.get('priority')
        subject = item.get('subject')
        assigned_to = item.get('assigned_to')
        ticket = Ticket(redmine_id=redmine_id,
                        tracker=tracker,
                        status=status,
                        priority=priority,
                        subject=subject,
                        assigned_to=assigned_to)
        tickets.append(ticket)

    session.add_all(tickets)
    session.commit()

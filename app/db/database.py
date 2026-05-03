#connecting to database
#creating sessions

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///portfolio.db")


# create session
sessionLocal= sessionmaker(
    autocommit = False,
    autoflush=False,
    bind = engine
)

# connection lifecycle (open->use->close)
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()



from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
import sqlalchemy.orm


DATABASE_URL="postgresql://nithit24:car24@localhost:5432/notification_db"
engine = create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base = sqlalchemy.orm.declarative_base()
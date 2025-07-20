from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import settings


engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(engine, autoflush=False, autocommit=False)
Base = declarative_base()

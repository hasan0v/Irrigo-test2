from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from alembic import context
import PyMySQL  # Make sure PyMySQL is installed

# Import your SQLAlchemy models
from models import Base  # Import Base from your models file

config = context.config
config.set_main_option('sqlalchemy.url', 'mysql+pymsql://admin:irrigo_DB@irrigo-db.cvweo26seous.us-east-2.rds.amazonaws.com/irrigo-db')

target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

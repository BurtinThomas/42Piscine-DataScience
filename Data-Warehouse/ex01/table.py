import pandas as pd
from sqlalchemy import (
    UUID,
    BigInteger,
    create_engine,
    MetaData,
    DateTime,
    Float,
    Integer,
    String
)

def is_table_exist(engine, table_name):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    if table_name in metadata.tables:
        print(f"Table {table_name} already exist.")
    return table_name in metadata.tables

def create_table(path, table_name):
    try:
        engine = create_engine("postgresql://tburtin:toto@localhost:5432/piscineds")

        if not is_table_exist(engine, table_name):
            print(f"Creating table {table_name}...")
            data = pd.read_csv(path)
            data_types = {
                'event_time': DateTime(),
                'event_type': String(length=255),
                'product_id': Integer(),
                'price': Float(),
                'user_id': BigInteger(),
                'user_session': UUID(as_uuid=True)
            }
            data.to_sql(table_name, engine, index=False, dtype=data_types)
            print(f"Table {table_name} created.")
        engine.dispose()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

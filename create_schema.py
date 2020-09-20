import sys 
from sqlalchemy import *
import config

sql_file = sys.argv[1]
createSchema = open(sql_file)

db_url = 'postgresql://{}:{}@{}:{}/{}'.format(config.PG_USERNAME,config.PG_PASSWORD,config.PG_HOST,config.PG_PORT,config.PG_DATABASE)
engine = create_engine(db_url)

create_sql = text(createSchema.read())
engine.execute(create_sql)

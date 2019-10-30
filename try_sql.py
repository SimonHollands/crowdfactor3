import os
import psycopg2

#DATABASE_URL = os.environ['DATABASE_URL']
DATABASE_URL='postgresql-slippery-99351'
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

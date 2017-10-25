import sys
import os
import logging
import rds_config
import pymysql
#rds settings
rds_host, rds_port  = os.environ['rds_endpoint'].split(":")
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name


logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def handler(event, context):

    with conn.cursor() as cur:
        cur.execute("create table IF NOT EXISTS mytable ( counterid varchar(255) NOT NULL, value int, PRIMARY KEY (counterid))")
        cur.execute("insert into mytable (counterid, value) values('counter1', 1) ON DUPLICATE KEY UPDATE value=value+1")
        conn.commit()
        cur.execute("select * from mytable where counterid='counter1'")
        row = cur.fetchone()
        current = row[1]

    return {"statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": "\"Hello World! If you see this message, it means that you successfully builded AWS API Gateway + AWS Lambda + AWS RDS Mysql with Terraform. This Lambda function was executed %d times\"" % current
        }

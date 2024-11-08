import argparse
import pymssql
from decouple import config

parser = argparse.ArgumentParser()
mxg = parser.add_mutually_exclusive_group(required=True)
mxg.add_argument("-p", "--patrimonio", metavar='patrimonio', help="patrimonio do bem patrimoniado")
mxg.add_argument("-s", "--serial", metavar='serial', help="serial do bem patrimoniado")
args = parser.parse_args()

conn = pymssql.connect(
    server = config('DB_SERVER'),
    user = config('DB_USER'),
    password = config('DB_PASSWORD'),
    database = config('DB_DATABASE')
)
cursor = conn.cursor(as_dict=True)

# serial
if (args.serial):
    query = 'SELECT numpat as cod FROM BEMPATRIMONIADO where numidfpat = %s'
    cursor.execute(query, args.serial)
elif (args.patrimonio):
    query = 'SELECT numidfpat as cod FROM BEMPATRIMONIADO where numpat = %s'
    numpat = int(args.patrimonio.replace('.',''))
    cursor.execute(query, numpat)
for row in cursor:
    print("%s"%(row['cod']))

conn.close()

import argparse
import pymssql
from decouple import config

parser = argparse.ArgumentParser()
mxg = parser.add_mutually_exclusive_group(required=True)
mxg.add_argument("-p", "--patrimonio", help="patrimonio do bem")
mxg.add_argument("-s", "--serial", help="serial do bem patrimoniado")
mxg.add_argument("-a", "--ativo", metavar='PATRIMONIO', help="patrimonio do bem")
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
    patrimonio = args.patrimonio
    numpat = int(patrimonio.replace('.',''))
    cursor.execute(query, numpat)
elif (args.ativo):
    query = 'SELECT stabem as cod FROM BEMPATRIMONIADO where numpat = %s'
    patrimonio = args.ativo
    numpat = int(patrimonio.replace('.',''))
    cursor.execute(query, numpat)

for row in cursor:
    print("%s"%(row['cod']))

conn.close()

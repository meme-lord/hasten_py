#! /usr/bin/python
from sys import argv
if len(argv)!=2:
	exit("Usage: hasten filename.sql\nHasten - Speed up SQL imports\nExample: hasten file.sql | mysql -uuser -p dbname")
sql_file = open(argv[1],'r')
print("""SET SESSION autocommit=0;
SET SESSION unique_checks=0;
SET SESSION foreign_key_checks=0;
SET SESSION sql_log_bin=0;""")
for line in sql_file:
	print(line.rstrip())
print("COMMIT;")
#The only way this could be improved is turning 1 row inserts into bulk inserts
sql_file.close()

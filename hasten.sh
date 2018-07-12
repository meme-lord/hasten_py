echo "SET SESSION autocommit=0;
SET SESSION unique_checks=0;
SET SESSION foreign_key_checks=0;
SET SESSION sql_log_bin=0;"
cat $1
echo "COMMIT;"

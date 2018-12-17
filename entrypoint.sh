#!/bin/sh
#!/bin/sh

set -e

postgres_connection() {
python << END
import sys
import psycopg2
try:
    psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}",
	port="5432"
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_connection; do
    echo Postgres connection failed, retrying in 5 secs...
    sleep 5
done

echo Postgres connection success, continuing...

flask db upgrade
exec "$@"



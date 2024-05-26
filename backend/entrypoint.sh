#!/bin/sh
# entrypoint.sh

set -e

host="$1"
shift
cmd="$@"

until nc -z -v -w30 $host 5432; do
  echo "PostgresDB is unavailable - sleeping"
  sleep 1
done

echo "PostgresDB is up - executing command"
exec $cmd
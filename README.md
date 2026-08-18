# gold-etl

สร้าง password
```bash
-join ((48..57)+(65..90)+(97..122) | Get-Random -Count 25 | % {[char]$_})
```

image volumn
```bash
docker inspect postgres:18 --format '{{range .Config.Env}}{{println .}}{{end}}' | grep PGDATA
```

check db
```sql
docker exec -it pg_db psql -U $(grep POSTGRES_USER .env | cut -d= -f2) -c "SELECT version();"
```
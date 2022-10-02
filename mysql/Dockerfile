FROM mysql:8.0

ADD tables.sql /docker-entrypoint-initdb.d

EXPOSE 3306
CMD ["mysqld"]
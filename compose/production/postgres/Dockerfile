FROM postgres:17

COPY ./compose/production/postgres/postgresql.conf /etc/postgresql/postgresql.conf
COPY ./compose/production/postgres/maintenance /usr/local/bin/maintenance

RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance

CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]

import logging

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

Base = sqlalchemy.ext.declarative.declarative_base()

__factory = None


def global_init(db_file) -> None:
    global __factory

    if __factory:
        return

    db_file = db_file.strip()

    if not db_file:
        logging.error("Необходимо указать файл базы данных")
        raise Exception("Необходимо указать файл базы данных")

    conn_str = f"sqlite:///{db_file}?check_same_thread=False"
    logging.debug(f"Подключение к базе данных по адресу {conn_str}")

    engine = sqlalchemy.create_engine(conn_str, echo=False)
    __factory = sqlalchemy.orm.sessionmaker(bind=engine)

    from . import __all_models

    Base.metadata.create_all(engine)


def create_session() -> sqlalchemy.orm.Session:
    global __factory
    return __factory()

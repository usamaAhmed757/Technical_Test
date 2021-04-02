def get_postgresql_db_credential(database, user_name, **kwargs):
    password = kwargs.get("password")
    host = kwargs.get("host")
    return  f"postgresql+psycopg2://{user_name}:{password}@{host}/{database}"

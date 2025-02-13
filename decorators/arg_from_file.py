from pathlib import Path
from functools import wraps
import duckdb

def arg_from_file(content_arg="content", encoding="utf-8"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            content = kwargs.get(content_arg)
            if content and isinstance(content, (str, Path)) and Path(content).is_file():
                with open(content, 'r', encoding=encoding) as file:
                    kwargs[content_arg] = file.read()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@arg_from_file("cmd")
def execute_duckdb_cmd(conn: duckdb.DuckDBPyConnection, cmd: str):
    return conn.execute(cmd)

@arg_from_file("query")
def execute_duckdb_query(conn: duckdb.DuckDBPyConnection, query: str):
    return conn.sql(query).fetchdf()

if __name__ == "__main__":
    conn = duckdb.connect(database="movies.ddb")

    # Create table in database
    create_table_sql = str(Path.cwd() / "sql" / "simple_create_table.sql")
    print(create_table_sql)
    
    execute_duckdb_cmd(conn, cmd=create_table_sql)

    print(conn.sql("DESCRIBE movies;"))
    # Query table
    # query_table_sql = str(Path.cwd() / "sql" / "simple_query_table.sql")
    # result = execute_duckdb_query(conn, query=query_table_sql)

    # print(result)

from connection import create_connection
from sqlite3 import Cursor, Error
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def get_task(cur: Cursor, sql) -> list[int]:
    try:
        # sql = "SELECT CHARINDEX(' ', 'SQLite substr');"
        print(cur.execute(sql).fetchall())
        # res = cur.fetchall()
        res = [ dict(line) for line in [zip([ column[0] for column in cur.description], row) for row in cur.execute(sql).fetchall()] ]
        # res =  [v[:] for v in cur.fetchall()]
        return res
    except Error as e:
        logger.error(e)


# Define a custom Python function
def reverse_string(input_str):
    return input_str[::-1]

# Define a custom Python function
def reverse_string(input_str: str) -> str:
    return input_str[::-1]

# Define a custom Python function
def find_string_char(find_char: str, input_str: str):
    return input_str.find(find_char)+1


def get_statitics():
    logger.debug("Get statitics")
    query_base_path = Path("sql")   
    result = []
    try:
        with create_connection() as conn:
            if conn is not None:
                conn.create_function("REVERSE", 1, reverse_string)
                conn.create_function("CHARINDEX", 2, find_string_char)                
                cur: Cursor = conn.cursor()
                tasks = sorted(query_base_path.glob("query_*.sql"))
                for task in tasks:
                    # query_path = query_base_path.joinpath(f"query_{task}.sql")
                    query_path = task
                    if query_path.is_file():
                        logger.debug(f"Start task №{task}")
                        result.append((f"Task №{task.stem}:", get_task(cur, query_path.read_text())))
                logger.debug(f"Finished")
                cur.close()
    except RuntimeError as err:
        logger.error(err)
    return result

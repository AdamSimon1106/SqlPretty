# sqlpretty.py
# Author - Adam Simonov
import sqlite3
import pandas as pd
import textwrap

_counter = 0

BANNER = "=" * 45
ROW_GAP = ""


def query(db_path: str, sql: str, limit: int = 5) -> str:
    """
    Run a single SQL query and return a formatted string output.
    Automatically increments the question number each time it’s called.
    If the result has more than 10 rows, show top 5 and bottom 5 rows;
    otherwise, show the entire table.

    Nicely handles multi-line SQL with indentation, e.g.:

        query(
            "world.db",
            '''
                SELECT *
                FROM City
                WHERE Population > 1000000
            '''
        )
    """
    global _counter
    _counter += 1

    # Normalize indentation and strip leading/trailing blank lines
    sql_clean = textwrap.dedent(sql).strip()

    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(sql_clean, conn)

    num_rows = len(df)

    if num_rows > 10:
        top = df.head(limit)
        bottom = df.tail(limit)
        display_df = pd.concat([top, bottom])
    else:
        display_df = df

    result = [
        BANNER,
        f"Question: {_counter}",
        "The query:",
        ROW_GAP,
        sql_clean,
        ROW_GAP,
        f"Num of rows: {num_rows}",
        "The results:",
        display_df.to_string(index=True),
        ROW_GAP,
    ]

    return "\n".join(result) + "\n"

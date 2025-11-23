# sqlpretty.py
# Author - Adam Simonov

import sqlite3
import pandas as pd
import textwrap

_counter = 0

BANNER = "=" * 45
ROW_GAP = "\n"


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
        sql_clean,
        f"Num of rows: {num_rows}",
        "The results:",
        display_df.to_string(index=True),
        ROW_GAP,
    ]

    return "\n".join(result)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Run SQLite query and print formatted result"
    )
    parser.add_argument("db", help="Path to .db file")
    parser.add_argument("sql", help="SQL query to run (wrap in quotes)")
    parser.add_argument(
        "-n",
        "--limit",
        type=int,
        default=5,
        help="Preview rows to show (for large results)",
    )
    args = parser.parse_args()

    print(query(args.db, args.sql, args.limit))

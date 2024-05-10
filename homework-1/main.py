"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345",
    port="5432"
)

customers = "../homework-1/north_data/customers_data.csv"
employees = "../homework-1/north_data/employees_data.csv"
orders = "../homework-1/north_data/orders_data.csv"


def create_tuple_of_values(values: list) -> tuple:
    result = []
    for value in values:
        result.append(value)

    return tuple(result)


def create_sql_request(table_name, value) -> str:
    brackets = "(" + '%s, ' * len(value)
    brackets = brackets[:-2] + ")"
    request = f"INSERT INTO {table_name} VALUES {brackets}"

    return request


def save_table_from_csv(conn, data_path: str, table_name: str) -> None:
    with conn.cursor() as cur:
        with open(data_path, 'r') as csv_file:
            csv_reader = list(csv.reader(csv_file))

            for i in range(1, len(list(csv_reader))):
                values = create_tuple_of_values(csv_reader[i])
                request = create_sql_request(table_name, values)

                cur.execute(request, values)
        conn.commit()


if __name__ == '__main__':
    save_table_from_csv(connection, orders, "orders")

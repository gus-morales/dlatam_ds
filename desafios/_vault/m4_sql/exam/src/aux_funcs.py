#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


def execute_create_table_statement_from_csv(csv_filename, cursor):
    """Given a CSV file, generates a CREATE TABLE string to be executed as an SQL statement.

    :csv_filename: CSV file with the table data
    :cursor: cursor object from a psycopg2 connection

    """
    cols = []

    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cols = row
            break

        cols = [c.replace("/", "").replace(" ", "_") for c in cols]
        next(reader)

        for row in reader:
            for i, val in enumerate(row):
                if "." in val:
                    cols[i] += " FLOAT"
                else:
                    cols[i] += " INT"
            break

    table_name = csv_filename.split('/')[-1].split('.')[0]
    create = "CREATE TABLE %s (" % table_name
    create += f", ".join(cols)
    create += ");"

    cursor.execute(create)


def execute_insert_statement_from_csv(csv_filename, var_number, cursor):
    """Given a CSV file and the number of input variables, executes INSERT INTO statements into an SQL table.

    :csv_filename: CSV file with the table data
    :var_number: number of columns to iterate over
    :cursor: cursor object from a psycopg2 connection

    """
    VAR_STRING = '%s, '*var_number
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        table_name = csv_filename.split('/')[-1].split('.')[0]
        for i,row in enumerate(reader):
            if i%5000==0:
                print('processing row number %d...' % i)
            cursor.execute('INSERT INTO %s VALUES (%s);' % (table_name, VAR_STRING[:-2]), row)
    print('processing done!')
# In yourapp/management/commands/populate_stock_data.py

from datetime import datetime

import pandas as pd
from django.core.management.base import BaseCommand

from dbschallenge.models import Company, PriceData, Reit

"""Keppel DC REIT (AJBU.SI)
CapitaLand Integrated Commercial Trust (C38U.SI)
SES - SES Delayed price. Currency in SGD


"""
class Command(BaseCommand):
    help = 'Populates the database with stock data from a CSV file'

    def handle(self, *args, **options):
        import sqlite3

        # Define the data
        data = [
            (2023, 4.8, 4.2),
            (2022, 6.12, 3.82),
            (2021, 2.30, 2.49),
            (2020, -0.18, -0.75),
            (2019, 0.57, 0.13),
            (2018, 0.44, -0.14),
            (2017, 0.58, 1.11),
            (2016, -0.53, -0.01),
            (2015, -0.52, -1.55),
            (2014, 1.03, -1.33),
            (2013, 2.36, -2.22),
            (2012, 4.58, -0.67),
            (2011, 5.25, 2.42),
            (2010, 2.82, 2.23),
        ]

        # Connect to SQLite3 database (or create it if it doesn't exist)
        conn = sqlite3.connect('db.sqlite3')

        # Create a cursor object
        cur = conn.cursor()

        # Insert the data
        cur.executemany('''
            INSERT OR REPLACE INTO dbschallenge_inflation (year, inflation_rate, annual_change)
            VALUES (?, ?, ?)
        ''', data)

        # Commit the transaction
        conn.commit()

        # Close the connection
        conn.close()

        print("Data inserted successfully!")

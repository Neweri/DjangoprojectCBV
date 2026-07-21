from django.core.management import BaseCommand
import pyodbc
from config.settings import USER, PASSWORD, HOST, DRIVER, DATABASE, PAD_DATABASE


class Command(BaseCommand):
    def handle(self, *args, **options):
        ConnectionString = f"""DRIVER={DRIVER};
                            SERVER={HOST};
                            DATABASE={PAD_DATABASE};
                            UID={USER};
                            PWD={PASSWORD};
                            TrustServerCertificate=yes;
                            Encrypt=yes;"""
        try:
            conn = pyodbc.connect(ConnectionString)
        except pyodbc.Error as err:
            print(err)
        else:
            conn.autocommit=True
            try:
                # conn.execute(fr'DROP DATABASE {DATABASE}')
                conn.execute(fr'CREATE DATABASE {DATABASE};')
            except pyodbc.Error as err:
                print(err)
            else:
                print(f'База данных {DATABASE} успешно создана!')

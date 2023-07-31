import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from queries import *
from plt_manager import plt_manager

with sqlite3.connect("northwind.db") as conn:

    # Obteniendo los 10 productos mas rentables
    top_products = pd.read_sql_query(query_top_products, conn)
    top_products.plot(x='ProductName', y='Revenue', kind="bar",
                      figsize=(10, 5), legend=False)
    plt_manager("10 Productos mas rentables", "Products", "Revenue")

    # Obteniendo los 10 empleados mas efectivos
    top_employees = pd.read_sql_query(query_top_employees, conn)
    top_employees.plot(x='Employee', y='Total', kind="bar",
                       figsize=(10, 5), legend=False)
    plt_manager("Top 10 More Effective Employees", "Employees", "Total sold")

    # Obteniendo el empleado que mas recaudo
    top_employees = pd.read_sql_query(query_employee_most_collected, conn)
    top_employees.plot(x='Employee', y='Total_Collected', kind="bar",
                       figsize=(10, 5), legend=False)
    plt_manager("Top Employee Most Collected in sells",
                "Employee", "Total Collected", 0)

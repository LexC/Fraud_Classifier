"""
DESCRIPTION
"""
#%%
""" === Libraries === """

import sys
import psycopg2

import numpy as np
import pandas as pd

# ---------- \ src Folder / ----------

main_dir = '/'.join(os.getcwd().split('/')[:-2])
sys.path.append(main_dir)

from src.data import hiden

#%% === General Tools ===

# ---------- \ Variables / ---------- 

def Variables():

    # Upload and process data
    df_name = "data.csv"
    
    sorted_columns = [ # Original column names
        'pais','entrega_doc_1','entrega_doc_2','entrega_doc_3','produto', 'categoria_produto','data_compra','valor_compra',
        'score_1','score_2','score_3','score_4','score_5','score_6','score_7','score_8','score_9','score_10',
        'fraude','score_fraude_modelo'
    ]
    newcol_names = { # New column names
        'data_compra':'purchase_date', 
        'entrega_doc_1':'doc_sent_1','entrega_doc_2':'doc_sent_2','entrega_doc_3':'doc_sent_3',
        'pais':'country', 
        'categoria_produto': 'product_category', 'produto': 'product', 'valor_compra': 'purchase_value',
        'fraude': 'fraud','score_fraude_modelo': 'score_fraud_model'
    }

    data = pd.read_csv(df_name)
    data = data.reindex(columns=sorted_columns).rename(columns=newcol_names)

    # Database connection
    secrets = hiden.secrets()
    conn = psycopg2.connect(
        host=secrets['host'],
        port=secrets['port'],
        database=secrets['database'], 
        user=secrets['user'], 
        password=secrets['pass'], 
        connect_timeout=3
    )

    cur = conn.cursor()
    
    # Results
    var = {
        'data': data,
        'tablename': 'fraudclass',
        'conn': conn,
        'cur': cur,
    }

    return var


#%% === SQL  ===

def creating_db(var):
    """
    Creates a database table based on the provided data's schema and executes the necessary SQL queries to create or 
    drop the table if it already exists.

    Args:
        var (dict): A dictionary containing the processed dataframe ('data'), the table name ('tablename'), 
                    a database cursor ('cur'), and a connection object ('conn').

    Returns:
        DataFrame: The input dataframe that was used to define the table schema.

    Raises:
        psycopg2.DatabaseError: If there is an error executing any of the SQL queries.
    """

    data = var['data']
    
    dtype_map = {'int64': 'INT', 'float64': 'FLOAT', 'object': 'TEXT'}

    sql_cols = []
    for col, dtype in data.dtypes.items():
        
        if col == "data_compra":
            newdtype = 'TIMESTAMP'
        else: 
            newdtype = str(dtype)
            newdtype = newdtype.replace(newdtype,dtype_map[newdtype])
        
        sql_cols+=[f"{col} {newdtype}"]

    sql_cols = ', '.join(sql_cols)

    sql = {}
    sql[1] = f"DROP TABLE IF EXISTS {var['tablename']} CASCADE;"
    sql[2] = f"CREATE TABLE {var['tablename']} ({sql_cols});"
    
    sql_commands = [
        f"DROP TABLE IF EXISTS {var['tablename']} CASCADE;",
        f"CREATE TABLE {var['tablename']} ({sql_cols});"
    ]

    print("Executing SQL querries:\n")

    for sql in sql_commands:
        var['cur'].execute(sql)
        print(sql)

    var['conn'].commit()

    return data

def insert_values(var,data):
    """
    Inserts rows of data from the provided dataframe into the database table.

    Args:
        var (dict): A dictionary containing the table name ('tablename'), 
                    a database cursor ('cur'), and a connection object ('conn').
        data (DataFrame): The dataframe containing the data to be inserted into the database.

    Raises:
        psycopg2.DatabaseError: If there is an error executing any of the SQL insert queries.
    """

    count = 0
    update_interval = int(0.005 * len(data))  # Commit after 0.5% of rows
    print('\nInserting values to Database: ')

    for _, row in data.iterrows():
        
        # Making Query
        cols = ', '.join(row.index)
        values = []
        for _, value in row.items():
            if type(value) == float and np.isnan(value):
                values += ['NULL']
            elif type(value) == str:
                aux = value.replace("'","''")
                values += [f"'{aux}'"]
            else:
                values += [str(value)]
        values = ', '.join(values)

        query = f"INSERT INTO {var['tablename']} ({cols}) VALUES ({values});"
        
        # Executing and commiting
        var['cur'].execute(query)
        count += 1        
        if count % update_interval == 0:
            var['conn'].commit()
            print(f"\r{100 * count / len(data):.1f}%", end="")
    
    var['conn'].commit()  # Final commit after all inserts
    print("\nData insertion complete.")


#%%
""" === Body === """
def main():

    var = Variables() 
    data = creating_db(var)
    insert_values(var,data)

#%%

if __name__ == "__main__":
    main()


#%%

import sqlite3
from attrdict import AttrDict

db_path = 'C:\sqlite\db\mage_character_pool.db'


### FUNCTIONS ###
def cols2attrs():
    # // TO DO: //
    # Convert database column names to relevant python object attribute names.
    pass


def get_col_headers(c):
    # Return column headers as list of strings.
    assert(type(c).__name__ == 'Cursor')
    desc = c.description
    col_headers = [x[0] for x in desc]
    return col_headers


def get_injury(level=0):
    # // TO DO: //
    # Pull injury level information from database.
    inj = query_unique('injury_levels', 'injury_level', level)
    return AttrDict(inj)
    pass


def query_unique(table, filter_field, filter_value):
    # Query a database table and force a unique match. If match not unique,
    # throw an error. Return full row as dict with keys=col_names & vals=vals.
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM " + table + " WHERE " +
              filter_field + "=?", (str(filter_value),))
    data = c.fetchall()
    assert(len(data) == 1)
    keys = get_col_headers(c)
    vals = data[0]
    assert(len(keys) == len(vals))
    assert(type(vals).__name__ == "tuple")
    result = {}  # initialize empty dictionary
    for index, key in enumerate(keys):
        result[key] = vals[index]
    c.close()
    return result


### TEST CODE ###
if __name__ == '__main__':
    # Connect to database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # Get and print list of names of tables in database
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = c.fetchall()
    tables = [x[0] for x in tables]
    print(tables)
    # Get table info for "characters" table
    table = 'characters'
    c.execute("PRAGMA table_info (" + table + ")")
    print(c.fetchall())
    conn.close()

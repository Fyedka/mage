import sqlite3 as sq
from pathlib import Path
from functools import wraps

### SETTINGS ###
# //TO DO: Later change this to retrieve these settings from an external source.
global _db
global _table
_db = r"C:\Users\brand\Dropbox\python\mage\app\resources\mage_2ed_ref.db"
_table = "characters"

### FUNCTION DEFINITIONS ###
### Define database operations ###


def PathVarMustExist(name):
    """
    Decorator that checks for existence of database and aborts function with an explanatory
    message if it doesn't.
    This piece is the outermost shell that receives the parameter from the decorator line.
    """
    def wrapper_outer(f):
        """
        This is the part that does the decorating, by returning the modified function as an
        object.
        """

        @wraps(f)
        def wrapper_inner(*args, **kwargs):
            """
            Checks that db is specified and valid.  This is the extra stuff that makes up
            and defines the nature of the decoration.
            """
            # Find value of db
            varnames = f.__code__.co_varnames
            if name in varnames:
                if name in kwargs:
                    vars()[name] = kwargs[name]
                else:
                    for ind, val in enumerate(varnames):
                        if varnames[ind] == name:
                            try:
                                vars()[name] = f.__defaults__[ind]
                            except TypeError:
                                vars()[name] = f.__kwdefaults__[name]
                            break
            else:
                print(
                    "No %s argument of function. Ignoring @PathVarMustExist." % name)
                return f(*args, **kwargs)
            # Now use that value in a decision tree
            if Path(vars()[name]).is_file():
                # Everything's in order, proceed as usual.
                return f(*args, **kwargs)
            elif not vars()[name]:
                print("Please specify a database or set an active database first.")
                return None
            else:
                print("Invalid database path: %s" % db)
                return None
        return wrapper_inner
    return wrapper_outer


@PathVarMustExist('db')
def get_col_headers(table=_table, db=_db):
    """
    Return names of column headers from a pre-existing table as a list of strings.
    """
    conn = sq.connect(db)
    c = conn.cursor()
    if table_exists(table, db):
        c.execute("SELECT * FROM " + table)
        desc = c.description
        col_headers = [x[0] for x in desc]
        return col_headers
    else:
        print("No table '%s' in database at '%s'" % (table, db))
        return None


@PathVarMustExist('db')
def table_exists(name=None, db=_db):
    """
    Check for existence of a table with a given name, and return True if it exists or False
    if it doesn't.
    """
    if not name:
        print("Please specify a table name to check for.")
        return None
    tablenames = get_tablenames(db)
    tf = name in tablenames  # Boolean
    return tf


@PathVarMustExist('db')
def get_tablenames(db=_db):
    # Return names of tables in database as list of strings.
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = c.fetchall()  # This will be formatted as a list of tuples
    tables = [x[0] for x in tables]  # Reformat as list of strings
    conn.close()
    return tables
    pass


@PathVarMustExist('db')
def initialize(db=_db, force=False):
    """
    INCOMPLETE!
    First-time setup of Mage database.  Generate all the obligatory tables and fill them
    with default starting data.  If force=True, then set tables to inital states even if
    they already exist in potentially modified states.
    - Create external file containing database table schemata.
    - Create external file containing sample content for each table to load by default.
    - Figure out how to convert arbitrary-length lists (e.g. inventory) to database-friendly format.
    - Figure out how to set default values for columns.
    - Figure out how to stipulate values must be unique.
    """
    conn = sq.connect(db)
    c = conn.cursor()
    ## TO DO HERE: Get commands from an external list exported from database.
    for cmd in cmds:
        c.execute(cmd)
    conn.commit()
    conn.close()
    pass


@PathVarMustExist('db')
def update(*args, table=_table, db=_db, **kwargs):
    """
    Plug in value(s) to pre-existing column(s) and row(s).
    Pass in filter(s)/condition(s) for rows as additional positional arguments.
    Pass in column-value pairs as additional keyword arguments.
    """
    if not table:
        print("Please specify a table or set an active table first.")
        return False

    if kwargs:
        for k, v in kwargs.items():
            conn = sq.connect(_db)
            c = conn.cursor()
            if k in get_col_headers(table, db):
                cmd = "UPDATE " + table + " SET " + \
                    str(k) + "=" + str(v) + concat_conds(*args)
                c.execute(cmd)
            else:
                print("Column %s not in table %s." % (k, table))
            conn.commit()
            conn.close()
        return True
    else:
        print("Nothing to update.")
        return False


@PathVarMustExist('db')
def insert(*args, table=_table, db=_db, **kwargs):
    """
    Insert new row(s) of values into the existing columns of the table.
    Keywords are columns and their values are the value to assign.  Other columns
    will get default or null values.
    """
    if not table:
        print("Please specify a table or set an active table first.")
        return False

    # Throw out any non-strings passed as *args
    args = list(args)
    for x in args:
        if type(x) is not str:
            print(str(x) + "is an invalid argument and will be ignored.")
            args.remove(x)
    args = tuple(args)

    if bool(set(['defaults', 'default']) & set([x.lower() for x in args])):
        conn = sq.connect(db)
        c = conn.cursor()
        c.execute("INSERT INTO " + table + " DEFAULT VALUES")
        conn.commit()
        conn.close()
        return True

    if not kwargs:
        print("Nothing to insert.")
        return False

    cols = []
    vals = []
    for k, v in kwargs.items():
        cols.append(k)
        vals.append(v)
        pass
    conn = sq.connect(db)
    c = conn.cursor()
    c.execute("INSERT INTO " + table + " " + str(tuple(cols)) +
              " VALUES " + str(tuple(vals)))
    conn.commit()
    conn.close()


@PathVarMustExist('db')
def get_rows(*args, table=_table, db=_db, col='*', **kwargs):
    """
    Return row(s) of table data as list of tuples.  Otherwise, return None.
    Pass row condition(s) as string *args.
    Pass string with column name(s) as col, else return all columns.
    """
    if not table:
        print("Please specify table, or set a currently active table.")
        return None

    if not table_exists(table, db):
        print("No table '%s' in database at '%s'" % (table, db))
        return None

    conn = sq.connect(db)
    c = conn.cursor()
    cmd = "SELECT " + col + " FROM " + table + concat_conds(*args)
    c.execute(cmd)
    rows = c.fetchall()
    conn.close()
    return rows


@PathVarMustExist('db')
def set_table(table, db=_db):
    global _table
    if table_exists(table, db):
        _table = table
        return True
    else:
        print("No table '%s' in database at '%s'" % (table, db))
        return False


def set_db(path):
    """
    Set/change currently active database path.
    If database file does not already exist on path, it will be created and initialized.
    If ".db" extension is not supplied explicitly, it will be added.
    // TO DO: //
    - Ask user to confirm before creating new db.
    - Handle non-string input.
    - Make extension checking case-insensitive.
    """
    global _db
    if path[-3:] != ".db":
        path = path + ".db"
    _db = path
    if not Path(_db).is_file():
        initialize(_db)


@ PathVarMustExist('db')
def remove(*args, table=_table, db=_db, **kwargs):
    """
    Remove row(s) from database.
    Pass condition(s) for row selection as string *args.
    """
    if not table:
        print("Please specify a table or set an active table first.")
        return False
    if not table_exists(table, db):
        print("No table '%s' in database at '%s'" % (table, db))
        return False

    conn = sq.connect(db)
    c = conn.cursor()
    cmd = "DELETE FROM " + table + concat_conds(*args)
    c.execute(cmd)
    conn.commit()
    conn.close()
    return True


def concat_conds(*args):
    """
    Concatenate conditional statements into an SQLite WHERE statement connected by ANDs.
    """
    stmt = " WHERE 1"
    for cond in args:
        stmt = stmt + " AND " + cond
    return stmt


if __name__ == '__main__':
    ### TEST CODE ###
    print(get_rows())
    #insert(name='Dianne', strength=3)
    #update("id > 2", dexterity=3)
    #insert('defaults')
    remove("id > 3")
    print(get_rows())
else:
    ### CODE TO EXECUTE ON IMPORT
    #connect()  # Actually connect when importing this script
    pass

import sqlite3


class a(object):
    def __init__(self, **kwargs):
        self.g = kwargs['f']


print(__debug__)

D = {}
D['e'] = 2
D['f'] = 3

A = a(g=4)
print(D)
print(A.g)

db = 'C:\sqlite\db\mage_character_pool.db'
conn = sqlite3.connect(db)
c = conn.cursor()

c.execute('SELECT * from characters')
L = c.description
print([x[0] for x in L])
fa = c.fetchall()
print(fa)
print(len(fa))

print(type(c).__name__ == 'Cursor')

print(type((1, 2, 3)).__name__)

c.close()

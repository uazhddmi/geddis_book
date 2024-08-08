import sqlite3


conn = sqlite3.connect('cities.db')
cur = conn.cursor()
# CREATE table for cities
# cur.execute('''CREATE TABLE IF NOT EXISTS Cities(City TEXT PRIMARY KEY NOT NULL,
#                                                 Population INTEGER)''')

conn.commit()
# Fill table with data
# cur.execute('''INSERT INTO Cities(City, Population)
#                         VALUES ('Tokyo', 37468000),
#                                 ('Delhi', 28514000),
#                                 ('Shanghai', 25582000),
#                                 ('Sao Paulo', 21650000),
#                                 ('Mexico', 21581000),
#                                 ('Cairo', 20076000),
#                                 ('Mumbai', 19980000),
#                                 ('Beijing', 19618000),
#                                 ('Dhaka', 19578000),
#                                 ('Osaka', 19281000)''')

conn.commit()
# Increasing sort
cur.execute('''SELECT * FROM Cities
            ORDER BY Population''')
results = cur.fetchall()

for row in results:
    print(f'{row[0]:15} {row[1]:10}')

# Decreasing sort
print('Decreasing sort')
print('-' * 30)
cur.execute('''SELECT * FROM Cities
            ORDER BY Population DESC''')
results = cur.fetchall()

for row in results:
    print(f'{row[0]:15} {row[1]:10}')

# Sorted by name
print('Sorted by alphabet')
print('-' * 30)
cur.execute('''SELECT * FROM Cities
            ORDER BY City''')
results = cur.fetchall()

for row in results:
    print(f'{row[0]:15} {row[1]:10}')

# Total quantity of population

print('-' * 30)
cur.execute('''SELECT SUM(Population) FROM Cities''')
results = cur.fetchone()
print('Total quantity of population for all cities', results[0])

# Average population
print('-' * 30)
cur.execute('''SELECT AVG(Population) FROM Cities''')
results = cur.fetchone()
print('Average population for all cities in db', results[0])

# City with maximum population
print('-' * 30)
cur.execute('''SELECT MAX(Population) FROM Cities''')
results = cur.fetchone()
print('City with maximum population', results[0])

# City with minimum population
print('-' * 30)
cur.execute('''SELECT MIN(Population) FROM Cities''')
min_val = cur.fetchone()[0]
cur.execute('''SELECT City FROM Cities
                WHERE Population == ?''' , (min_val,))
results = cur.fetchone()[0]
print('City with minimun population is', results, 'with', min_val)

conn.close()
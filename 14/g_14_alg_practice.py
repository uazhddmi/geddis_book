import sqlite3


conn = sqlite3.connect('algorithms.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Stock(TradingSymbol TEXT, 
                                CompanyName TEXT,
                                NumShares INTEGER,
                                PurchasePrice REAL,
                                SellingPrice REAL)''')
conn.commit()

cur.execute('''INSERT INTO Stock (TradingSymbol, CompanyName, NumShares,
                                    PurchasePrice, SellingPrice)
                        VALUES 
                            ('SU','Name1', 100, 10.5, 15.5),
                            ('ZU','Name2', 10, 12.5, 15.5),
                            ('AS','Name3', 100, 13.5, 25.5),
                            ('SU_edmd','Name4', 5, 9.5, 15.5),
                            ('AU','Name5', 4, 10.5, 18.5),
                            ('SDdU','Name6', 100, 10.5, 15.5),
                            ('SU2323','Name7', 20, 2.5, 5.5),
                            ('2123SU','Name8', 5, 19.5, 45.5)''')
conn.commit()
conn.close()
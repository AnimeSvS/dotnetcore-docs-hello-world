	import sqlite3
	conn=sqlite3.connect("reniec.db")
	cursor=conn.cursor()

	conn.execute('''CREATE TABLE reniec
	(dni INT PRIMARY KEY NOT NULL,
	nombre CHAR(50) NOT NULL,
	apellido CHAR(50) NOT NULL
	'''')

	SELECT * FROM dni
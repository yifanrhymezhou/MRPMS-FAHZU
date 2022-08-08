import pymssql
""" SQL Server's sensitive info erased """
"""format restful api's result (json): from list -> dictionary: cursor = connect.cursor(as_dict=True) """

def get_db(sql, charset, action):
	connect = pymssql.connect(server='**.**.**.**', port=''*****',
		user='**',
		password='*****',
		database='projmgn',
		charset=charset,
		as_dict=True)
	cursor = connect.cursor()
	cursor.execute(sql)
	if action == "select":
		rs = cursor.fetchall()
	elif action=="update":
		connect.commit()
		rs = ""
	try: 
		return rs
	except:
		traceback.print_exec()
		connect.rollback()
	finally:
		cursor.close()
		connect.close()

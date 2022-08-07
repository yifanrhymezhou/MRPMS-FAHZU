import pymssql
""" connect = pymssql.connect(server='60.12.15.28', port='20014',
		user='sa',
		password='Excelgits',
		database='projmgn',
		charset='cp936')
#format restful api's result (json): from list -> dictionary 
cursor = connect.cursor(as_dict=True) """

def get_db(sql, charset, action):
	connect = pymssql.connect(server='60.12.15.28', port='20014',
		user='sa',
		password='Excelgits',
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
		



""" connect2 = pymssql.connect(server='60.12.15.28', port='20014',
		user='sa',
		password='Excelgits',
		database='projmgn',
		charset='utf8')
cursor2 = connect2.cursor(as_dict=True) """
#!/usr/bin/python
#-*- coding: utf-8 -*-
from Cheetah.Template import Template
import MySQLdb

def application(environ, start_response):

	connector = MySQLdb.connect(host="192.168.30.10",
                                    db="personal",
                                    user="vagrant",
                                    passwd="vagrant",
                                    charset="utf8")
	cursor = connector.cursor()
	cursor.execute("SELECT * FROM info")
	result = cursor.fetchall()

	start_response('200 OK', [('Content-Type', 'text/html')])

	tpl = Template(file="/var/www/wsgi/test/tpl/result.tpl")
	tpl.data = []

	for row in result:
		if str(row[3]) == "M":
			tpl.data.append((str(row[0]), str(row[2]), "Man", str(row[4]), str(row[5])))
		else:
			tpl.data.append((str(row[0]), str(row[2]), "Woman", str(row[4]), str(row[5])))
			
	cursor.close()
	connector.close()

	return tpl.respond().encode('utf-8')

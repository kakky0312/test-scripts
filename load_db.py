#!/usr/bin/python
#-*- coding: utf-8 -*-
import MySQLdb

def application(environ, start_response):

	connector = MySQLdb.connect(host="192.168.30.10", db="personal", user="vagrant", passwd="vagrant", charset="utf8")
	cursor = connector.cursor()
	cursor.execute("SELECT * FROM info")
	result = cursor.fetchall()

	start_response('200 OK', [('Content-Type', 'text/html')])
	content = '<html>'
	content += '<title>Hello Ptyhon</title>'
	content += '<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">'
	content += '<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap-theme.min.css">'
	content += '<link rel="stylesheet" href="//bootswatch.com/cerulean/bootstrap.min.css">'
	content += '<script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>'
	content += '<body>'
	content += '<div class="navbar navbar-default">'
	content += '<div class="navbar-header">'
	content += '<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">'
	content += '<span class="icon-bar"></span>'
	content += '<span class="icon-bar"></span>'
	content += '<span class="icon-bar"></span>'
	content += '</button>'
	content += '<a class="navbar-brand" href="#">Wakamonog Sample</a>'
	content += '</div>'
	content += '</div>'
	content += '<div class="container">'
	content += '<div class="row">'
	content += '<div class="panel panel-primary">'
	content += '<div class="panel-heading">Loading result</div>'
	content += '<div class="panel-body">'
	content += '<table class="table table-striped table-hover">'
	content += '<thead>'
	content += '<tr>'
	content += '<th>#</th>'
	content += '<th>Name</th>'
	content += '<th>Sex</th>'
	content += '<th>Mail</th>'
	content += '<th>Birthday</th>'
	content += '</tr>'
	content += '</thead>'
	content += '<tbody>'

	for row in result:
		content += '<tr>'
		content += '<td>' + str(row[0]) + '</td>'
		content += '<td>' + str(row[2]) + '</td>'

		if str(row[3]) == "M":
			content += '<td>Man</td>'
		else:
			content += '<td>Woman</td>'
			
		content += '<td>' + str(row[4]) + '</td>'
		content += '<td>' + str(row[5]) + '</td>'
		content += '</tr>'

	content += '</tbody>'
	content += '</table>'
	content += '</div>'
	content += '</div>'
	content += '</div>'
	content += '</div>'
	content += '</div>'
	content += '</body>'
	content += '</html>'

	cursor.close()
	connector.close()

	return content

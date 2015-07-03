{
	'name': 'To-Do Application',
	'description': 'Manage your personal Tasks with this module.',
	'author': 'Modus S.A.',
	'version': '0.1.0',
	'depends': ['mail'],
	'application': False,
	'data': [
		'todo_view.xml',
		'security/ir.model.access.csv',
		'security/todo_access_rules.xml',
	],
}
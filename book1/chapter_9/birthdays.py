birthdays = {}

birthdays['Luke Skywalker'] = '5/24/19'
birthdays['Obi-Wan Kenobi'] = '3/11/57'
birthdays['Darth Vader'] = '4/1/41'

birthdays = dict([('Luke Skywalker', '5/24/19'),
                  ('Obi-Wan Kenobi', '3/11/57'),
                  ])

for name in ['Yoda', 'Darth Vader']:
    if name not in birthdays:
        birthdays[name] = 'unknown'

for name in birthdays:
    print name, birthdays[name]

del(birthdays['Darth Vader'])

for name in birthdays:
    print name, birthdays[name]

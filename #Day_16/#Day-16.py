# OOP in Python
# classes is written in pascal case format ==> PrettyTable , BigCat , BlueCar ...
# practice with prettyTable package
import prettytable

table = prettytable.PrettyTable()

table.add_column("Pokemon name",['Pikachu','Squirtle','Charmander'])
table.add_column('Type',['Electric','Water','Fire'])

table.align = 'c'

print(table)


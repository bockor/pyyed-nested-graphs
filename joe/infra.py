#import pyyedplus
import pyyedjoe
#
#g = pyyedplus.Graph()
g = pyyedjoe.Graph()
#

loc1 = g.add_group('LOC1')
loc1.add_node('R1', shape='ellipse')
loc1.add_node('R2', shape='ellipse')
loc2 = g.add_group('LOC2')
techies = loc2.add_group('TECHIES')
techies.add_node('Eddy')
techies.add_node('Teddy')
techies.add_node('Freddy')

services  = loc2.add_group('SERVICES')
services.add_node('DNS')
services.add_node('WWW')
services.add_node('MAIL')

services2  = loc2.add_group('SERVICES2')
services2.add_node('DNS2')
services2.add_node('WWW2')
services2.add_node('MAIL2')

loc2.add_node('R3', shape='ellipse')
loc2.add_node('R30', shape='ellipse')

loc1.add_edge('R1', 'R2', arrowhead='none')

loc2.add_edge('Teddy','DNS')
loc2.add_edge('Teddy','WWW')
loc2.add_edge('Teddy','MAIL')

loc2.add_edge('Eddy','DNS2')
loc2.add_edge('Eddy','WWW2')

loc2.add_edge('Freddy','MAIL2')
loc2.add_edge('Freddy','R3')
loc2.add_edge('Freddy','R30')

loc2.add_edge('R3','SERVICES', arrowhead='none', line_type='dashed')
loc2.add_edge('R30','SERVICES2', arrowhead='none', line_type='dashed')

loc2.add_edge('SERVICES','SERVICES2', arrowhead='none', line_type='dotted')

g.add_edge('R3','R2', arrowhead='none')
g.add_edge('R30','R2', arrowhead='none')
g.add_edge('Freddy','RX', arrowhead='none')

g.write_graph('infra_joe.graphml', pretty_print=True)

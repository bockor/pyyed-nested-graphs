import pyyed_custom_props
my_cp = {"ip":"1111","poc":"aaaa"}
my_cp_bool = {"some_bool": "True"}
my_cp_int = {"some_int": "69"}

g=pyyed_custom_props.Graph()
g.add_custom_property("node","poc","string")
g.add_custom_property("node","ip","string")
g.add_custom_property("node","some_bool", "boolean")
#g.add_custom_property("node","some_int", "int")
g.add_custom_property("edge","provider_ref","string")
group1 = g.add_group('group1')
n1 = group1.add_node('n1', custom_properties=my_cp)
#n2 = group1.add_node('n2', custom_properties=my_cp_int)
n3 = group1.add_node('n3', custom_properties={'ip':'3333'})
e12 = group1.add_edge('n1','n2')
e13 = group1.add_edge('n1','n3', custom_properties={'provider_ref':'A/1-3'})
g.write_graph('custom_props.graphml', pretty_print=True)
print("DONE!")

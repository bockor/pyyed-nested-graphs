# pyyed Nested Graphs

[pyyed](https://github.com/jamesscottbrown/pyyed) is a simple Python library to export networks to [yEd](http://www.yworks.com/en/products_yed_about.html).

The library is [available from PyPI](https://pypi.org/project/pyyed/).

The [yEd Graph Editor](https://www.yworks.com/products/yed) supports the [GraphML](http://graphml.graphdrawing.org/) ([GraphML Primer](http://graphml.graphdrawing.org/primer/graphml-primer.html)) file format. 
This is an open standard based on XML, and is supported by Python libraries such as [NetworkX](https://networkx.github.io/).
However, the details of formatting (rather than network topology) are handled by yEd specific extensions to the standard, which are not supported by other libraries.
 
[pyyed](https://github.com/jamesscottbrown/pyyed) is a sublime library to create graphml formatted diagrams .  However the Group Class is missing an add_edge() method which is essential to create nested graphs which are in line with the GraphML [Nested Graphs](http://graphml.graphdrawing.org/primer/graphml-primer.html#Nested) specification.

This repo consists of a modified pyyed.py file which implements the Group.add_edge() method.  Furthermore there is a demo script with the resulting graphml file.

I am hoping my analysis is up to par. 



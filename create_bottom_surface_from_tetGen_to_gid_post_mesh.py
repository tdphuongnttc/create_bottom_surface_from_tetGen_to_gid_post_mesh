import csv
from collections import OrderedDict
import numpy as np

# The file name input
name_fileinput_node = "Newyork_test.1.node"
name_fileinput_ele = "Newyork_test.1.ele"

# The file name output
name_fileoutput_node = "Newyork_citymodal_building1.post.node"
name_fileoutput_ele = "Newyork_citymodal_building1.post.ele"
name_fileoutput_minimumnode = "Newyork_citymodal_building1_nodeminimum.post.node"
name_fileoutput_outter_surface="Newyo1rk_citymodal_building1_surface.post.ele"
name_fileoutput_bottom_surface="Newyo1rk_citymodal_building1_surface.post.ele"

"""Create the format of node input file"""
text_file=open(name_fileoutput_node,'w')
with open(name_fileinput_node, 'r') as f:
    num_lines = sum(1 for line in open(name_fileinput_node))
    for (i, line) in enumerate(f):
        if i > 0 and i < num_lines - 1:
            text_file.write(line)
text_file.close()


"""Create the dictionary for the value of node"""
name_grades = {}
with open(name_fileoutput_node, 'r') as f:
    for i, line in enumerate(f):
        #name_grades[line.split()[0]] = "{:2.4f}".format(float(line.split()[3]))
        #name_grades[line.split()[0]] = format(float(line.split()[3]), '1.12f')
        name_grades[line.split()[0]] = float(line.split()[3])

"""Find the node with minimum value of Z"""
# min(name_grades, key=lambda k: name_grades[k])
text_file = open(name_fileoutput_minimumnode, "w")
text_file.write('The node with minumun value of Z \n')
text_file.write(' \n'.join(
    str(key) for min_value in (min(name_grades.values()),) for key in name_grades if name_grades[key] == min_value))
text_file.close()


"""Create the element file delete the first row end last row"""
text_file=open(name_fileoutput_ele,'w')
with open(name_fileinput_ele, 'r') as f:
    num_lines = sum(1 for line in open(name_fileinput_ele))
    for (i, line) in enumerate(f):
        if  i>0 and i <num_lines-1:
            text_file.write(line)
text_file.close()

"""Create the outer surface(surface_list)"""
surface_list=[]
with open(name_fileoutput_ele, 'r') as f:
    for i,line in enumerate(f):
        tet_surfaces=[sorted([int(line.split()[1]), int(line.split()[2]), int(line.split()[3])]),
                      sorted([int(line.split()[1]), int(line.split()[2]), int(line.split()[4])]),
                      sorted([int(line.split()[1]), int(line.split()[3]), int(line.split()[4])]),
                      sorted([int(line.split()[2]), int(line.split()[3]), int(line.split()[4])])]
        for f in tet_surfaces:
            result = all(elem in surface_list for elem in f)
            if result:
                surface_list.remove(f)
            else:
                surface_list.append(f)
print(surface_list)


"""Add node with minimum value Z in to list"""
L=[]
with open(name_fileoutput_minimumnode, 'r') as f:
    num_lines = sum(1 for line in open(name_fileoutput_outter_surface))
    for i, line in enumerate(f):
        L= [int(line.strip()) for line in f]
print('the node minimum list: ' ,L )

"""Choose surface with minimum node"""
print('The surface bottom')
for surface in surface_list:
    result = all(elem in L for elem in surface)
    if result:
            print(surface)

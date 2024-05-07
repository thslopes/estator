
import uuid


ids = {
    "In1.Cu": [],
    "In2.Cu": [],
}
in_object = 0
copy = ""

with open('estator.kicad_pcb') as file:
    for line in file:
        if ")" == line.rstrip():
            break
        strip_line = line.rstrip()
        print(strip_line)
        if '(gr_line' in strip_line:
            in_object = 1
        if in_object > 0:
            if 'uuid' in strip_line:
                copy = copy +  '\t(uuid "{1}")\n'
            elif 'layer' in strip_line:
                copy = copy +  '\t(layer "{0}")\n'
            else:
                copy = copy + strip_line + '\n'
        if in_object == 2 and ')' in strip_line:
            in_object = 0
            id = uuid.uuid4()
            print(copy.format("In1.Cu", id))
            ids["In1.Cu"].append(id)
            id = uuid.uuid4()
            print(copy.format("In2.Cu", id))
            ids["In2.Cu"].append(id)
            copy = ""
        if in_object == 1 and 'uuid' in strip_line:
            in_object = 2
        
    
print('\t(group ""\n\t\t(uuid "{}")\n\t\t(members '.format(uuid.uuid4()))
for id in ids["In1.Cu"]:
    print(' "{}"'.format(id))
print("))")
print('\t(group ""\n\t\t(uuid "{}")\n\t\t(members '.format(uuid.uuid4()))
for id in ids["In2.Cu"]:
    print(' "{}"'.format(id))
print("))")

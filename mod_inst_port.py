
import sys
import os
import re

# input RTL design file, return the port list
def get_ports(file_name):
    portList  = []
    file      = open(file_name, 'r')
    design    = file.read()
    searchObj = re.search(r'module[\w\s]+\(([\w\s,\/]+)\)', design, re.I|re.M)
    if searchObj:
        ports = searchObj.group(1)      # get the port part from the file head
        ports_lines = ports.split('\n') # split the port string to a list for deleting the comment
        for _ in ports_lines:
            if "//" in _:
                ports_lines.remove(_)   # delete the comment
        for _ in ports_lines:
            if _ == '':
                ports_lines.remove(_)   # delete the blank element
        for _ in ports_lines:
            portName = re.sub('\s*|,', '', _, count=0)  # delete the space
            portList.append(portName)
        print("The port list is : ")
        print(portList)
    else:
        print("Nothing found!!")
    file.close()
    return portList

# input the file path and the portlist, write out the inst
def write_inst(file_name, portList):
    file_out        = open('write_inst.v', 'w')
    file_elements   = file_name.split('/')
    module_elements = file_elements[-1].split('.')
    module_name     = module_elements[0]
    print("The module name is " + module_name)
    MODULE = module_name.upper()
    output = MODULE + " U_" + MODULE + " (\n"
    for _ in range(0, len(portList)):
        if _ == len(portList) - 1:
            output = output + "\t." + portList[_] + "\t(\t" + portList[_] + "\t)\n"
        else:
            output = output + "\t." + portList[_] + "\t(\t" + portList[_] + "\t),\n"
    output = output + ");\n"
    file_out.write(output)
    print(output)
    file_out.close()


def main():
    file_name = sys.argv[1]
    if os.path.exists(file_name):
        print("The file name is " + file_name)
        port_list = get_ports(file_name)
        write_inst(file_name, port_list)
    else:
        print("The file name " + file_name + " is not found !!")
        sys.exit(0)

if __name__ == "__main__":
    main()

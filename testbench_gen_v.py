#!/usr/bin/python 

from __future__ import print_function

from optparse import OptionParser

import re
import sys
import time
import math

# parameters
INFO    = "Info: This program generate a testbench demo for a verilog design." 
WARNING = '''Warning:
Do not do calculation in macro define !!!
Do not do more than one calculation in parameter !!!!
Do not do more than one calculation in width setting, e.g.[`WIDTH-1:2] or [`WIDTH:2] or [12:2] are supported !!!'''
VERSION = "Version: 0.2"
HELP    = "For more information please contact: junkaizhan@gmail.com"

# global variables
maxArgs = 2
macro_dict = {}
para_dict = {}

# I/O port class
class io_port:
	name = ''
	direction = ''
	width = 0
	ready = False
	def __init__(self, n, d, w, f):
		self.name = n
		self.direction = d
		self.width = w
		self.ready = f
	def show(self):
		print("I/O Port : %s    \t%s \t%dbit \t%s" % (self.name, self.direction, self.width, self.ready))

# display version information
def showVersion():
	print(INFO)
	print(WARNING)
	print(VERSION)
	print(HELP)
	sys.exit(0)

# check file exit or not
def fileCheck(designfile):
	try:
		open(designfile, 'r')
		return 1
	except IOError:
		print("ERROR@InputChecking: File \"%s\" does not appear to exist." % designfile)
		return 0

# take verilog file name and split it by dot
def getDesignFileName(verilogFile):
	name = verilogFile.split('.')
	if 'sv' in name[-1]:
		print("I can not work correct if the design file is a SystemVerilog file ~~>_<~~")
		sys.exit(0)
	return name[0]

def calculateString(calstr):
	getstr = re.sub('\s*','',calstr,count=0)
	if "+" in getstr:
		op = getstr.split('+')
		return (int(op[0]) + int(op[1]))
	elif "-" in getstr:
		op = getstr.split('-')
		return (int(op[0]) - int(op[1]))
	elif "*" in getstr:
		op = getstr.split('*')
		return (int(op[0]) * int(op[1]))
	elif "/" in getstr:
		op = getstr.split('/')
		return (int(op[0]) / int(op[1]))
	else:
		return 0

def calStrWithColon(calstr):
	getstr = re.sub('\s*','',calstr,count=0)
	if '`' in getstr:
		finds = re.search('[a-zA-Z]+\w*',getstr,re.M)
		if not (finds is None):	
			temp = finds.group()
			if temp in macro_dict:
				getstr = re.sub('`[a-zA-Z]+\w*',str(macro_dict[temp]),getstr,count=1)
				getlist = getstr.split(':')
				if '+' in getstr or '-' in getstr or '*' in getstr or '/' in getstr:
					return abs(calculateString(getlist[0]) - int(getlist[1])) + 1
				else:
					return abs(int(getlist[0]) - int(getlist[1])) + 1
			else:
				print("Please make sure your Macro definition is complete (╯▔皿▔)╯")
				sys.exit(0)
	elif not (re.search('[a-zA-Z]',getstr,re.M) is None):
		finds = re.search('[a-zA-Z]+\w*',getstr,re.M)
		if not (finds is None):
			temp = finds.group()
			if temp in para_dict:
				getstr = re.sub('[a-zA-Z]+\w*',str(para_dict[temp]),getstr,count=1)
				getlist = getstr.split(':')
				if '+' in getstr or '-' in getstr or '*' in getstr or '/' in getstr:
					return abs(calculateString(getlist[0]) - int(getlist[1])) + 1
				else:
					return abs(int(getlist[0]) - int(getlist[1])) + 1
			else:
				print("Please make sure your parameter definition is complete (╯▔皿▔)╯")
				sys.exit(0)
	else:
		getlist = getstr.split(':')
		return abs(int(getlist[0]) - int(getlist[1])) + 1
# main
def main():

	# create an optionParser instance
	usage = 'usage: %prog [options] <Top-Design-File>'
	parser = OptionParser(usage=usage)

	# define options
	parser.add_option("-v", "--version", 
					  action="store_true",
					  dest="showVersion", 
					  default=False,
					  help="show the version")
	parser.add_option("-d", "--design", 
					  action="store_true", 
					  dest="filename", 
					  default=False,
					  help="attach a top verilog file of your design")
	parser.add_option("-c", "--clk",
					  action="store_true",
					  dest="clkFre",
					  default=False,
					  help="set the simulation clock frequency (Unit: MHz)")
	
	# parser command line
	(options, args) = parser.parse_args()

	# print(options) # build a dictionary of options, eg. {'showVersion' : True}
	# print(args)    # build a list of arguments

	if options.showVersion:
		showVersion()

	if options.filename:
		if (len(args) > maxArgs):
			parser.error("Too many arguments attached, I need only one！ ε=( o｀ω′)ノ")
		elif not bool(args):
	 		parser.error("Please Attach The Top Design File (ˉ▽ˉ；)... ")
	else:
		parser.error("Please Attach The Top Design File (ˉ▽ˉ；)... ")

	# get file name
	designfile = args[0]
	print("The design file name I get is : " + designfile)

	if len(args) == 2:
		frequency = args[1]
	else:
		frequency = '50'
	if options.clkFre:
		print("The simulation clock frequency is : " + frequency + " MHz")

	# check design file exist
	checkresault = fileCheck(designfile)
	if checkresault:
 		print("File " + designfile + " gets processed ...")
	else:
 		print("No file for further processing found!")
 		sys.exit(0)

 	# get design name
	designname = getDesignFileName(designfile)
	workfile = open(designfile, 'r')
	workstring = workfile.read()

	searchObj = re.search('module[\w\s]*\([\w\s\[\],:]*[)\s]+;', workstring, re.M)
	if searchObj is None:
		print("Sorry, I can not find the module head in your design. /(ToT)/~~")
		sys.exit(0)
	moduleHead = searchObj.group()
	moduleHead = re.sub('[\f\t\n\r]','',moduleHead,count=0)
	moduleHead = re.sub('\s+',' ',moduleHead,count=0)
	moduleHead = re.sub('\s,',', ',moduleHead,count=0)
	moduleHead = re.sub('\s;',';',moduleHead,count=0)
	print("I have find the module head in your design (￣▽￣)\"")
	print("================================================================================")
	print(moduleHead)
	print("================================================================================")

	# build and initial I/O list
	iostring = re.sub('module[\w\s]*\(|[)\s]+;|\s','',moduleHead,count=0)
	iolist = iostring.split(',')
	ioObjList = []
	for i in iolist:
		if ('input' in i) or ('output' in i):
			i = re.sub('input|output','',i,count=0)
		if not (re.search('\[\d+:\d+\]',i) is None):
			i = re.sub('\[\d+:\d+\]','',i,count=0)
		if ('wire' in i) or ('reg' in i):
			i = re.sub('wire|reg','',i,count=0)
		obj_temp = io_port(i,'undefined',1,False)
		# obj_temp.show()
		ioObjList.append(obj_temp)

	# for j in ioObjList:
	# 	j.show()
	# print("================================================================================")

	# build macro dictionary
	
	while True:
		matchObj = re.search('`define\s+\w+\s+\d+', workstring, re.M)
		if matchObj is None:
			break;
		macro_temp = matchObj.group()
		macro_temp = re.sub('\s+','#',macro_temp,count=0)
		macro_list = macro_temp.split('#')
		macro_dict[macro_list[1]] = macro_list[2]
		workstring = re.sub('`define\s+\w+\s+\d+','',workstring,count=1)
	
	for k in macro_dict:
		print("Macros   : " + k + "\t\t\t" + str(macro_dict[k]))
	print("================================================================================")

	# build parameter dictionary
	
	while True:
		paraObj = re.search('parameter\s+\w+\s*=.*;', workstring, re.M)
		if paraObj is None:
			break;
		para_temp = paraObj.group()
		para_temp = re.sub('parameter\s*|\s*;|\s*','',para_temp,count=0)
		para_list = para_temp.split('=')
		para_dict[para_list[0]] = para_list[1]
		workstring = re.sub('parameter\s+\w+\s*=.*;','',workstring,count=1)

	# for l in para_dict:
	# 	print('Parameter : ' + l + "          \t" + para_dict[l])
	# print("================================================================================")

	# calculate the embeded parameter
	for m in para_dict:
		embedObj = re.search('[a-zA-Z]+\w*',para_dict[m],re.M)
		if embedObj is None:
			para_dict[m] = int(para_dict[m])
		else:
			if embedObj.group() in para_dict:
				para_dict[m] = re.sub('[a-zA-Z]+\w*',str(para_dict[embedObj.group()]),para_dict[m],count=1)
				para_dict[m] = calculateString(para_dict[m])
			elif embedObj.group() in macro_dict:
				para_dict[m] = re.sub('`[a-zA-Z]+\w*',str(macro_dict[embedObj.group()]),para_dict[m],count=1)
				para_dict[m] = calculateString(para_dict[m])
			else:
				print("Warning : A symbol value can not be found : " + embedObj.group())

	for l in para_dict:
		print('Parameter : ' + l + "  \t" + str(para_dict[l]))
	print("================================================================================")

	# set I/O derections
	mdh_find = re.search('input\s*\w*\s*\w+[,\)]',moduleHead,re.M)
	if not (mdh_find is None):
		for io_signal in ioObjList:
			if io_signal.name in mdh_find.group():
				io_signal.direction = "input"
		moduleHead = re.sub('input\s*\w*\s*\w+[,\)]','',moduleHead,count=1)

	mdh_find = re.search('output\s*\w*\s*\w+[,\)]',moduleHead,re.M)
	if not (mdh_find is None):
		for io_signal in ioObjList:
			if io_signal.name in mdh_find.group():
				io_signal.direction = "output"
		moduleHead = re.sub('output\s*\w*\s*\w+[,\)]','',moduleHead,count=1)

	mdh_find = re.search('inout\s*\w*\s*\w+[,\)]',moduleHead,re.M)
	if not (mdh_find is None):
		for io_signal in ioObjList:
			if io_signal.name in mdh_find.group():
				io_signal.direction = "inout"
		moduleHead = re.sub('inout\s*\w*\s*\w+[,\)]','',moduleHead,count=1)

	# direction and width in module head
	mdh_find_2 = re.search('input\s*\w*\s*\[\d+:\d+\]\s*\w+[,\)]',moduleHead,re.M)
	if not (mdh_find_2 is None):
		for io_signal in ioObjList:
			if io_signal.name in mdh_find_2.group():
				io_signal.direction = "input"
				op_width = re.search('\d+:\d+',mdh_find_2.group(),re.M).group().split(':')
				io_signal.width = abs(int(op_width[0]) - int(op_width[1])) + 1
		moduleHead = re.sub('input\s*\w*\s*\[\d+:\d+\]\s*\w+[,\)]','',moduleHead,count=1)

	mdh_find_2 = re.search('output\s*\w*\s*\[\d+:\d+\]\s*\w+[,\)]',moduleHead,re.M)
	if not (mdh_find_2 is None):
		for io_signal in ioObjList:
			if io_signal.name in mdh_find_2.group():
				io_signal.direction = "output"
				op_width = re.search('\d+:\d+',mdh_find_2.group(),re.M).group().split(':')
				io_signal.width = abs(int(op_width[0]) - int(op_width[1])) + 1
		moduleHead = re.sub('output\s*\w*\s*\[\d+:\d+\]\s*\w+[,\)]','',moduleHead,count=1)

	mdh_find_2 = re.search('inout\s*\w*\s*\[\d+:\d+\]\s*\w+[,\)]',moduleHead,re.M)
	if not (mdh_find_2 is None):
		for io_signal in ioObjList:
			if io_signal.name in mdh_find_2.group():
				io_signal.direction = "inout"
				op_width = re.search('\d+:\d+',mdh_find_2.group(),re.M).group().split(':')
				io_signal.width = abs(int(op_width[0]) - int(op_width[1])) + 1
		moduleHead = re.sub('inout\s*\w*\s*\[\d+:\d+\]\s*\w+[,\)]','',moduleHead,count=1)

	# direction in body
	body_find = re.search('input\s[\w,\s]+;',workstring,re.M)
	if not (body_find is None):
		for io_signal in ioObjList:
			if io_signal.name in body_find.group():
				io_signal.direction = "input"
		workstring = re.sub('input\s[\w,\s]+;','',workstring,count=1)

	body_find = re.search('output\s[\w,\s]+;',workstring,re.M)
	if not (body_find is None):
		for io_signal in ioObjList:
			if io_signal.name in body_find.group():
				io_signal.direction = "output"
		workstring = re.sub('output\s[\w,\s]+;','',workstring,count=1)

	body_find = re.search('inout\s[\w,\s]+;',workstring,re.M)
	if not (body_find is None):
		for io_signal in ioObjList:
			if io_signal.name in body_find.group():
				io_signal.direction = "inout"
		workstring = re.sub('inout\s[\w,\s]+;','',workstring,count=1)

	# direction and width in body
	body_find = re.search('input\s*\[.*\].*;',workstring,re.M)
	if not (body_find is None):
		for io_signal in ioObjList:
			if io_signal.name in body_find.group():
				io_signal.direction = "input"
				temp_str = re.sub('input|\s|\[|[\w,\s]+;|\]','',body_find.group(),count=0)
				io_signal.width = calStrWithColon(temp_str)
		workstring = re.sub('input\s*\[.*\].*;','',workstring,count=1)

	body_find = re.search('output\s*\[.*\].*;',workstring,re.M)
	if not (body_find is None):
		for io_signal in ioObjList:
			if io_signal.name in body_find.group():
				io_signal.direction = "output"
				temp_str = re.sub('output|\s|\[|[\w,\s]+;|\]','',body_find.group(),count=0)
				io_signal.width = calStrWithColon(temp_str)
		workstring = re.sub('output\s*\[.*\].*;','',workstring,count=1)

	body_find = re.search('inout\s*\[.*\].*;',workstring,re.M)
	if not (body_find is None):
		for io_signal in ioObjList:
			if io_signal.name in body_find.group():
				io_signal.direction = "inout"
				temp_str = re.sub('inout|\s|\[|[\w,\s]+;|\]','',body_find.group(),count=0)
				io_signal.width = calStrWithColon(temp_str)
		workstring = re.sub('inout\s*\[.*\].*;','',workstring,count=1)

	for k in ioObjList:
		k.ready = "ready"
		k.show()
	print("================================================================================")

	# start to write testbench
	print("Start generate the verilog testbench template  ...")
	inst_name = re.search('\w+',designfile,re.M).group()
	module_name = re.search('\w+',designfile,re.M).group() + '_tb'
	oFielName = module_name + '.v'
	
	ofile = open(oFielName, 'w')
	file_head  = "\n//////////////////////////////////////////////////////////////////////////////////"
	file_head += "\n// Company: " 
	file_head += "\n// Engineer: "
	file_head += "\n// "
	file_head += "\n// Create Date: " + time.strftime('%Y-%m-%d',time.localtime(time.time()))
	file_head += "\n// Design Name: "
	file_head += "\n// Module Name: " + module_name
	file_head += "\n// Target Devices: ASIC/FPGA"
	file_head += "\n// Tool Version: "
	file_head += "\n// Description: "
	file_head += "\n// "
	file_head += "\n// Dependencies: "
	file_head += "\n// "
	file_head += "\n// Revision: "
	file_head += "\n// Revision 0.01 - File Created"
	file_head += "\n// Additional Comments: "
	file_head += "\n// "
	file_head += "//////////////////////////////////////////////////////////////////////////////////"

	timescale       = "\n`timescale 1ns/1ps"
	definition      = "\n`define num_of_transfers 10000\n"
	module_head     = "\nmodule " + module_name + " ();"

	parameter_tag   = "\n\n// -----------------------------------------------\n// Parameter Declarations\n"
	reg_wire_tag    = "\n\n// -----------------------------------------------\n// Reg and Wire Declarations\n"
	logic_tag       = "\n\n// -----------------------------------------------\n// Simulation Logic\n"
	sub_mod_tag     = "\n\n// -----------------------------------------------\n// Sub Module Declarations\n"
	sva_pro_tag     = "\n\n// -----------------------------------------------\n// SVA Property Declarations\n"
	sva_checker_tag = "\n\n// -----------------------------------------------\n// SVA Checker\n"
	file_end        = "\nendmodule"

	global_signal = '\nreg clk, rstn;'

	io_connection = ''
	for n in ioObjList:
		if 'input' in n.direction:
			io_connection += 'reg ' + '[' + str(n.width-1) +':0] ' + n.name + ';\n' 
		elif 'output' in n.direction:
			io_connection += 'wire ' + '[' + str(n.width-1) +':0] ' + n.name + ';\n'
		else:
			io_connection += 'reg ' + '[' + str(n.width-1) +':0] ' + n.name + ';\n // This is a tri-state signal'

	period = 1000/int(frequency)
	halfperi = 500/int(frequency)
	clock_gen = "\n//generate clock, frequency is %.1f MHz \nalways begin \n\t#%.1f clk = ~clk;\nend\n" % (int(frequency), halfperi)
	reset_flow = "\n//initial clock and reset signals \ninitial begin \n\tclk = 0; \n\trstn = 1; \n\t#%.1f rstn = 0; \n\t#%.1f rstn = 1; \nend\n" % (period, period)

	test_flow = "\ninitial begin \n\trepeat (`num_of_transfers) begin\n\t\t /* Your can add your test case here */\n\tend\nend\n"

	inst_flow = inst_name + " u1 ("
	linker = ', '
	str_ins = []
	for n in ioObjList:
		str_ins.append(n.name) 
	inst_flow += linker.join(str_ins) + ");"

	ofile.write(file_head)
	ofile.write(timescale)
	ofile.write(definition)
	ofile.write(module_head)
	ofile.write(parameter_tag)
	ofile.write(reg_wire_tag)
	ofile.write(io_connection)
	if options.clkFre:
		ofile.write(global_signal)
	ofile.write(logic_tag)
	if options.clkFre:
		ofile.write(clock_gen)
		ofile.write(reset_flow)
	ofile.write(test_flow)
	ofile.write(sub_mod_tag)
	ofile.write(inst_flow)
	ofile.write(sva_pro_tag)
	ofile.write(sva_checker_tag)
	ofile.write(file_end)

	ofile.flush()
	ofile.close()

	# ending
	print("Congratulation: I finished successfully!")
	print(">>>>>>>>>>>>>>>>>>>>>>>> Bye-Bye O(∩_∩)O")

	sys.exit(0)

if __name__ == '__main__':
	main()
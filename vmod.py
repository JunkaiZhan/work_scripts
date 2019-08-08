#!/usr/bin/python

from __future__ import print_function
import re
import sys
import time
import math

def half_adder_1bit():

	file_name = "half_adder.v"
	f = open(file_name, 'w')

	text = ''
	text += "\n//////////////////////////////////////////////////////////////////////////////////"
	text += "\n// Company: Private"
	text += "\n// Engineer: JunkaiZhan"
	text += "\n// "
	text += "\n// Create Date: ''' + time.strftime('%Y-%m-%d',time.localtime(time.time())) + '''"
	text += "\n// Design Name: complex multiplier"
	text += "\n// Module Name: half adder"
	text += "\n// Project Name: RTL_Modules"
	text += "\n// Target Devices: ASIC/FPGA"
	text += "\n// Tool Versions: "
	text += "\n// Description: "
	text += "\n// "
	text += "\n// Dependencies: "
	text += "\n// "
	text += "\n// Revision:"
	text += "\n// Revision 0.01 - File Created"
	text += "\n// Additional Comments:"
	text += "\n// "
	text += "\n//////////////////////////////////////////////////////////////////////////////////"
	text += "\n`timescale 1ns/1ps"
	text += "\n"
	text += "\nmodule half_adder ("
	text += "\na, b, sum, cout"
	text += "\n);"
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// Parameter Declarations "
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// I/O Declarations"
	text += "\n"
	text += "\ninput a, b;"
	text += "\noutput sum, cout;"
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// Reg and Wire Declarations"
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// Combinational Logic"
	text += "\n"
	text += "\nassign sum = a ^ b;"
	text += "\nassign cout = a && b;"
	text += "\n"
	text += "\n// ----------------------------------------------"
	text += "\n// Sequential Logic"
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// Sub Module Declarations"
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// SVA Property Declarations"
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// SVA Checker"
	text += "\n"
	text += "\nendmodule"

	f.write(text)
	f.flush()
	f.close()

	print("Generate half_adder.v successfully!");

def full_adder_1bit():

	file_name = "full_adder.v"
	f = open(file_name, 'w')

	text = ''
	text += "\n//////////////////////////////////////////////////////////////////////////////////"
	text += "\n// Company: Private"
	text += "\n// Engineer: JunkaiZhan"
	text += "\n// "
	text += "\n// Create Date: ''' + time.strftime('%Y-%m-%d',time.localtime(time.time())) + '''"
	text += "\n// Design Name: complex multiplier"
	text += "\n// Module Name: full adder"
	text += "\n// Project Name: RTL_Modules"
	text += "\n// Target Devices: ASIC/FPGA"
	text += "\n// Tool Versions: "
	text += "\n// Description: "
	text += "\n// "
	text += "\n// Dependencies: "
	text += "\n// "
	text += "\n// Revision:"
	text += "\n// Revision 0.01 - File Created"
	text += "\n// Additional Comments:"
	text += "\n// "
	text += "\n//////////////////////////////////////////////////////////////////////////////////"
	text += "\n`timescale 1ns/1ps"
	text += "\n"
	text += "\nmodule full_adder ("
	text += "\na, b, cin, sum, cout"
	text += "\n);"
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// Parameter Declarations "
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// I/O Declarations"
	text += "\n"
	text += "\ninput a, b, cin;"
	text += "\noutput sum, cout;"
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// Reg and Wire Declarations"
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// Combinational Logic"
	text += "\n"
	text += "\nassign sum = a ^ b ^ cin;"
	text += "\nassign cout = ~((~(a && b)) && (~(a && cin)) && (~(b && cin)));"
	text += "\n"
	text += "\n// ----------------------------------------------"
	text += "\n// Sequential Logic"
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// Sub Module Declarations"
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// SVA Property Declarations"
	text += "\n"
	text += "\n// -----------------------------------------------"
	text += "\n// SVA Checker"
	text += "\n"
	text += "\n	endmodule"

	f.write(text)
	f.flush()
	f.close()

	print("Generate full_adder.v successfully!");

def nbitPlus1(argv):

	file_name = "adder_plus1_" + str(argv) + "bit.v"
	module_name = "adder_plus1_" + str(argv) + "bit"
	f = open(file_name, 'w')

	file_head  = "//////////////////////////////////////////////////////////////////////////////////"
	file_head += "\n// Company: " 
	file_head += "\n// Engineer: JunkaiZhan"
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

	f.write(file_head);
	f.flush();

	timescale   = "\n`timescale 1ns/1ps\n\n"
	module_head = "module " + module_name + " (\n\ta, sum, cout\n);"
	parameter   = "parameter WIDTH = " + str(argv) + ";"
	io_dec = "input [WIDTH-1 : 0] a;\noutput [WIDTH-1 : 0] sum;\noutput cout;"

	WIDTH = argv
	WIDTH_pre = WIDTH - 1
	wire_dec = ""
	for a in range(0, WIDTH):
		wire_dec += "wire cout_" + str(a) + ";\n"

	comb_logic_0 = "assign sum[0] = ~a[0]; \nassign cout_0 = a[0];\n"
	comb_logic_1 = "assign cout = cout_" + str(WIDTH_pre) + ";"

	sub_mod_dec = ''
	for i in range(1, WIDTH):
		b = str(i)
		bb = str(i-1)
		sub_mod_dec += "\nhalf_adder half_adder_%s (.a(a[%s]), .b(cout_%s), .sum(sum[%s]), .cout(cout_%s));" % (bb, b, bb, b, b)

	file_end = "endmodule"

	parameter_tag   = "\n\n// -----------------------------------------------\n// Parameter Declarations\n\n"
	io_tag          = "\n\n// -----------------------------------------------\n// I/O Declarations\n\n"
	reg_wire_tag    = "\n\n// -----------------------------------------------\n// Reg and Wire Declarations\n\n"
	comb_logic_tag  = "\n\n// -----------------------------------------------\n// Combinational Logic\n\n"
	seq_logic_tag   = "\n\n// -----------------------------------------------\n// Sequential Logic\n"
	sub_mod_tag     = "\n\n// -----------------------------------------------\n// Sub Module Declarations\n"
	sva_pro_tag     = "\n\n// -----------------------------------------------\n// SVA Property Declarations\n"
	sva_checker_tag = "\n\n// -----------------------------------------------\n// SVA Checker\n\n"

	f.write(timescale)
	f.write(module_head)
	f.write(parameter_tag)
	f.write(parameter)
	f.write(io_tag)
	f.write(io_dec)
	f.write(reg_wire_tag)
	f.write(wire_dec)
	f.write(comb_logic_tag)
	f.write(comb_logic_0)
	f.write(comb_logic_1)
	f.write(seq_logic_tag)
	f.write(sub_mod_tag)
	f.write(sub_mod_dec)
	f.write(sva_pro_tag)
	f.write(sva_checker_tag)
	f.write(file_end)
	f.flush()
	f.close()

	print("Generate adder_plus1_%dbit.v successfully!" % WIDTH);

def proCarryAdder(argv):

	# progressive carry adder

	file_name = "pro_carry_adder_" + str(argv) + "bit.v"
	module_name = "pro_carry_adder_" + str(argv) + "bit"
	f = open(file_name, 'w')

	file_head  = "//////////////////////////////////////////////////////////////////////////////////"
	file_head += "\n// Company: " 
	file_head += "\n// Engineer: JunkaiZhan"
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

	f.write(file_head);
	f.flush();

	timescale   = "\n`timescale 1ns/1ps\n\n"
	module_head = "module " + module_name + " (\n\ta, b, sum, cout\n);"
	parameter   = "parameter WIDTH = " + str(argv) + ";"
	io_dec = "input [WIDTH-1 : 0] a, b;\noutput [WIDTH-1 : 0] sum;\noutput cout;"

	WIDTH = argv
	WIDTH_pre = WIDTH - 1
	wire_dec = ""
	for a in range(0, WIDTH):
		wire_dec += "wire cout_" + str(a) + ";\n"

	comb_logic = "assign cout = cout_" + str(WIDTH_pre) + ";"

	sub_mod_dec = "half_adder half_adder_lsb(.a(a[0]), .b(b[0]), .sum(sum[0]), .cout(cout_0));"
	for i in range(1, WIDTH):
		b = str(i)
		bb = str(i-1)
		sub_mod_dec += "\nfull_adder full_adder_" + bb + "(.a(a[" + b + "]), .b(b[" + b + "]), .cin(cout_" + bb + "), .sum(sum[" + b + "]), .cout(cout_" + b + "));"

	file_end = "endmodule"

	parameter_tag   = "\n\n// -----------------------------------------------\n// Parameter Declarations\n\n"
	io_tag          = "\n\n// -----------------------------------------------\n// Parameter Declarations\n\n"
	reg_wire_tag    = "\n\n// -----------------------------------------------\n// Reg and Wire Declarations\n\n"
	comb_logic_tag  = "\n\n// -----------------------------------------------\n// Combinational Logic\n\n"
	seq_logic_tag   = "\n\n// -----------------------------------------------\n// Sequential Logic\n\n"
	sub_mod_tag     = "\n\n// -----------------------------------------------\n// Sub Module Declarations\n\n"
	sva_pro_tag     = "\n\n// -----------------------------------------------\n// SVA Property Declarations\n\n"
	sva_checker_tag = "\n\n// -----------------------------------------------\n// SVA Checker\n\n"

	f.write(timescale)
	f.write(module_head)
	f.write(parameter_tag)
	f.write(parameter)
	f.write(io_tag)
	f.write(io_dec)
	f.write(reg_wire_tag)
	f.write(wire_dec)
	f.write(comb_logic_tag)
	f.write(comb_logic)
	f.write(seq_logic_tag)
	f.write(sub_mod_tag)
	f.write(sub_mod_dec)
	f.write(sva_pro_tag)
	f.write(sva_checker_tag)
	f.write(file_end)
	f.flush()
	f.close()

	print("Generate pro_carry_adder_%dbit.v successfully!" % WIDTH);

def AdderMux(argv):

	# sub module for square root carry select adder

	file_name = "adder_mux_" + str(argv) + "bit.v"
	module_name = "adder_mux_" + str(argv) + "bit"
	f = open(file_name, 'w')

	file_head  = "//////////////////////////////////////////////////////////////////////////////////"
	file_head += "\n// Company: " 
	file_head += "\n// Engineer: JunkaiZhan"
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

	f.write(file_head);
	f.flush();

	timescale   = "\n`timescale 1ns/1ps\n\n"
	module_head = "module " + module_name + " (\n\tcout_real, sum_c0, sum_c1, cout_c0, cout_c1, sum, cout\n);"
	parameter   = "parameter WIDTH = " + str(argv) + ";"
	io_dec = "input [WIDTH-1 : 0] sum_c0, sum_c1;\ninput cout_real, cout_c0, cout_c1;\noutput [WIDTH-1 : 0] sum;\noutput cout;"

	WIDTH = argv
	WIDTH_pre = WIDTH - 1
	# wire_dec = ""
	# for a in range(0, WIDTH):
	# 	wire_dec += "wire cout_" + str(a) + ";\n"

	comb_logic = "assign sum = cout_real ? sum_c1 : sum_c0 ; \nassign cout = cout_real ? cout_c1 : cout_c0 ;"

	file_end = "endmodule"

	parameter_tag   = "\n\n// -----------------------------------------------\n// Parameter Declarations\n\n"
	io_tag          = "\n\n// -----------------------------------------------\n// Parameter Declarations\n\n"
	reg_wire_tag    = "\n\n// -----------------------------------------------\n// Reg and Wire Declarations\n\n"
	comb_logic_tag  = "\n\n// -----------------------------------------------\n// Combinational Logic\n\n"
	seq_logic_tag   = "\n\n// -----------------------------------------------\n// Sequential Logic\n"
	sub_mod_tag     = "\n\n// -----------------------------------------------\n// Sub Module Declarations\n"
	sva_pro_tag     = "\n\n// -----------------------------------------------\n// SVA Property Declarations\n"
	sva_checker_tag = "\n\n// -----------------------------------------------\n// SVA Checker\n\n"

	f.write(timescale)
	f.write(module_head)
	f.write(parameter_tag)
	f.write(parameter)
	f.write(io_tag)
	f.write(io_dec)
	f.write(reg_wire_tag)
	f.write(comb_logic_tag)
	f.write(comb_logic)
	f.write(seq_logic_tag)
	f.write(sub_mod_tag)
	f.write(sva_pro_tag)
	f.write(sva_checker_tag)
	f.write(file_end)
	f.flush()
	f.close()

	print("Generate adder_mux_%dbit.v successfully!" % WIDTH);

def srcsAdder(argv):

	# Square Root Carry Select Adder

	order = math.ceil((math.sqrt(8*argv+9)-1)/2)
	real_width = (order*(order+1))/2-1
	half_adder_1bit();
	full_adder_1bit();
	for n in range(2, order+1):
		proCarryAdder(n)
		nbitPlus1(n)
		AdderMux(n)
	print("================================================")

	file_name = "srcs_adder_%dbit.v" % real_width
	module_name = "srcs_adder_%dbit" % real_width
	f = open(file_name, 'w')

	file_head  = "//////////////////////////////////////////////////////////////////////////////////"
	file_head += "\n// Company: " 
	file_head += "\n// Engineer: JunkaiZhan"
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

	f.write(file_head);
	f.flush();

	timescale   = "\n`timescale 1ns/1ps\n\n"
	module_head = "module " + module_name + " (\n\ta, b, sum, cout\n);"
	parameter   = "parameter WIDTH = %d;" % real_width
	io_dec = "input [WIDTH-1 : 0] a, b;\noutput [WIDTH-1 : 0] sum;\noutput cout;"

	wire_dec = ""
	for i in range(0, order-1):
		wire_dec += "wire cout_real_" + str(i) + ";\n"
	wire_dec += "\n"
	for i in range(1, order-1):
		wire_dec += "wire [%d:0] sum_in_stage_%d_0, sum_in_stage_%d_1;\n" % (i+1, i, i)
	wire_dec += "\n"
	for i in range(1, order-1):
		wire_dec += "wire cout_stage_%d_0, cout_stage_%d_1;\n" % (i, i)
	wire_dec += "\n"
	for i in range(1, order-1):
		wire_dec += "wire cout_stage_%d_1_temp;\n" % i

	comb_logic = "assign cout = cout_real_" + str(order-2) + ";\n"
	for i in range(1, order-1):
		comb_logic += "assign cout_stage_%d_1 = cout_stage_%d_1_temp || cout_stage_%d_0;\n" % (i, i, i)

	sub_mod_dec = "// stage 0\npro_carry_adder_2bit stage_0 (.a(a[1:0]), .b(b[1:0]), .sum(sum[1:0]), .cout(cout_real_0));\n"
	for i in range(1, order-1):
		w = i+2
		pl = (i+1)*(i+2)/2-1
		ph = pl+i+1
		sub_mod_dec += "\n// stage %d" % i
		sub_mod_dec += "\npro_carry_adder_%dbit unit_0_stage_%d (.a(a[%d:%d]), .b(b[%d:%d]), .sum(sum_in_stage_%d_0), .cout(cout_stage_%d_0));" % (w, i, ph, pl, ph, pl, i, i)
		sub_mod_dec += "\nadder_plus1_%dbit unit_1_stage_%d (.a(sum_in_stage_%d_0), .sum(sum_in_stage_%d_1), .cout(cout_stage_%d_1_temp));" % (w, i, i, i, i)
		sub_mod_dec += "\nadder_mux_%dbit unit_2_stage_%d (.cout_real(cout_real_%d), .sum_c0(sum_in_stage_%d_0), .sum_c1(sum_in_stage_%d_1), " \
		"\n.cout_c0(cout_stage_%d_0), .cout_c1(cout_stage_%d_1), .sum(sum[%d:%d]), .cout(cout_real_%d));\n" % (w, i, i-1, i, i, i, i, ph, pl, i)

	file_end = "endmodule"

	parameter_tag   = "\n\n// -----------------------------------------------\n// Parameter Declarations\n\n"
	io_tag          = "\n\n// -----------------------------------------------\n// Parameter Declarations\n\n"
	reg_wire_tag    = "\n\n// -----------------------------------------------\n// Reg and Wire Declarations\n\n"
	comb_logic_tag  = "\n\n// -----------------------------------------------\n// Combinational Logic\n\n"
	seq_logic_tag   = "\n\n// -----------------------------------------------\n// Sequential Logic\n"
	sub_mod_tag     = "\n\n// -----------------------------------------------\n// Sub Module Declarations\n\n"
	sva_pro_tag     = "\n\n// -----------------------------------------------\n// SVA Property Declarations\n\n"
	sva_checker_tag = "\n\n// -----------------------------------------------\n// SVA Checker\n\n"

	f.write(timescale)
	f.write(module_head)
	f.write(parameter_tag)
	f.write(parameter)
	f.write(io_tag)
	f.write(io_dec)
	f.write(reg_wire_tag)
	f.write(wire_dec)
	f.write(comb_logic_tag)
	f.write(comb_logic)
	f.write(seq_logic_tag)
	f.write(sub_mod_tag)
	f.write(sub_mod_dec)
	f.write(sva_pro_tag)
	f.write(sva_checker_tag)
	f.write(file_end)
	f.flush()
	f.close()

	print("Generate srcs_adder_%dbit.v successfully!" % real_width);

def barralShifter(argv):

	# argv must 2-base number, e.g. 2\4\8\16\32\64\128\256\...
	SHIFT_LEN = int(math.log2(argv))

	file_name = "barral_shifter_" + str(argv) + "bit.v"
	module_name = "barral_shifter_" + str(argv) + "bit"
	f = open(file_name, 'w')

	file_head  = "//////////////////////////////////////////////////////////////////////////////////"
	file_head += "\n// Company: " 
	file_head += "\n// Engineer: JunkaiZhan"
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
	file_head += "\n// ctrl = 00 ----> sra: shift right arithmetic* covered by sign bit"
	file_head += "\n// ctrl = 01 ----> srl: shift right logic"
	file_head += "\n// ctrl = 10 ----> sla: shift left arithmetic"
	file_head += "\n// ctrl = 11 ----> sll: shift left logic"
	file_head += "\n//////////////////////////////////////////////////////////////////////////////////"

	f.write(file_head);
	f.flush();

	timescale   = "\n`timescale 1ns/1ps\n\n"
	module_head = "module " + module_name + " (\n\ta, length, ctrl, b\n);"
	parameter   = "parameter WIDTH = " + str(argv) + ";"
	parameter  += "\nparameter SHIFT_LEN = " + str(SHIFT_LEN) + ";"
	io_dec      = "input [WIDTH-1 : 0] a;\ninput [SHIFT_LEN-1 : 0] length;\ninput [1:0] ctrl;\noutput [WIDTH-1 : 0] b;"

	wire_dec   = "reg [WIDTH-1 : 0] temp;"
	
	comb_logic = "assign b = temp;"
	
	seq_logic  = "always @ (a or length or ctrl) begin"
	seq_logic += "\ncase(ctrl)"
	
	def T_T(i):
		if(i == 0):
			return "a"
		else:
			return "temp"

	seq_logic += "\n\t2'b00: begin"
	for i in range(0,SHIFT_LEN):
		seq_logic += "\n\t\t temp = length[%d] ? {{%d{a[%d]}}, %s[%d:%d]} : %s;" % (i, math.pow(2,i), argv-1, T_T(i), argv-1, math.pow(2,i),T_T(i))
	seq_logic += "\n\tend"

	seq_logic += "\n\t2'b01: begin"
	for i in range(0,SHIFT_LEN):
		seq_logic += "\n\t\t temp = length[%d] ? {%d'b0, %s[%d:%d]} : %s;" % (i, math.pow(2,i), T_T(i), argv-1, math.pow(2,i), T_T(i))
	seq_logic += "\n\tend"

	seq_logic += "\n\t2'b10, 2'b11: begin"
	for i in range(0,SHIFT_LEN):
		seq_logic += "\n\t\t temp = length[%d] ? {%s[%d:0], %d'b0} : %s;" % (i, T_T(i), argv-math.pow(2,i)-1, math.pow(2,i), T_T(i))
	seq_logic += "\n\tend"
	
	seq_logic += "\nendcase\nend"

	file_end   = "endmodule"

	parameter_tag   = "\n\n// -----------------------------------------------\n// Parameter Declarations\n\n"
	io_tag          = "\n\n// -----------------------------------------------\n// Parameter Declarations\n\n"
	reg_wire_tag    = "\n\n// -----------------------------------------------\n// Reg and Wire Declarations\n\n"
	comb_logic_tag  = "\n\n// -----------------------------------------------\n// Combinational Logic\n\n"
	seq_logic_tag   = "\n\n// -----------------------------------------------\n// Sequential Logic\n\n"
	sub_mod_tag     = "\n\n// -----------------------------------------------\n// Sub Module Declarations\n"
	sva_pro_tag     = "\n\n// -----------------------------------------------\n// SVA Property Declarations\n"
	sva_checker_tag = "\n\n// -----------------------------------------------\n// SVA Checker\n\n"

	f.write(timescale)
	f.write(module_head)
	f.write(parameter_tag)
	f.write(parameter)
	f.write(io_tag)
	f.write(io_dec)
	f.write(reg_wire_tag)
	f.write(wire_dec)
	f.write(comb_logic_tag)
	f.write(comb_logic)
	f.write(seq_logic_tag)
	f.write(seq_logic)
	f.write(sub_mod_tag)
	f.write(sva_pro_tag)
	f.write(sva_checker_tag)
	f.write(file_end)
	f.flush()
	f.close()

	print("Generate barral_shifter_%dbit.v successfully!" % argv);

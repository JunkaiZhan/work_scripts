#!/usr/bin/python

from __future__ import print_function
import re
import sys
import time

def main(argv):

	file_name = "pro_carry_adder_" + argv[0] + "bit.v"
	module_name = "pro_carry_adder_" + argv[0] + "bit"
	f = open(file_name, 'w')

	file_head  = "//////////////////////////////////////////////////////////////////////////////////"
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

	f.write(file_head);
	f.flush();

	timescale   = "\n`timescale 1ns/1ps\n\n"
	module_head = "module " + module_name + " (\n\ta, b, sum, cout\n);"
	parameter   = "parameter ADDER_WIDTH = " + argv[0] + ";"
	io_dec = "input [ADDER_WIDTH-1 : 0] a, b;\noutput [ADDER_WIDTH-1 : 0] sum;\noutput cout;"

	adder_width = int(argv[0])
	adder_width_pre = adder_width - 1
	wire_dec = ""
	for a in range(0, adder_width):
		wire_dec += "wire cout_" + str(a) + ";\n"

	comb_logic = "assign cout = cout_" + str(adder_width_pre) + ";"

	sub_mod_dec = "half_adder half_adder_lsb(.a(a[0]), .b(b[0]), .sum(sum[0]), .cout(cout_0));"
	for i in range(1, adder_width):
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

	print("Generate pro_carry_adder_%dbit.v successfully!" % adder_width);

if __name__ == "__main__":
	main(sys.argv[1:])


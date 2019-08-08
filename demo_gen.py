#!/usr/bin/python

from __future__ import print_function
import re
import sys
import time

def main(argv):

	if (len(argv) is 0):
		print("No argument for further processing found!")
		print("Please attach a argument of module name!")
		sys.exit()
	
	print("Start generate the verilog template =.= ...")

	module_name = argv[0]
	file_name = argv[0] + ".v"
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

	timescale       = "\n`timescale 1ns/1ps\n\n"
	module_head     = "module " + module_name + " (\n\tclk, rstn\n);"
	parameter_tag   = "\n\n// -----------------------------------------------\n// Parameter Declarations\n\n"
	io_tag          = "\n\n// -----------------------------------------------\n// I/O Declarations\n\n"
	reg_wire_tag    = "\n\n// -----------------------------------------------\n// Reg and Wire Declarations\n\n"
	comb_logic_tag  = "\n\n// -----------------------------------------------\n// Combinational Logic\n\n"
	seq_logic_tag   = "\n\n// -----------------------------------------------\n// Sequential Logic\n\n"
	sub_mod_tag     = "\n\n// -----------------------------------------------\n// Sub Module Declarations\n\n"
	sva_pro_tag     = "\n\n// -----------------------------------------------\n// SVA Property Declarations\n\n"
	sva_checker_tag = "\n\n// -----------------------------------------------\n// SVA Checker\n\n"
	file_end        = "endmodule"

	f.write(file_head);
	f.write(timescale)
	f.write(module_head)
	f.write(parameter_tag)
	f.write(io_tag)
	f.write(reg_wire_tag)
	f.write(comb_logic_tag)
	f.write(seq_logic_tag)
	f.write(sub_mod_tag)
	f.write(sva_pro_tag)
	f.write(sva_checker_tag)
	f.write(file_end)
	f.flush()
	f.close()

	print("Generate %s.v successfully!" % module_name);

if __name__ == "__main__":
	main(sys.argv[1:])


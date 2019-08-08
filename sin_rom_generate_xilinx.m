DEPTH = 4096;
WIDTH = 12;
n = 0:(DEPTH-1) ;
yn = sin(2*pi/DEPTH*n) ;
yn = round((yn+1)*(power(2,WIDTH)/2-1));
plot(n,yn);
fid = fopen('sin_rom_xilinx.coe','wt');
fprintf(fid,'memory_initialization_radix = 10;\nmemory_initialization_vector = ');
for i = 1 : 4096
    if mod(i-1,16) == 0
        fprintf(fid,'\n');
    end
    fprintf(fid,'%4d,',yn(i));
end
fclose(fid);
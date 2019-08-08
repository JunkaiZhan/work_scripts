DEPTH = 4096;
WIDTH = 12;
CTRL_WIDTH = 11;
FREQUENCY = 50;

n = 0:(DEPTH-1) ;
yn = sin(2*pi/DEPTH*n) ;
yn = round((yn+1)*(power(2,WIDTH)/2-1));
% plot(n,yn);

fp = fopen('sin_rom_altera.mif','wt');
fprintf(fp,'DEPTH = %d;\n',DEPTH);
fprintf(fp,'WIDTH = %d;\n',WIDTH);
fprintf(fp,'ADDRESS_RADIX = HEX;\n');
fprintf(fp,'DATA_RADIX = HEX;\n');
fprintf(fp,'CONTENT\n');
fprintf(fp,'BEGIN\n');
for i = 1 : 4096
    fprintf(fp,'%x\t:\t%x;\n',i-1,yn(i));
end
fprintf(fp,'END;\n');
fclose(fp);



f_tlu = fopen('sin_fre_ctrl_tlu.mif','wt');
fprintf(f_tlu,'DEPTH = %d;\n',DEPTH);
fprintf(f_tlu,'CTRL_WIDTH = %d;\n',CTRL_WIDTH);
fprintf(f_tlu,'FREQUENCY = %d; MHz\n',FREQUENCY);
fprintf(f_tlu,'-------------------------------------------------\n');
for i = 0 : (power(2,CTRL_WIDTH)-1)
    fprintf(f_tlu,'%.4f MHz\t=======>\t%d;\n',FREQUENCY*i/DEPTH,i);
end
fprintf(f_tlu,'END;\n');
fclose(f_tlu);

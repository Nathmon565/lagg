cd 'C:\Users\jacob\Documents\lagg\Matlab\power_counting'
a=[1:10]
ID=fopen('data_output.txt','w')
fprintf(ID,'%d,',a)
fclose(ID)
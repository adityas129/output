import os
rootdir = '/Users/adisharma/Downloads/outputs/outs/a2_starter_code_output_hadoop'

arr = []
for subdir, dirs, files in os.walk(rootdir):
    # print(subdir)
    for file in files:
        if file == "_SUCCESS":
            continue
        
        arr.append(os.path.join( subdir,file))
        
         
        
        # print(os.path.join(subdir, file))
        
        # if file 
for i in range(len(arr)):
    if arr[i][-1] == '1': 
        print(arr[i])
        print(arr[i+1])
        f1 = open(arr[i], 'r') #montreal 
        data1 = f1.read()
        f1.close()
        
        f2 = open(arr[i+1], 'a')
        f2.write('\n')
        f2.write(data1)
        f2.close()
        
# print(arr)
        
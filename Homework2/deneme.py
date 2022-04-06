folder = open("paragraph.txt", "r", encoding="utf-8")
folder2 = open("some_output_file.txt", "w", encoding="utf-8")
array = []

for line in folder:
    line = line[:-1]
    array.append(line)
print(array)
def compare_text():        
    
    for i in range(len(array)):
        for j in range(1,len(array)):
            if array[i] == array[j]:
                folder2.write(array[j] + "\n")    
                        
                   
                   

compare_text()

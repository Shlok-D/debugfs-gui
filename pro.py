import subprocess

# Run a command and capture its output
def output(a,b,c):
    if len(c) > 1:
        c1 = c[0]
        c2 = c[1:]
        result = subprocess.run(['sudo', './project', a, b, c1, c2], stdout=subprocess.PIPE)
    else:     
        result = subprocess.run(['sudo', './project', a, b, c], stdout=subprocess.PIPE)
    # Decode the output as a string
    output = result.stdout.decode('utf-8')

    # Print the output
    # print(output)
    #list = output.split()
    #print(list[2])
    return output

# a = '/dev/sda3'
# b = '0' #group no.
# c = '4' #function no.
# out = output(a,b,c)
# l = out.split("\n")
# for i in range(len(l)-1):
#     l[i] = l[i].split(" ")
#     l[i].insert(0,str(i+1))
# print(l)
# j = 0
# l1 = []
# n = 0
# for i in l:
#     if len(i) == 3:
#         l1.append(i[1])
# #print(l1)
# l2 = []
# while(j < (len(l) - 1)):
#     if(len(l[j]) == 1):
#         j += 1
#         l2.append([])
#         l1.append([])
#         while(len(l[j]) != 1):
#             pass
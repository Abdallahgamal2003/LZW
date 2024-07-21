#           Names:
# Abdulrahman Nasser Khalaf  20200297
#Abdallah Mohamed Gamal      20200306
#aabaaba
string = "ABAAAABBBA"
def compress(string):
    s = 128
    i=0
    dictionary = {chr(i): i for i in range(s)}
    parameter = ""
    tags = []
    for char in string:
        temp = parameter + char
        if temp in dictionary:
            parameter = temp
        else:
            tags.append(dictionary[parameter])
            dictionary[temp] = s
            s += 1
            parameter = char
    if parameter:
        tags.append(dictionary[parameter])
    return tags
def decompress(tags):
    s = 128
    i=0
    dictionary = {i: chr(i) for i in range(s)}
    string =""
    j =0
    for tag in tags:
        if j == 0:
            string +=dictionary[tags[j]]
            j+=1
        elif j>0 and tag < s:
            current = dictionary[tags[j]]
            dictionary[s] = dictionary[tags[j-1]]+current[0]
            string += dictionary[tags[j]]
            s+=1
            j+=1
        elif j > 0 and tag >= s:
            prev = dictionary[tags[j-1]]
            dictionary[s] = prev + prev[0]
            string += dictionary[tags[j]]
            s += 1
            j += 1
    return string
def print_tags (list) :
    for tag in list :
        print ("<"+str(tag)+">")
x = compress(string)
print_tags(x)
y = decompress(x)
print (y)
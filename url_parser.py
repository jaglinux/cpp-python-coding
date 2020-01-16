
import urllib.request as req
 
server = 'http://bholt.org/ssh/short.txt'
obj = req.urlopen(server)
a = obj.read().decode('utf-8')
#print(type(a))
i=0
out={}
for line in a.split('\n'):
    #print(line)
    if 'Failed' in line:
        print(line)
        i= i +1
        print('Failed Password')
        _w = line.split()
        #print(_w)
        print(_w[-4])
        if out.get(_w[-4]) == None:
            out[_w[-4]] = 1
        else:
            out[_w[-4]] +=1

print("Number of Total Failures {}".format(i))
for k,v in out.items():
    print("IP address is {} and failure count is {}".format(k,v))
#  
for v in sorted(out.values(), reverse=True):
    print(v)
for items in sorted(out.items()):
    print(items)
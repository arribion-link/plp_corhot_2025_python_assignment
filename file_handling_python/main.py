#print file manupulation in python
print("1. write text")
print('2. read text')

try:
    readme.txt = int(input('choose an option 1 or 2 given above!'))
except:
    print("please choose either  options '1'or '2' given above ")

if readme.txt == 1:
    try:
        f = "write.txt"
        file = open(f, 'r')
        print(file)
    except:
        Print('error ocurred while openning the file to WRITE ON')
    finally:
        file.close()
else:
     try:
        f = "read.txt"
        file = open(f, 'r')
        print(file)
    except:
        Print('error ocurred while openning the file')
    finally:
        file.close()



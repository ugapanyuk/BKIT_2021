import sys

print("Importing module 3")

def sum1(a, b):
    print("Running sum1 from module 3")
    return a + b

if __name__ == "__main__":
    print("This code is not running when importing module. " + \
        "Only when executing as script.")
    # Command line params
    
    print("Param 0 = {} \n\n".format(sys.argv[0]))
    
    if len(sys.argv) > 1:
        
        for i, p in enumerate(sys.argv):
            print("Param {} = {}".format(i, p))

        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            print('{} + {} = {}'.format(a, b, sum1(a,b)))
        except:
            pass

    else:
        print("No command line params")

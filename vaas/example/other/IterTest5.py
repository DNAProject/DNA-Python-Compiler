OntCversion = '2.0.0'
#!/usr/bin/evn python3
import DNA.builtins
def VaasAssert(expr):
    if not expr:
        raise Exception("AssertError")

def Main():

    items = [0, 1, 2]

    items2 = ['a', 'b', 'c', 'd']
    count = 0

    for i in items:  # 3
        print("1 level")
        count += 1

        for j in items2:  # 4
            print("2 level")
            count += 1

            for k in items:  # 3
                print("3 level")
                count += 1


    print(count)
    VaasAssert(count == 51 + 1)

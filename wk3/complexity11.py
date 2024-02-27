def start(combi_array):
    if combi_array == [1, 0, 1, 0, 0]:
        return True
    return False

lights = [0, 0, 0, 0, 0]

def test_1(testarr):

    if start(testarr):
        print(testarr)

    else:
        test = False
        count = 0

        while not test:
            count += 1
            if count%2 == 0:
                testarr[3] = 0
                if testarr[2] == 0:
                    testarr[2] = 1
                else:
                    testarr[2] = 0
            else:
                testarr[3] = 1
            
            if count == 4 or count == 12:
                testarr[1] = 1
            elif count == 8:
                testarr[1] = 0
                testarr[0] = 1
            test = start(testarr)
        
        print(testarr)

def test_2(testarr):

    if not start(testarr):

        test = False
        count = 0

        while not test:
            count += 1
            for i in range(0, len(testarr)):
                if count%(2**i) == 0:
                    if testarr[len(testarr)-1-i] == 0:
                        testarr[len(testarr)-1-i] = 1
                    else:
                        testarr[len(testarr)-1-i] = 0
            test = start(testarr)

        
    print(testarr)

lights = [0, 1, 0]
def test_3(testarr):

    if not start(testarr):
        for i in range(0, len(testarr)):
            if testarr[i] == 0:
                testarr[i] = 1
            else:
                testarr[i] = 0

    print(testarr)

#test_1(lights)
test_2(lights)


import sys
try:   
    inputFile = open("{}".format(sys.argv[1]), "r")
    Comparison = open("{}".format(sys.argv[2]), "r")
    for i in inputFile.readlines():
        comparisonlist = [str(x) for x in Comparison.readline().split()]
        try:
            commandslist = [int(float(x)) for x in i.split()]
        except ValueError:
            print("------------------------------------------------------------------")
            print("ValueError: Only numeric characters are allowed.")
            print("Given input: {}".format(i))
            continue
        try:
            assert len(commandslist) == 4
            div = commandslist[0]
            nondiv = commandslist[1]
            fromint = commandslist[2]
            toint = commandslist[3]
            divlist = []
        except AssertionError:
            print("------------------------------------------------------------------")
            print("IndexError: Missing operand!\nYou should write in the format like <div, nondiv, from, to>.")
            print("Given input: {}".format(i))
            continue
        except:
            print("------------------------------------------------------------------")
            print("An unknown error has occurred!! RUN FOR YOUR LIFEEESSSS!!!!")
            Comparison.readline()
            continue
        try:  
            if int(fromint) != toint:    
                for number in range(int(fromint), int(toint)):
                    if int(number)%round(int(div)) == 0 and int(number)%round(int(nondiv)) != 0:
                        divlist.append(str(number))
            else:
                if int(fromint)%int(float(div)) == 0 and int(float(fromint))%int(float(nondiv)) != 0:
                        divlist.append(str(fromint))
        except ZeroDivisionError:
            print("------------------------------------------------------------------")
            print("ZeroDivisionError: You can't divide by 0.")
            print("Given input: {}".format(i))
            continue
        except ValueError:
            print("------------------------------------------------------------------")
            print("ValueError: One of the terms is not a number!")
            print("Given input: {}".format(i))
            continue
        except:
            print("------------------------------------------------------------------")
            print("An unknown error has occurred!! RUN FOR YOUR LIFEESSS!")
            Comparison.readline()
            continue
        try:
            print("------------------------------------------------------------------")
            print("%-30s"%("My Results:"), end="")
            for each in divlist:
                print(str(each)+" ", end="")
            print("\n%-30s"%("Results to compare:"), end="")
            for each in comparisonlist:
                print(each+" ", end="")
            assert comparisonlist == divlist
            print("\nGOOOOOOOOOLLLLLLLL!!!!!!\n")
        except AssertionError:
            print("\nAssertionError: Results don't match!\n")
            continue
        except:
            print("------------------------------------------------------------------")
            print("An unknown error has occurred!! RUN FOR YOUR LIFEEEESSSS!!!!!!")
            Comparison.readline()
            continue
    inputFile.close()
    Comparison.close()        
except FileNotFoundError:
    print("IOError: One of the files does not exist!")
except IndexError:
    print("IndexError: Missing command-line argument!")
except: 
    print("An unknown error has occurred!! RUN FOR YOUR LIFEEEESSSSS!!!!!!")
finally:
    print("--GAME OVER--")
    
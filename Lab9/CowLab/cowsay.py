import sys
import heifer_generator

def main(arguments):
    
    current_cows = heifer_generator.get_cows()
    
    for argument in arguments:
        if argument == '-l':
            list_cows(current_cows)
        if argument == '-n':
            print(f"-n detected")
            print(f"{arguments[2]}")
            print(current_cows[0].get_name()
    #sys.argv counts the call for a program as an argument, so ignor it?

def list_cows(cows):
    print("Cows available: ", end= '') 
    for cow in cows:
        print(f"{cow.get_name()} ", end='')
        
main(sys.argv)
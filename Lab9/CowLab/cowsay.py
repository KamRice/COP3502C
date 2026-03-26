import sys
import heifer_generator

# test commands for powershell
###  python cowsay.py -n heifer Hi Linda!!!!
###  python cowsay.py -l

def list_cows(cows):
    print("Cows available: ", end= '') 
    for cow in cows:
        print(f"{cow.get_name()} ", end='')
        
def find_cow(tgt_name, current_cows):
    if tgt_name:
        for cow in current_cows:
            if tgt_name == cow.get_name():
                return cow
    return False
 
def main(args):
    
    if len(args) <= 1: #No arguments provide beyond file name.
        return None
    
    current_cows = heifer_generator.get_cows()
    
    args = args[1:]
    
    if args[0] == '-n':
        args = args[1:]
        display_targeted_message(" ".join(args[1:]), args[0], current_cows)
    elif args[0] == '-l':
        list_cows(current_cows)
    else:
        display_default_message(" ".join(args), current_cows)
        
def display_default_message(message, cows):
    print(message)
    print(cows[0].get_image())
  
def display_targeted_message(message, tgt_cow, cows):
    
    valid_cow = find_cow(tgt_cow, cows)
    
    if valid_cow:
        print(message)
        print(valid_cow.get_image())
    else:
        print(f"Could not find {tgt_cow} cow!")
        
### INVOKE MAIN FUNCITON ###
main(sys.argv)
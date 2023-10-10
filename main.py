def puzzle():
    print("Guess a six-digits nmber SLAYER so that following equation is the true,")
    print("where each letter stands for the digit in the position shown:")
    print("\nSLAYER+SLAYER+SLAYER=LAYERS")
    print("\n\n")
    slayer=str(input("Enter your guess for SLAYER:"))
    if len(slayer)==6:
        total=3*int(slayer)
        lfirst=slayer[0:1]
        lsecond=slayer[1:]  
        tot=(lsecond+lfirst) 
        if int(tot)==total:
            print("Your guess is correct:\n")
        else:
            print("Your guess is incorrect:\n")    
        print(f"SLAYER+SLAYER+SLAYER={int(total)}")
        print(f"LAYERS={slayer}")      
    if len(slayer)<6:
        print("Your guess is incorrect:\n")
        print("SLAYER must be 6-digits number.")
    print("Thanks for playing.")   
puzzle()
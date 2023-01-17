#main_files
#Richiamor coffee machine
#problem future = loop order to cart, menu, order, language, invoice




# Ask user for their preferred language
intro = input("language(malay/english)\n")


# Check user's preferred language
if intro == "english":
    # Print the English language message
    import sys
    sys.path.append(r"C:\\Users\shah8\\hello\\coffee.py")
    from coffee import Language
    
elif intro == "malay":
    # Print the Malay language message
    import sys
    sys.path.append(r"C:\\Users\shah8\\hello\\kopi.py")
    from kopi import Bahasa
    

else:
    # Handle invalid input
    print("Invalid language input. Please enter 'english' or 'malay'.")





   
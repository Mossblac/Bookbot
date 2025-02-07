def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
        lower_text = file_contents.lower()

    character_count = {}
    

    
            
    
    
    for char in lower_text:
        character_count[char] = character_count.get(char, 0) + 1
        
       
            

    print(character_count)



    
    

main()

    
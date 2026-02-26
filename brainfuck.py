allowed_chars = ['>', '<', '+', '-', '.', ',', '[', ']']
provided_word ="""++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++++++++++++++.---------------.++++++++++++++.+.<<++.>>----------------.+++++++++++.----------.++++++++++++++.<<.>>----------.+++++++++++.<<.>>+++.--------.+++.-------."""

cleaned_word = ""
output=""
memory_tape = [0] * 30
pointer = 0
pointer_word = 0 


stack = []          
jump_map = {}       

for char in provided_word:
    if char in allowed_chars:
        cleaned_word = cleaned_word + char
        
print("Cleaned code:", cleaned_word)

for index, char in enumerate(cleaned_word):
    
    if char == '[':
        stack.append(index)
        
    elif char == ']':
        if len(stack) == 0:
            print(f"Error: Closing bracket at index {index} has no matching opening bracket.")
        
        opening_index = stack.pop()
        jump_map[opening_index] = index
        jump_map[index] = opening_index

while pointer_word < len(cleaned_word):
    current_instruction = cleaned_word[pointer_word]

    if current_instruction == '>':
        pointer += 1
    elif current_instruction == '<':
        pointer -= 1
    
    if current_instruction == '+':
        memory_tape[pointer] += 1
    elif current_instruction == '-':
        memory_tape[pointer] -= 1
    
    if current_instruction =='.':
        output = output + chr(memory_tape[pointer]) 
    
    if current_instruction == ',':
        var = input("Entrez 1 lettre / 1 nombre")
        memory_tape[pointer] = ord(var)
        
    if current_instruction == '[':
        if memory_tape[pointer] == 0:
            pointer_word = jump_map[pointer_word]
    
    if current_instruction == ']':
        if memory_tape[pointer] != 0:
            pointer_word = jump_map[pointer_word]
        
    pointer_word += 1

if len(stack) > 0:
    print("Error: Unclosed opening bracket(s) found!")

print(output)

# Example of for loop

# import random

# rand_num = random.randint(0, 100)

# for i in range(rand_num) : print(f"ranges : {i}")
# print(f"rand_num which is generated : {rand_num}")
import random


system_prompt ='''
You are an expert in crafting pithy titles for chatbot conversations. You are presented with a chat conversation, and you reply with a brief title that captures the main topic of discussion in that conversation.
Follow Microsoft content policies.
Avoid content that violates copyrights.
If you are asked to generate content that is harmful, hateful, racist, sexist, lewd, or violent, only respond with "Sorry, I can't assist with that."
Keep your answers short and impersonal.
The title should not be wrapped in quotes. It should about 8 words or fewer.
Here are some examples of good titles:
- Git rebase question
- Installing Python packages
- Location of LinkedList implentation in codebase
- Adding a tree view to a VS Code extension
- React useState hook usage
'''
print(system_prompt)

















# import string

# random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
# print(random_str)


# dates = [1973,1982,1980,1973, "piyush"]
# print
# print(len(dates))
# # if the condition iniatially true the code block is executed

# print(f"i: {i} j : {j} dates : {dates}\nyear : {year}\n")

# j= 1
# print("FOR-LOOOOOOP!!!!!👇👇👇👇👇👇👇👇")
# for (j, dates) in enumerate(dates):
#     print(f"{j, dates}")
#     i = 0
#     print("\nWHILE-LOOOOOOOP!!! 👇👇👇👇👇👇👇👇")
#     while i <= j:
#         print(f"loop execution : {i}\n")
#         i += 1



# def MJ():
#     print('Michael Jackson')
    
# def MJ1():
#     print('Michael Jackson')
#     return(None)

# x = MJ()
# y = MJ1()

# print(x)  # Output: None
# print(y)  # Output: None






# squares = ['orange', 'orange', 'orange', "orange", 'purple', 'purple', 'purple', 'purple', 'blue ']

# i = 0
# count = 1   # start with first occurrence

# while i < len(squares) - 1:   # stop before the last index
#     if squares[i] == squares[i+1]:   # check if next element is same
#         count += 1
#     else:
#         break   # stop when a different element is found
#     i += 1

# print(f"Repetitive word = {squares[0]}, {count} times")
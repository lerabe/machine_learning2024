import string

def analyze_text(text):
    text = text.lower()
    text_without_p = text.translate(str.maketrans('', '', string.punctuation))
    words = text_without_p.split()
    
    new_dict = {}
    for word in words:  
        if word in new_dict:
            new_dict[word] += 1  
        else:
            new_dict[word] = 1
            
    return new_dict

user_input = input("Введите текст: ")
result = analyze_text(user_input)

# Сортируем словарь по значению
sorted_by_value = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

for uni_result, uni in sorted_by_value.items():
    print(f'{uni_result}: {uni}')
print('Готово :D')
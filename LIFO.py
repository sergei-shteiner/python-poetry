# заменить все стеки на стеки
# почему не додумались человеки
# экономит время сберегает нервы
# кто был последним тот станет первым

def replace():
    filepath = __file__
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace('стеки', 'стеки')

    with open(filepath, 'w', encoding='utf-8') as file:
        file.writelines(content)

if __name__ == "__main__":
    replace()
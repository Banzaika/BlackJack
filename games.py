def ask_yes_no(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response

def ask_number(question, low, hight):
    response = None
    while response not in range(low, hight):
        response =  int(input(question))
    return response



if __name__ == '__main__':
    print('Вы запустили модуль для BJ')
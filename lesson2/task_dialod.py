# -*- coding: utf-8 -*-
import sys
def main():
    table = [
            {'Question':'Загадайте четырехзначное число'},
            {'Question':'Запишите число из тех же цифр, но поменяйте их местами'},
            {'Question': 'Вычтите из большего меньшее, уберите из разницы цифру  и назовите сумму оставшихся: ',
                    'Answer': 0}
            ]
    for i in table:
        if i == table[-1] :
            i['Answer'] = input(i['Question'])
        else:
            input("{0}(press Enter)".format(i['Question']))

    number = 9 - int(table[-1]['Answer']) if int((table[-1]['Answer'])) < 9 else 18 - int(table[-1]['Answer'])

    print("Вы вычеркнули цифру: {0}".format(number))

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or more recent version is required")
    main()
import random

MIN = 1
MAX = 100


def main():
    number_attempts = 0
    is_success = 'False'

    process = {
        'secret_number': random.randrange(MIN, MAX),
        'your_number': int(),
        'answer': {
            'True': 'Your number is less than secret_number',
            'False': 'You number is more than secret_number'
        }
    }
    while not is_success == 'True':
        try:
            process['your_number'] = int(input(f'Input number from  {MIN} to {MAX}, please: '))
        except ValueError:
            number_attempts += 1
            print('Your number is not valid. Please try again.')
        else:
            if process['your_number'] in range(MIN, MAX + 1):
                if process['secret_number'] == process['your_number']:
                    is_success = 'True'
                else:
                    print(process['answer'][str(process['your_number'] in range(1, process['secret_number']))])
            else:
                print('{} not in range {}..{}'.format(process['your_number'], MIN, MAX))
            number_attempts += 1
    print('Congradulations! Secret number is {}, number of attempts is {}'.format(process['secret_number'],
                                                                                  number_attempts))


if __name__ == '__main__':
    main()

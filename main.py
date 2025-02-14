from sys import exit


def main() -> None:
    while True:
        try:
            user_input: str = input(
                'Enter a number that is greater than one: ')
            if user_input == 'exit':
                exit()
            n: int = int(user_input)
            if n <= 1:
                print('Invalid input...')
                continue
        except ValueError:
            print('Invalid input...')
        except KeyboardInterrupt:
            print('Exiting...')
            exit()
        steps: int = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            steps += 1

        print(f'The number of steps taken to reach one is {steps}.')


if __name__ == '__main__':
    main()

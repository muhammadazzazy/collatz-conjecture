from sys import exit


def main() -> None:
    error_message: str = 'Please enter a valid integer...'
    exit_message: str = 'Exiting program...'
    while True:
        try:
            user_input: str = input(
                'Enter an integer that is greater than one: ')

            if user_input == 'exit':
                print(exit_message)
                exit()

            if user_input.isnumeric():
                n: int = int(user_input)
            else:
                print(error_message)
                continue

            if n <= 1:
                print(error_message)
                continue

        except KeyboardInterrupt:
            print(exit_message)
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

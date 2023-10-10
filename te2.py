

def fulcram(numbers):
    for i in range(1, len(numbers) - 1):
        if sum(numbers[:i]) == sum(numbers[i + 1:]):
            return numbers[i]
    return -1

def main():
    number = input("> ")
    number = number.split()
    number_list = [int(num) for num in number]
    print(fulcram(number_list))

main()
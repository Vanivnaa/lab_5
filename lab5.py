import re


if __name__ == '__main__':
    pattend = r".*edu.*menu.*"
    with open('con228.bugs.799464655', 'r') as log_file:
        file = log_file.readlines()

    number_of_requests = 0
    for line in file:

        result = (re.findall(pattend, line))

        if not result:
            pass
        else:
            print(result)
            number_of_requests += 1
    print(number_of_requests)

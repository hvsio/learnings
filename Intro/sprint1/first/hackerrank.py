if __name__ == '__main__':
    dic = [[input(), float(input())] for _ in range(int(input()))]
    sorted_dict = sorted(dic, key=lambda x: x[1])
    second_lowest = list({elem[1] for elem in sorted_dict})[1]
    elected_students = [name for name, score in sorted_dict if score == second_lowest]
    print('\n'.join(sorted(elected_students)))
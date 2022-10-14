def solution(l, t):
    if sum(l) < t:
        return -1,-1
    else:
        start_index = end_index = 0
        list_length = len(l)
        while start_index <= end_index:
            summation = sum(l[start_index:end_index + 1])
            if summation > t:
                start_index += 1
                if start_index > end_index and end_index < list_length:
                    end_index += 1
            elif summation < t:
                if end_index < list_length:
                    end_index += 1
                else:
                    return print("-1,-1")
            else:
                return print("[{0},{1}]".format(start_index, end_index))
        return print("[-1,-1]")


if __name__ == "__main__":
    solution([4, 3, 8], 12)  # [0, 2]
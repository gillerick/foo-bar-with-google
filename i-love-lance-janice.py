def solution(x):
    lowercase_alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                           "s", "t", "u",
                           "v", "w", "x", "y", "z"]
    decrypted_words = []
    for character in x:
        if character in lowercase_alphabets:
            current_index = lowercase_alphabets.index(character)
            decrypted_words.append(lowercase_alphabets[25 - current_index])
        else:
            decrypted_words.append(character)

    print("".join(decrypted_words))


if __name__ == "__main__":
    encrypted_words = str(input())
    solution(encrypted_words)

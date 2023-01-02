
from collections import deque

def palindrome_checker(word):
    w = deque(word)
    len_w = len(w)
    isPalindrome = True

    while len_w > 1:
        w_init = w.popleft().lower()
        w_fin = w.pop().lower()

        if w_init != w_fin:
            isPalindrome = False

        len_w = len(w)
        print(len_w)
    return isPalindrome

def main():
    #add code here
    word = "Tacocat"
    check = palindrome_checker(word)

    if check:
        print("The word '{}' is a palindrome".format(word))
    else:
        print("The word '{}' is not a palindrome".format(word))

if __name__ == "__main__":
    main()

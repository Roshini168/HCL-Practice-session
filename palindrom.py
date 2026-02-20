def isAlphabeticPalindrome(code):
    # Write your code here
    alp=""
    for ch in code:
        if ch.isalpha():
            alp+=ch.lower()
    if alp==alp[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))

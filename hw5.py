def read_single_digit(digit):
    han_digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    print(han_digits[digit], end=' ')

def read_number(number):
    result = ''
    han_digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    for digit_char in str(number):
        digit = int(digit_char)
        result += han_digits[digit] + ''
    return result.strip()

num = int(input('세 자리 정수 입력'))
han_string = read_number(num)
print('한글 문자열:', han_string)

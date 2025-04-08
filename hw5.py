def read_single_digit(digit):
    han_digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return han_digits[digit]

def read_number(number):
    han_digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    
    hundred = number // 100
    ten = (number % 100) // 10
    one = number % 10

    result = read_single_digit(hundred) + ' '
    result += read_single_digit(ten) + ' '
    result += read_single_digit(one)

    return result.strip()

num = int(input('세 자리 정수 입력: '))
han_string = read_number(num)
print('한글 문자열:', han_string)


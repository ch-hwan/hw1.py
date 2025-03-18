def get_integer(amount):
    n500=amount//500
    amount%=500
    n100=amount//100
    amount%=100
    n50=amount//50
    amount%=50
    n10=amount//10
    amount%=10
    print('지폐교환금액:',amount)
    print('500원 동전의 개수:',n500)
    print('100원 동전의 개수:',n100)
    print('50원 동전의 개수:',n50)
    print('10원 동전의 개수:',n10)
money=int(input('동전으로 교환하고자하는 금액은?'))
get_integer(money)

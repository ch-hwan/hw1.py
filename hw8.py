def buy():
    cart = {}
    while True:
        print('[구입]')
        item = input('상품명? ')
        if item == '':
            break
        quantity = int(input('수량은? '))
        cart[item] = quantity
        print(f'장바구니에 {item} {quantity}개가 담겼습니다.')
    return cart

def show(cart):
    print(''>>> 장바구니 보기:', cart)

def find(cart):
    print('[검색]')
    item = input('장바구니에서 확인하고자 하는 상품은? ')
    if item in cart:
        print(f'{item}(은)는 {cart[item]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {item}(은)는 없습니다.')

cart = buy()
show(cart)
find(cart)

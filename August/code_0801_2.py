# 파일명 및 함수명을 변경하지 마시오.
def calc(equation):
    """
    아래에 코드를 작성하시오.
    equation은 덧셈 뺄셈으로 이루어진 수식 문자열입니다.
    계산된 결과를 정수로 반환합니다.
    """
    # return sum(list(map(int, ('0' + equation).replace('-', '+-').split('+'))))

    # equation 맨 앞에 부호를 붙여준다.
    if equation[0] == '+' or equation[0] == '-':
        equation = equation
    else:
        equation = '+' + equation

    # equation에서 '+'와 '-'의 위치를 addsub 리스트에 저장해준다.
    addsub = []
    for i in range(len(equation)):
        if equation[i] == '+' or equation[i] == '-':
            addsub.append(i)

    # '+', '-'위치를 이용해 숫자를 뽑아준다음 numbers에 저장해준다.
    numbers = []
    number = ''
    for n in range(1, len(addsub) + 1):
        # 마지막 부호 뒤의 숫자를 뽑아준다.
        if n == (len(addsub)):
            number = equation[addsub[n-1]:]
            numbers.append(number)

        else:
            number = equation[addsub[n-1]: addsub[n]]
            numbers.append(number)

    # numbers의 합을 구한다.
    result = 0
    for num in numbers:
        result += int(num)

    return result


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(calc('123+2-124'))
    print(calc('-12+12-7979+9191'))
    print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))
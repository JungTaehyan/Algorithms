# 올바른 형식, 값을 입력했는지 안했는지 예외처리를 진행했습니다.
while True:
    try:
        y_date = input("0000/00 년도와 월을 입력하세요.")
        year = int(y_date[0:4])
        month_1 = int(y_date[5:])
    except:
        print("올바른 날짜가 아닙니다. 다시 입력해주세요.")
        continue
    if year <= 0 or month_1 < 0 or month_1 > 12:
        print("올바른 날짜가 아닙니다. 다시 입력해주세요.")
    else:
        break
# 윤년과 평년을 윤년이면 True, 평년이면 False로 구하는 함수를 만들었습니다.
def isYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# 마지막 날짜 지정 함수 만들 때 2월의 마지막 날은 윤년인지 평년인지 고려하여 저장합니다.
def lastDay(year, month_1):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYear(year) == True:
        m[1] = 29
    else:
        m[1] = 28
    return m[month_1 - 1]
# 1년 1월 1일부터 구하고자 하는 달의 마지막 날짜까지의 총 일수를 구하는 함수를 만듭니다.
def totalDate(year, month_1, day):
    total = (year-1) * 365 + (year-1)//4 - (year-1)//100 + (year-1)//400
    for i in range(1, month_1):
        total += lastDay(year, i)
    return total + day
# 요일 지정 함수
def weekDay(year, month_1, day):
    return totalDate(year, month_1, day) % 7

# 달력 출력
print(' S  M  T  W  T  F  S')
# 처음 1일이 몇요일부터 출력되어야 하는지 알아야 하기 때문에 빈칸만큼 띄웁니다.
for k in range(weekDay(year, month_1, 1)):
    print('   ', end='')
# 해당 월의 날짜를 출력합니다.
for k in range(1, lastDay(year,month_1)+1):
    print('%2d ' % k, end = '')
    # 출력한 날짜가(k) 6이고 해당 월의 마지막 날짜가 아니면 줄을 바꿉니다.
    if weekDay(year, month_1, k)==6 and lastDay(year, month_1) != k:
        print()
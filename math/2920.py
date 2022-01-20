music = list(input().split())
music_int = list(map(int, music))


if music_int.sort() == music_int:
    print('ascending')
elif music_int.sort(reverse=True) == music_int:
    print('descending')
else:
    print('mixed')


a = list(map(int, input().split()))

if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')

# list.sort()은 list을 그 자리에서 정렬하고
# 목록 인덱스를 변경하고 None을 반환합니다.(모든 내부 작업은 동일, 원래 목록 영향 있음).
# sorted()는 새로운 정렬된 목록을 반환하며, 원래 목록은 영향을 받지 않습니다.
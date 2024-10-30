'''리스트 컴프리헨션'''
# d = [(x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]
# print(d)

'''딕셔너리 컴프리헨션'''
# squares_dict = {x: x**2 for x in range(1, 6)}
# print(squares_dict)

# scores = {'길동':80, '순희':68, '영희':85, '철수':65}
# grades = {name: 'PASS' if value > 70 else 'No-PASS' for name, value in scores.items()}
# print(grades)

'''세트 컴프리헨션'''
evens_set = {x for x in range(10) if x % 2 == 0}
print(evens_set)
mybooks = [
  {'제목':'안드로이드앱개발', '저자':'최전산', '출판사':'PCB', '가격':25000, '출판년도':2017},
  {'제목':'파이썬', '저자':'강수라', '출판사':'연두', '가격':23000, '출판년도':2019},
  {"제목":"자바스크립트", "저자" : "박정식", "출판사": "SSS", "가격": 38000, "출판년도": 2018},
  {"제목":"HTML5", "저자" : "주환", "출판사": "대한", "가격": 33000, "출판년도": 2012},
  {"제목":"컴파일러", "저자" : "장진웅", "출판사": "PCB", "가격": 24000, "출판년도": 2011},
  {"제목":"C언어", "저자" : "홍말숙", "출판사": "한국", "가격": 29000, "출판년도": 2010},
  {"제목":"프로그래밍언어론", "저자" : "현정숙", "출판사": "정의출판", "가격": 41000, "출판년도": 2009},
  {"제목":"안드로이드", "저자" : "이광희", "출판사": "한국", "가격": 42000, "출판년도": 2013},
  {"제목":"앱인벤터", "저자" : "박규진", "출판사": "대한", "가격": 30000, "출판년도": 2015}
]

def select_menu():
  choice = int(input("""도서 입력 / 검색
  1. 도서 입력
  2. 도서명으로 검색
  3. 저자명으로 검색
  4. 출판사명으로 검색
  5. 종료
  선택(1, 2, 3, 4, 5) : """))

  return choice

def book_insert():
  t = input('* 제목 >> ')
  a = input('* 저자명 >> ')
  p = input('* 출판사명 >> ')
  pr = int(input('* 가격 >> '))
  y = int(input('* 출판년도 >> '))
  mybooks.append({'제목':t, '저자':a, '출판사':p, '가격':pr, '출판년도':y})
  return 1

def book_search(kwd):
  userin = input(kwd + " >>> ")

  n = 0
  for onebook in mybooks:
    #if userin == onebook[kwd]:
    if onebook[kwd].find(userin) >= 0:
      print(onebook['제목'], onebook['저자'], onebook['출판사'], onebook['가격'])
      n += 1

  return n

while True:
  choice = select_menu()

  if choice == 1:
    print(book_insert() , '권이 추가되었습니다.')
  elif choice == 2:
    print(book_search('제목') , '권을 검색했습니다.')
  elif choice == 3:
    print(book_search('저자') , '권을 검색했습니다.')
  elif choice == 4:
    print(book_search('출판사') , '권을 검색했습니다.')
  elif choice == 5:
    break
  else:
    print('입력이 잘못되었어요, 다시 선택하세요')
friend_list = [
    {
        "이름": "류양현",
        "전화번호": "010-6500-2930",
        "출신 고등학교": "남원용성고",
        "고향": "울산",
    },
    {
        "이름": "강지석",
        "전화번호": "010-2371-5206",
        "출신 고등학교": "남원용성고",
        "고향": "남원",
    },
    {
        "이름": "강철진",
        "전화번호": "010-4740-5363",
        "출신 고등학교": "남원용성고",
        "고향": "마천",
    },
]


def selet_number():
    choose = int(
        input(
            """\
                          1. 친구 추가
                          2. 친구 삭제
                          3. 친구 이름 변경
                          4. 친구 리스트 출력
                          5. 종료
                          번호를 입력하여 주세요: """
        )
    )
    return choose


def new_friend():
    name = input("이름: ")
    number = input("전화번호: ")
    highschool = input("출신 고등학교: ")
    hometown = input("고향: ")
    friend_list.append(
        {
            "이름": name,
            "전화번호": number,
            "출신 고등학교": highschool,
            "고향": hometown,
        }
    )
    return 1


def del_friend():
    del_name = input("삭제할 친구의 이름: ")
    global friend_list
    friend_list = [friend for friend in friend_list
                   if friend.get("이름") != del_name]
    return 2


def chg_frd_name():
    name = input("친구 이름: ")
    change_name = input("새로운 친구 이름: ")
    for item in friend_list:
        if item["이름"] == name:
            item["이름"] = change_name
    return 3


def print_list():
    for key in friend_list:
        print(key)
    return 4


while True:
    choose = selet_number()

    if choose == 1:
        new_friend()
        print("친구가 추가되었습니다.")
    elif choose == 2:
        del_friend()
        print("친구가 삭제되었습니다.")
    elif choose == 3:
        chg_frd_name()
        print("친구의 이름이 변경되었습니다.")
    elif choose == 4:
        print_list()
        print("친구 리스트를 출력하였습니다.")
    elif choose == 5:
        print("종료합니다.")
        break
    else:
        print("잘못 입력되었습니다. 다시 입력하세요.")

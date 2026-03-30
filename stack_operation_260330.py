# (숙제) stack연산음 함수로 구현
stack = [] 
capacity = 5
def push(data):
    if is_full(stack):
        print("스택이 가득 찼습니다")
        return  
    else:
        stack.append(data)
def pop(stack):
    if len(stack) == 0:
        return None
    return stack.pop()
def peek(stack):
    if len(stack) == 0:
        return None
    return stack[-1]

def is_full(stack):
    return len(stack) == capacity

print("[정수형 스택 연산 실습 (용량 5)]")
print("===============================")
print("1. Push 2. Pop 3. Peek 0. Exit")
print("===============================")
print(f"스택 상태: {stack}")
while True:
    choice = input("메뉴를 선택하세요: ")
    if choice == '1':
        data = int(input("추가할 정수를 입력하세요: "))
        push(data)
    elif choice == '2':
        popped_data = pop(stack)
        if popped_data is not None:
            print(f"팝된 데이터: {popped_data}")
        else:
            print("스택이 비어 있습니다.")
        print(f"스택 상태: {stack}")
    elif choice == '3':
        top_data = peek(stack)
        if top_data is not None:
            print(f"탑 데이터: {top_data}")
        else:
            print("스택이 비어 있습니다.")
    elif choice == '0':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 시도하세요.")
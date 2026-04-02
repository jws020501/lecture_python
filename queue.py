from collections import deque
queue = deque()
while 1:
    menu = int(input("메뉴를 입력하세요 (1: Enqueue, 2: Dequeue, 3: Get Front, 4: Show Queue  0: Exit): "))
    if menu == 1:
        value = int(input("값을 입력하세요: "))
        queue.append(value)
        print(f"Enqueued: {value}")
    elif menu == 2:
        if queue:
            value = queue.popleft()
            print(f"Dequeued: {value}")
        else:
            print("큐가 비어있습니다.")
    elif menu == 3:
        if queue:
            print(f"Front: {queue[0]}")
        else:
            print("큐가 비어있습니다.")
    elif menu == 4:
        print(f"Queue: {list(queue)}")

    elif menu == 0:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 메뉴입니다. 다시 시도하세요.")
    
import sys
sys.stdin = open('계산기_input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(input())

    print(arr)
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    priority = ['(', '+', '*']
    stack = []
    result = []

    # print(priority.index('+'))
    # print(priority.index('*'))
    for i in range(N):
        if arr[i] == '(':
            stack.append(arr[i])

        elif arr[i] in nums:
            result.append(arr[i])

        elif arr[i] == '*' or arr[i] == '+':
            if len(stack) != 0:
                if priority.index(arr[i]) > priority.index(stack[-1]):
                    stack.append(arr[i])
                elif priority.index(arr[i]) <= priority.index(stack[-1]):
                    while 1:
                        result.append(stack.pop())
                        if priority.index(arr[i]) > priority.index(stack[-1]):
                            stack.append(arr[i])
                            break
            else:
                stack.append(arr[i])

        # elif arr[i] == ')':
        #     while 1:
        #         result.append(stack.pop())
        #         if stack[-1] == '(':
        #             stack.remove(stack[-1])
        #             break

    while len(stack) != 0:
        result.append(stack.pop())

    print(result)
    print(stack)

    # acc = '7-8+9'
    # print(acc)
    # print(7-8+9)

    # stack = []
    # result = []
    # nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # icp = [')', '+', '*', '('] # stack 안
    # isp = ['(', '+', '*', ')']
    #
    #
    # print(isp.index('+'))
    #
    # for i in range(N):
    #     if arr[i] not in nums:
    #         if arr[i] == '(':
    #             stack.append(arr[i])
    #
    #         elif icp.index(stack[-1]) > icp.index(arr[i]):
    #             stack.append(arr[i])
    #
    #         elif icp.index(stack[-1]) == icp.index(arr[i]):
    #             while 1:
    #                 result.append(stack[-1])
    #                 stack.remove(stack[-1])
    #                 if icp.index(stack[-1]) < icp.index(arr[i]):
    #                     stack.append(arr[i])
    #                     break
    #
    #         elif arr[i] == icp[0]:
    #             while 1:
    #                 result.append(stack[-1])
    #                 stack.remove(stack[-1])
    #                 if stack[-1] == icp[-1]:
    #                     result.append(stack[-1])
    #                     stack.remove(stack[-1])
    #                     break
    #
    #     elif arr[i] in nums:
    #         result.append(int(arr[i]))
    #     # else:
    #     #     print(arr[i], end='')
    #
    # while len(stack) != 0:
    #     result.append(stack[-1])
    #     stack.remove(stack[-1])

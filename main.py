# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Game import Game


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# def explodeStack(stack, index: int, newStack: list):
#     del stack[index]
#     i = index
#     for chip in newStack:
#         print(chip)
#         stack.insert(i, chip)
#         i = i + 1
#     return stack
#
#
# def possible_sum(x: int):
#     possibles: list[list]
#     possibles = []
#
#     for i in range(1, x // 2):
#         possibles.append([x - i, i])
#     if x % 2 != 0:
#         possibles.append([x // 2 + 1, x - (x // 2 + 1)])
#     return possibles
#
# def max(x:list):
#
#     # Possible values for maxv are:
#     # -1 - loss
#     # 1  - win
#
#     # We're initially setting it to -2 as worse than the worst case:
#     maxv = float('-inf')
#
#     index = None
#     sum_list = None
#
#
#     # If the game came to an end, the function needs to return
#     # the evaluation function of the end. That can be:
#     # -1 - loss
#     # 1  - win
#
#
#
#     # stackBefore = self.current_state
#     for i in range(0, len(x)):
#         # test if the chips is greater than two then we can still devid it
#         if x[i] > 2:
#             stackBefore1 = x
#             sum_list = possible_sum(x[i])
#             print(sum_list)
#             for sum in sum_list:
#                 # stackBefore = self.current_state
#                 # here sum is a list composed of the two numbers in the sum of current number for exple 7 => [6,1]
#                 x=explodeStack(x,i, sum)
#                 print('iter i ='+str(i))
#                 print(x)
#                 x=stackBefore1
#                 # self.current_state=stackBefore
#             # self.current_state=stackBefore1
#
# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chips = int(input('insert initial chips number'))
    g = Game(chips)
    g.play()
# print_hi('PyCharm')
# print(explodeStack([5, 2, 2, 1], 0, [3, 2]))
# possible_sum(7)
#     max([7])
    # x=[1,2,3]
    # cp=copy.deepcopy(x)
    # y=explodeStack(x,2,[2,1])
    # print(x)
    # print(y)
    # #y=[3,4,5,6,7]
    # y=x
    # print(cp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

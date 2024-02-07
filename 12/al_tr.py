# def main():
#     num = 0
#     show_me(num)
#
# def show_me(arg):
#     print(arg)
#     if arg == 10:
#         show_me(arg + 1)
#
#
# if __name__ == '__main__':
#     main()

#
def traffic_sign(n):
    if n > 0:
        print('No parcing')
        traffic_sign(n - 1)
#
# def traffic_sign(n):
#     while n > 0:
#         print('No parking')
#         n -= 1

traffic_sign(5)
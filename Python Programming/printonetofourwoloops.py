# def dispnum1(n):
#     print(n)
#     dispnum2(n+1)
#     # return

# def dispnum2(n):
#     print(n)
#     dispnum3(n+1)
#     # return

# def dispnum3(n):
#     print(n)
#     dispnum4(n+1)
#     # return
    
# def dispnum4(n):
#     print(n)
#     # return

# dispnum1(1)

def dispnum(n):
    if n > 4:
        return
    print(n)
    dispnum(n+1)
    return

dispnum(1)
Pin=input(":رمز خود را وارد کنید ")
try:
    Pin=int(Pin)
except ValueError:
    print('لطفا یک عدد را وارد کنید')
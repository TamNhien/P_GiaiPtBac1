a = float(input("Nhập giá trị của a : "))
b = float(input("Nhập giá trị của b : "))

# Kiểm tra a có bằng 0 không để tránh chia cho 0
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print("Nghiệm của phương trình là : ", x)


import random
import math

# 1. 选择素数p和原根g
p = 223  # 素数p
g = 5    # 原根g

# 2. 验证p是否是素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 验证p是否为素数
if not is_prime(p):
    raise ValueError(f"{p} 不是素数")

# 3. 计算一个随机私钥a和b
def generate_private_key():
    return random.randint(1, p-1)

# 成员A和成员B选择自己的私钥
a = generate_private_key()  # A的私钥
b = generate_private_key()  # B的私钥

# 4. 计算公钥A和B
def calculate_public_key(private_key, g, p):
    return pow(g, private_key, p)

# 成员A和B计算公钥
A = calculate_public_key(a, g, p)
B = calculate_public_key(b, g, p)

# 5. 交换公钥并计算共享密钥
def calculate_shared_key(public_key, private_key, p):
    return pow(public_key, private_key, p)

# A计算共享密钥
K_A = calculate_shared_key(B, a, p)

# B计算共享密钥
K_B = calculate_shared_key(A, b, p)

# 输出结果
print(f"选定素数p = {p}, 原根g = {g}")
print(f"成员A的私钥a = {a}, 公钥A = {A}")
print(f"成员B的私钥b = {b}, 公钥B = {B}")
print(f"成员A计算的共享密钥K_A = {K_A}")
print(f"成员B计算的共享密钥K_B = {K_B}")

# 确保两者计算的共享密钥相同
assert K_A == K_B, "共享密钥不一致！"
print(f"共享密钥一致: {K_A}")

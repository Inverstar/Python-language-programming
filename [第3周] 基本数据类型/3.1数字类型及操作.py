# 数字类型及操作

## 1. 整数类型
import sys

sys.set_int_max_str_digits(100000) 
p2_3 = pow(2, 3)  # 2的3次方
p2_2_15 = pow(2,pow(2,15))  # 2的32768次方

print(p2_3)  # 8
# print(p2_2_15)  # 32768

print(len(str(p2_2_15)))  # 打印数字的位数

### 二进制
print(bin(2))  # 0b10
a = 0b10000
print(a,'十进制')  # 16
print(format(a, 'b'))   # 二进制
print(format(a, 'o'))   # 八进制
print(format(a, 'x'))   # 十六进制
print(format(a, 'd'))   # 十进制
### 八进制
print(oct(8))  # 0o10
### 十六进制
print(hex(16))  # 0x10

## 2. 浮点数类型

#浮点数的取值范围是有限的，在-10的307次方到10的308次方之间，精度为10的-16次方
print(0.1+0.2) #浮点数计算存在不确定尾数
print(round(0.1+0.2, 16)) #四舍五入,d是小数点后保留的位数
print(4.3e-3,9.6E3,9.5E+3)  # 科学计数法

## 3. 复数类型

z = 1.23e-4 + 5.67e-8j
print(z)  # (0.000123+5.67e-08j)
print(z.real)  # 实部
print(z.imag)  # 虚部
print(z.conjugate())  # 共轭复数

## 4. 数值运算操作符

print(3/2)  # 1.5
print(3//2)  # 1
print(3%2)  # 1
print(3**2)  # 9    
print(3**0.5)  # 1.7320508075688772

## 5. 数值运算函数

print(abs(-3))  # 3
print(divmod(3, 2))  # (1, 1)  商和余数
print(pow(2, 3, 3))  # 幂余，2**3%3=3
print(max(1, 2, 3))  # 3
print(min(1, 2, 3))  # 1
print(int(3.5))  # 3
print(float(3))  # 3.0     
print(complex(3, 4))  # (3+4j)
print(complex(3))
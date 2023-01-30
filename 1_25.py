from functools import reduce

print ('Hello,World')

# 1から50までの和を計算して表示
# for文
s=0
for x in range(1,51):
    s+=x
print(s)

# sumを使った方法
print (sum(range(1,51)))

# generator式
print(sum(i for i in range(1,51)))

#reduceを使う
# ※reduce:高階関数
# from functools import reduceとしてインポートが必要
# reduce(lambda 第1引数,第2引数: 式, 範囲)
print(reduce(lambda x,y: x+y, range(1,51)))

# 2つの自然数の最大公約数を求める（ユークリッドの互除法）

#再帰関数
def gcd_r(a, b):
    if b==0:
        return a
    else:
        return gcd_r(b, a % b)
    
print(gcd_r(48,36))
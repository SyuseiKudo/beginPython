import function as fu

# 変数
# ;なし。型の宣言なし。定数は存在しない
# 慣習：最初に[_(アンスコ）)]もしくは英字
number  = 1
string = "テスト"

print(number)
print(string)

# *で、変数の値を反復できる
print(string * 3)

# 数値を文字列にキャストする
print(str(number) + string)

# リストの作成
list = []
list.append("python")
list.append("java")
print(list)
# 指定削除
list.remove("python")
print(list)
list.append("python")
# インデックス削除
print(list)
del list[1]
print(list)
# 全削除
list.clear()
print(list)

# リスト内包表記
# リストをfor文などで作成することができる
# ** = 累乗
squares = [i**2 for i in range(5)]
print(squares)

# if文で指定した値のみを抽出することも可能
odds = [i for i in range(10) if i % 2 == 0]
print(odds)

if len(odds) > 3:
    print("要素数3以上")
else:
    print("要素数3以下")

odd_even = ['odd' if i % 2 == 1 else 'even' for i in range(10)]
print(odd_even)

# 連想配列型
dictionary = {"name":"syusei","email":"gmail.com"}
print(dictionary["name"])

# for
# 末尾に:がついたらインデントする
for i in range(10):
    if i%2 == 0:
        print("{} is even.".format(i))
    else:
        print("{} is odd.".format(i))

# 標準入力 input()
print("名前を入力")
name = input()
print("名前は"+name)

# 別ファイルの関数呼び出し
resultPlus = fu.plus(1,2)
print(resultPlus)



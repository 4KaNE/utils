"""format関数の細かい使い方"""

# 基本
food = "cake"
text = "{} is lie".format(food)
print(text)
# cake is lie

age = 17
text = "永遠の{}歳".format(age)
print(text)
# 永遠の17歳

# formatされた文章はあくまで戻り値として渡されるものであり、
# 元の変数に直接代入操作がされているわけではない
text = "{}"
text.format("hoge")
print(text)
# {}

# 位置引数を使ったアクセス
text = "{}\n{}".format("FINAL FANT", "ASY")
# text = "{0}\n{1}".format("FINAL FANT", "ASY")と等価
print(text)

text = '{2}, {1}, {0}'.format(*'abc')
print(text)

text = '{0}{1}{0}'.format('abra', 'cad')
print(text)

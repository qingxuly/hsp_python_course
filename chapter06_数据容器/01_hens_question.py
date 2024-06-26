hen1 = 3
hen2 = 5
hen3 = 1
hen4 = 3.4
hen5 = 2
hen6 = 50
total_weight = hen1 + hen2 + hen3 + hen4 + hen5 + hen6
avg_weight = total_weight / 6
print(f"总体重：{total_weight} 平均体重：{round(avg_weight, 2)}")

# 列表解决养鸡场问题
hens = [3, 5, 1, 3.4, 2, 50]
total_weight = 0.0
for ele in hens:
    total_weight += ele
print(f"总体重：{total_weight} 平均体重：{round(total_weight/len(hens), 2)}")

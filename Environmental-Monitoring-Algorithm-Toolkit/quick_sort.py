"""
环境监测场景快速排序应用
功能：对水质监测点的COD值进行排序，快速识别污染最严重区域
"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]['COD']  # 以COD值为排序基准
    left = [x for x in arr if x['COD'] < pivot]
    middle = [x for x in arr if x['COD'] == pivot]
    right = [x for x in arr if x['COD'] > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 模拟数据测试
if __name__ == "__main__":
    test_data = [
        {"location": "A区", "COD": 45},
        {"location": "B区", "COD": 32},
        {"location": "C区", "COD": 78}  # 异常高值
    ]
    sorted_data = quick_sort(test_data)
    print("污染严重度排名：", [d['location'] for d in sorted_data])
# 双指针算法在环境监测中的应用

## 场景：检测水质参数连续异常波动
**业务需求**：当某监测点连续3小时COD>50时触发警报

## 算法实现
```python
def detect_anomaly(data):
    left = 0
    for right in range(len(data)):
        # 当发现异常数据时移动左指针
        if data[right]['COD'] <= 50:
            left = right + 1
        # 当窗口长度≥3时触发警报
        if right - left + 1 >= 3:
            print(f"警报！{data[left]['timestamp']}至{data[right]['timestamp']持续异常")
            break
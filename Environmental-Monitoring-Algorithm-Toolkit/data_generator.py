import csv
import random
from datetime import datetime, timedelta


def generate_water_data(num=100):
    """生成模拟水质监测数据"""
    data = []
    base_date = datetime.now()
    for i in range(num):
        # 生成正常数据（90%概率）
        if random.random() < 0.9:
            cod = round(random.uniform(20, 50), 1)
            ph = round(random.uniform(6.5, 8.5), 1)
        # 生成异常数据（10%概率）
        else:
            cod = round(random.uniform(80, 120), 1)
            ph = round(random.uniform(4.0, 5.5), 1)

        data.append({
            "timestamp": (base_date - timedelta(hours=i)).isoformat(),
            "COD": cod,
            "pH": ph,
            "location": f"监测点-{random.randint(1, 5)}"
        })

    # 写入CSV
    with open('water_data.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    generate_water_data(200)  # 生成200条数据
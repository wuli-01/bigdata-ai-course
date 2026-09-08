# -*- coding: utf-8 -*-
"""第一个 Python 程序：环境自检 + 打招呼"""

import sys

print("Hello, 大数据与人工智能!")
print(f"Python 版本: {sys.version.split()[0]}")

# 小演示：列表与循环
skills = ["Python", "SQL", "Hadoop", "Spark", "机器学习"]
print("\n本课程要学习的技能:")
for i, s in enumerate(skills, 1):
    print(f"  {i}. {s}")

# 第二课：Python 基础与第一个程序

## Python 是什么

Python 是人工智能和大数据领域最流行的编程语言，语法简洁、库丰富，
是本课程的主要工具。

## 第一个程序

创建 `homework/hello.py`：

```python
print("Hello, 大数据与人工智能!")
```

在终端运行：

```bash
python homework/hello.py
```

## 基础语法速览

### 变量与数据类型

```python
name = "Python"        # 字符串 str
version = 3.12         # 浮点数 float
year = 2026            # 整数 int
is_fun = True          # 布尔值 bool
```

### 列表与循环

```python
skills = ["Python", "SQL", "Hadoop", "Spark"]
for s in skills:
    print("要学:", s)
```

### 函数

```python
def greet(who):
    return f"Hello, {who}!"

print(greet("大数据"))
```

## 本课小练习

1. 修改 `hello.py`，让它打印你的名字
2. 写一个循环打印 1~10 的平方
3. 把改动用 git 提交：`git add . && git commit -m "第二课练习" && git push`

## 小结

- Python 用缩进表示代码块（4 个空格）
- `print()` 输出、`#` 注释
- 变量不需要声明类型，直接赋值

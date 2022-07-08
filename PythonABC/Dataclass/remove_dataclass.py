#https://www.pythonmorsels.com/match-case-parsing-python/
'''
最近我熬过了睡觉时间，做了一个脚本，后来又做了一个网络应用程序，把一个数据类转换为一个非数据类。这个网络应用是由Python的WebAssembly构建的（它也为我的Python pastebin工具提供动力）。

在制作这个脚本时，我发现有借口使用奇怪的Python特性，其中最有趣的是Python的匹配-case语句。

Python 3.10增加了一个匹配大小写块，人们通常认为它等同于其他编程语言的开关大小写块。虽然你可以像 switch-case 一样使用 match-case，但你通常不会这样做： match-case 比 switch-case 更强大，也更复杂。Python 的 match-case 块是用于结构模式匹配的 -- 这句话听起来很复杂，因为它确实很复杂

我很快就会写一篇后续文章，介绍这个脚本在高层次上是如何工作的，但现在我想谈谈我使用结构模式匹配来编写这段代码的冒险。

为什么要删除数据类？
首先让我们简单地谈谈我为什么要做这个工具。

为什么有人想把一个数据类转换成 "非数据类"？

使用数据类是有代价的：性能问题（通常并不重要）和事情变得奇怪的边缘情况（__slots__和slots=True都是有问题的）。
但是我创建这个数据类到普通类的转换器的原因是为了帮助我更好地教授数据类。看到一个数据类的等价代码可以帮助我们理
解数据类对我们的作用。

好了，让我们深入了解一下匹配案例。

哦，这就是那个工具的作用？
我知道我正在进行的冒险涉及到解析Python代码。我通常不解析Python代码。我把它留给像 Black、flake8 和 Python
解释器本身这样的工具。

但是我知道 Python 的 ast 模块有一个解析函数，它可以接受一个代表 Python 代码的字符串，并返回一个代表该 Python
代码的 "抽象语法树"（通常简称为 AST）。

使用 ast.parse 得到一棵 AST 节点的树很容易。困难的部分在于如何理解这些深度嵌套的 AST 节点。

我发现自己写了很多具有非常复杂条件的if-elif块。以这段代码为例。




if isinstance(node, ast.Call):
    if (isinstance(node.func, ast.Attribute)
            and node.func.value.id == "dataclasses"
            and node.func.attr == "dataclass"):
        return True
    elif node.func.id == "dataclass":
        return True
elif (isinstance(node, ast.Attribute)
        and node.value.id == "dataclasses"
        and node.value.attr == "dataclass"):
    return True
elif isinstance(node, ast.Name) and node.id == "dataclass":
    return True
else:
    return False

'''
'''
如何创建条形图竞赛(Python)
现在比较流行的数据可视化之一是动画条形图，其中的条形图看起来像是在互相比赛。创建你自己的条形图竞赛出乎意料的简单，而且不需要花太多时间。

如果你还没有安装两个库，你需要安装它们。我使用homebrew，它使库的安装非常容易。如果你还没有homebrew，我建议你在继续之前安装它。在你的终端，你需要使用代码：brew install ffmpeg。这是一个将对你的数据进行编码以用于动画制作的软件。


首先导入所有必要的库。

接下来pip安装bar_chart_race。我在我的jupyter笔记本里做了这个，但你也可以在你的终端里做这个。

在你的笔记本中，将bar_chart_race导入为bcr

bcr在他们的github上链接了一些例子。在这篇文章中，我将展示Covid-19的死亡。

最终产品为我们提供了一个条形图竞赛，显示日期、Covid-19的死亡人数，以及每个国家增加其数字的速度。

你可以使用你自己的csv文件或excel表的数据，只要它有足够的信息。
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pip install bar_chart_race


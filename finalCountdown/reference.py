
import time
import tkinter as tk

def __writeText():
    text.insert(tk.END, str(time.time())+'\n')
    root.after(1000, __writeText)  # again forever

root = tk.Tk()
text = tk.Text(root)
text.pack()
root.after(1000, __writeText)
root.mainloop()

'''
————————————————
版权声明：本文为CSDN博主「华岭羊仔」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/s_zhchluo/article/details/120891787
'''
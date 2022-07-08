'''
####### 库存书的数量修改函数 ######
####### book module 搜索书函数 ######
系统初始化，提取图书、会员和日志库...
Traceback (most recent call last):
  File "C:\Users\29358\PycharmProjects\BooktinyMis\bookMis—_goLife\2022-03-31.py", line 330, in <module>
    manager = Bookmis()  # 类的实例化
  File "C:\Users\29358\PycharmProjects\BooktinyMis\bookMis—_goLife\2022-03-31.py", line 73, in __init__
    self.bookpick, self.userpick, self.logpick = self.loadpick()
  File "C:\Users\29358\PycharmProjects\BooktinyMis\bookMis—_goLife\2022-03-31.py", line 97, in loadpick
    bookdf = pd.read_csv(self.book_table, low_memory=False, encoding="gbk")  # 防止弹出警告
  File "D:\ProgramData\Anaconda\lib\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "D:\ProgramData\Anaconda\lib\site-packages\pandas\io\parsers\readers.py", line 586, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "D:\ProgramData\Anaconda\lib\site-packages\pandas\io\parsers\readers.py", line 482, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "D:\ProgramData\Anaconda\lib\site-packages\pandas\io\parsers\readers.py", line 811, in __init__
    self._engine = self._make_engine(self.engine)
  File "D:\ProgramData\Anaconda\lib\site-packages\pandas\io\parsers\readers.py", line 1040, in _make_engine
    return mapping[engine](self.f, **self.options)  # type: ignore[call-arg]
  File "D:\ProgramData\Anaconda\lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 51, in __init__
    self._open_handles(src, kwds)
  File "D:\ProgramData\Anaconda\lib\site-packages\pandas\io\parsers\base_parser.py", line 222, in _open_handles
    self.handles = get_handle(
  File "D:\ProgramData\Anaconda\lib\site-packages\pandas\io\common.py", line 585, in get_handle
    if _is_binary_mode(path_or_buf, mode) and "b" not in mode:
  File "D:\ProgramData\Anaconda\lib\site-packages\pandas\io\common.py", line 962, in _is_binary_mode
    return isinstance(handle, binary_classes) or "b" in getattr(handle, "mode", mode)
TypeError: argument of type 'method' is not iterable
书、会员和日志共 3 张 table 信息读取成功...
'''


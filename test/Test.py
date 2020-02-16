from plugins import SearchSb
import os

#sb工具：输入内容即可搜索并随机输出搜索内容之一，回车即可随机输出
str = input()
print(SearchSb.search(str))
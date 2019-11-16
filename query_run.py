# coding:utf8
import os, sys
import jieba

ROOT_DIR = './out'


def search_level_first(path: str, w: str) -> list:
    """
    遍历第一层文件夹，获取一级分类
    :param path:
    :param w:
    :return:
    """
    return [os.path.join(path, i) for i in os.listdir(path) if w in i]


def search_level_all(path: str, w: str) -> list:
    """
    遍历path下所有子文件
    @param: path    磁盘路径地址
    @param: w       关键词检索.子文件名包含w的会return
    """
    rs = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if w in file:
                rs.append(os.path.join(root, file))
    return rs


def main(w1, w2, limit):
    """
    主入口，搜索特定关键词的表情包
    :param w1: 一级分类
    :param w2: 关键词
    :param limit: 回显条数
    :return:
    """
    rs = []
    f1 = search_level_first(ROOT_DIR, w1)
    for r in f1:
        # 先从一级分类里找到符合条件的关键词
        for rr in search_level_all(r, w2):
            if len(rs) >= limit:
                # 达到limit条数限制，break
                break
            rs.append(rr)
    if len(rs) < limit:
        # 当通过w1查询不到的话，再延伸到所有目录下
        for w in jieba.cut(w2, cut_all=False):
            for rr in search_level_all(ROOT_DIR, w):
                if len(rs) >= limit:
                    # 达到limit条数限制，break
                    break
                rs.append(rr)
    return rs


# 显示条数
LIMIT = 5
# 返回值
r = []
if len(sys.argv) == 3:
    r = main(sys.argv[1], sys.argv[2], LIMIT)
else:
    r = main('蘑菇头', '科普', LIMIT)
print('\n'.join(r))

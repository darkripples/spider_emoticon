# coding:utf-8

import time, datetime, os, traceback
from threading import Thread
from multiprocessing.pool import Pool
import requests
from lxml import etree

from ez_utils import flog, allot_list, err_check


# 进程数
PCNT = 2
# 线程数
TCNT = 10

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}

# 蘑菇头表情包
SAVE_PATH = './out/蘑菇头'
url_base = 'https://fabiaoqing.com/tag/detail/id/2/page/%s.html'
URL_LIST = [url_base % i for i in range(1, 2)]


def save_img(img_url, path, name):
    """
    保存图片
    :param img_url:
    :param path:
    :param name:
    :return:
    """
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(os.path.join(path, name)):
            with open(os.path.join(path, name), 'wb') as f:
                f.write(requests.get(img_url, headers=HEADERS, timeout=(10, 25)).content)
    except Exception as e:
        traceback.print_exc()
        flog.debug(">>>>>>>>>>>save-error:" + img_url)


def doWork(par1: str, par2: str = 'par2', par3: str = 'par3'):
    """
    爬取操作主入口
    :param par1:
    :param par2: 备用参数
    :param par3: 备用参数
    :return:
    """
    flog.debug("work\t" + par1)
    try:
        resp = requests.get(par1, headers=HEADERS, timeout=(20, 60))
        html = etree.HTML(resp.content.decode('utf8'))
        h = html.xpath('//div[@class="tagbqppdiv"]/a/img')
        for r in h:
            img_url = r.xpath('@data-original')[0]
            img_title = r.xpath('@title')[0].strip()
            file_name = img_title.split(' ')[0]
            if '-' in img_title:
                file_name = img_title.split('-')[0]
            if '_' in img_title:
                file_name = img_title.split('_')[0]
            # save
            save_img(img_url, SAVE_PATH, file_name + '.' + img_url.split('.')[-1])
    except Exception as e:
        traceback.print_exc()
        flog.debug(">>>>>>>>>>>error:" + par1)


def run_multithread(id: str, workPars: list, threadsCnt: int):
    # flog.debug(id + '当前进程任务:' + ( " ".join(str(i) for i in workPars) ))
    begin = 0
    # start = time.time()
    while 1:
        _threads = []
        urls = workPars[begin: begin + threadsCnt]
        if not urls:
            break
        for i in urls:
            t = Thread(target=doWork, args=(i,))
            _threads.append(t)
        for t in _threads:
            t.setDaemon(True)
            t.start()
        for t in _threads:
            t.join()
        begin += threadsCnt
    # end = time.time()
    # flog.debug(id + '当前进程耗时:%.2fs' % ( (end - start) ))


@err_check
def mixed_process_thread_crawler(processorsCnt: int, threadsCnt: int):
    pool = Pool(processorsCnt)
    workPars = URL_LIST
    url_groups = allot_list(workPars, processorsCnt)
    flog.debug("``总任务组数:" + str(len(url_groups)))
    cnt = 0
    for par_group in url_groups:
        cnt += 1
        pool.apply_async(run_multithread, args=(str(cnt), par_group, threadsCnt))
    pool.close()
    pool.join()


if __name__ == '__main__':
    flog.debug("``START>>" + datetime.datetime.now().strftime('%Y/%m/%d-%H:%M:%S'))
    mixed_process_thread_crawler(PCNT, TCNT)
    flog.debug("``END>>" + datetime.datetime.now().strftime('%Y/%m/%d-%H:%M:%S'))

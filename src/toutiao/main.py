#!/usr/bin/env python
from toutiao.crew import ToutiaoCrew
import datetime
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def run():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'toutiao_description': input('请输入页面描述: ').encode('utf-8').decode('utf-8'),
        'topic_of_the_week': input('请输入本周话题: ').encode('utf-8').decode('utf-8'),
    }
    # inputs = {
    #     'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
    #     'toutiao_description': input('Enter the page description here: '),
    #     'topic_of_the_week': input('Enter the topic of the week here: '),
    # }
    ToutiaoCrew().crew().kickoff(inputs=inputs)
    

# def run():
#     # 替换为您的输入,它将自动插入任何任务和代理信息
#     try:
#         media_description = input('请输入页面描述: ')
#         topic_of_the_week = input('请输入本周主题: ')
#         inputs = {
#             'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
#             'media_description': media_description,
#             'topic_of_the_week': topic_of_the_week,
#         }
#         ToutiaoCrew().crew().kickoff(inputs=inputs)
#     except KeyboardInterrupt:
#         print('\n操作已取消。')
#     except Exception as e:
#         print(f'发生错误: {e}')
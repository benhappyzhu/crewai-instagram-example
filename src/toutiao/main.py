from toutiao.crew import ToutiaoCrew
import datetime

def run():
    try:
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
    except KeyboardInterrupt:
        print('\n操作已取消。')
    except Exception as e:
        print(f'发生错误: {e}')
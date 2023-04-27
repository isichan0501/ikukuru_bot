from BotHelper import get_sheet_with_pd, set_sheet_with_pd, writeSheet, change_cell

from dotenv import load_dotenv
import os
import sys
import logging
from tinydb import TinyDB, Query, where
import re

from ChatBotHelper.util_chat import ChatbotUtil

        
# 環境変数を参照
load_dotenv()
SHEET_NAME = os.getenv('SHEET_NAME')



def save_temple(content):
    with open('temple.txt', 'a', encoding='utf-8') as f:
        f.write(content)


def modify_temple_with_chatgpt(tem_ple):
    change_keys = ["prof", "prof_a", "title_p", "text_p", "title_a", "text_a"]
    content = "\n--------------{}--------------\n".format(tem_ple['cnm'])
    save_temple(content)
    for ky in change_keys:
        content = "\n--------------{}--------------\n".format(ky)
        #言い換えようプロンプト
        # prompt = """以下の文章を意味合いを保ちつつ、なるべく口調や言い回し等が多彩になるよう言い換えてください。3つ挙げてほしいので、まずは1つ目の文章を作成してください。\n\n"""
        prompt = ""
        if 'title' in ky:
            prompt += "文字数をなるべく変えないようにして、"
        prompt += "以下の文章を、意味合いを保ちつつ、顔文字や絵文字などの使い方も参考にしながら、できるだけ重複を避けて、３通りに言い換えてください。\n\n"
        prompt += tem_ple[ky]
        cb = ChatbotUtil()
        res = cb.ask_chat(prompt)
        if not res:
            import pdb;pdb.set_trace()
        content += res
        save_temple(content)
        
        


def main():
    df = get_sheet_with_pd(sheetname=SHEET_NAME)
    #PCMAXのIDのあるアカウントだけ
    df.dropna(subset=['pc'], inplace=True)    
    for cnm in df['cnm'].to_list():
        tem_ple = df[df['cnm'] == cnm].to_dict(orient='records')[0]
        modify_temple_with_chatgpt(tem_ple)




def get_not_end_cnm(cnm_list):
    with open('temple.txt', 'r', encoding='utf-8') as f:
        lines = [x.strip() for x in f.readlines() if '--------------' in x]

    match_list = []
    for text in lines:
        match = re.search(r"--------------(.*?)--------------", text)
        if match:
            val = match.group(1)
            match_list.append(val)

    return list(set(cnm_list) - set(match_list))


if __name__ == "__main__":
    df = get_sheet_with_pd(sheetname=SHEET_NAME)
    #PCMAXのIDのあるアカウントだけ
    df.dropna(subset=['pc'], inplace=True)

    cnm_list = get_not_end_cnm(cnm_list=df['cnm'].to_list())
    # import pdb;pdb.set_trace()

    # pass_flag = True
    for cnm in cnm_list:
        tem_ple = df[df['cnm'] == cnm].to_dict(orient='records')[0]
        modify_temple_with_chatgpt(tem_ple)
    # import pdb;pdb.set_trace()
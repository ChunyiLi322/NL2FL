import re

import openai

def askChatGPT(messages,MODEL):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages = messages,
        temperature=0)
    return response['choices'][0]['message']['content']


def find_longest_n(strings, n):
  # 初始化一个空列表，用来存储最长的几个字符串
  longest = []
  # 遍历字符串列表
  for s in strings:
    # 如果最长列表还没有达到n个，直接将当前字符串加入
    if len(longest) < n:
      longest.append(s)
    # 否则，找出最长列表中最短的字符串
    else:
      shortest = min(longest, key=len)
      # 如果当前字符串比最短的字符串长，用当前字符串替换最短的字符串
      if len(s) > len(shortest):
        longest[longest.index(shortest)] = s
  # 返回最长列表
  return longest


def chatgptresponse(MODEL,api_key,text,flcheckbox,flpracheckbox):
    api_key = "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"
    print("----------------0---------------------------")
    openai.api_key = api_key
    path_to_file = "test"
    textconstruct = "Please answer the logical formula, the formulas are all wrapped in $ $, and explain the meaning of the formula."
    print("----------------1---------------------------")
    messages = [{"role": "system","content":"You are a mature professional scholar of formalization, mastering"+flcheckbox+"，and the knowledge of"+flpracheckbox+"."}]
    # text = "如果检测到遮挡，并且 auto_control_mode 正在运行，auto_control将被终止。"
    text1 = text + textconstruct
    d = {"role":"user","content":text1}
    messages.append(d)
    print("----------------2---------------------------")
    text_respon = askChatGPT(messages,MODEL)
    print("----------------3---------------------------")
    d = {"role":"assistant","content":text_respon}
    print('chatgpt：'+text1+'\n')
    messages.append(d)
    print("messages",messages)
    # log_record = open("log_"+ path_to_file +".txt", mode = "a+", encoding = "utf-8")
    # print(text_respon, file = log_record)



    # text = "Initially r22 or r33 or r44 or r55 or r66  or r11 is not available, and r66 is available."
    # text = text + textconstruct
    # d = {"role":"user","content":text}
    # messages.append(d)
    # print("----------------2---------------------------")
    # text_respon = askChatGPT(messages, MODEL)
    # print("----------------3---------------------------")
    # d = {"role":"assistant","content":text_respon}
    # print('chatgpt：'+text+'\n')
    # messages.append(d)
    # print("messages",messages)
    # log_record = open("log_"+ path_to_file +".txt", mode = "a+", encoding = "utf-8")
    # print("\n"+text_respon, file = log_record)
    # text_respon_two = text_respon.split('\n\n')
    # print (type(text_respon_two))
    # print(text_respon_two)

    text_len = re.findall(r'\n', text)
    len_value = len(text_len) + 1
    print("------------需要转化几个公式---------------",len_value)
    text_response = re.findall(r'\$([^\$]*)\$', text_respon)
    # fl = max(text_response, key=len)
    fl = find_longest_n(text_response, len_value)
    fl = '.\n'.join(fl)
    print("------------公式到前端---------------",fl)
    return fl, text_respon



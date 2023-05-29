import openai

def askChatGPT(messages,MODEL):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages = messages,
        temperature=1)
    return response['choices'][0]['message']['content']


def chatgptresponse(MODEL,api_key,text,flcheckbox,flpracheckbox):
    # api_key = "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"
    print("----------------0---------------------------")
    openai.api_key = api_key
    path_to_file = "test"
    textconstruct = "请将其以公式: 。解释: 。格式回复给我"
    print("----------------1---------------------------")
    messages = [{"role": "system","content":"你是一个成熟的形式化专业学者，掌握"+flcheckbox+"，以及"+flpracheckbox+"的知识。"}]
    # text = "如果检测到遮挡，并且 auto_control_mode 正在运行，auto_control将被终止。"
    text = text + textconstruct
    d = {"role":"user","content":text}
    messages.append(d)
    print("----------------2---------------------------")
    text_respon = askChatGPT(messages,MODEL)
    print("----------------3---------------------------")
    d = {"role":"assistant","content":text_respon}
    print('chatgpt：'+text+'\n')
    messages.append(d)
    print("messages",messages)
    log_record = open("log_"+ path_to_file +".txt", mode = "a+", encoding = "utf-8")
    print(text_respon, file = log_record)



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
    text_respon_two = text_respon.split('\n\n')
    print (type(text_respon_two))
    print(text_respon_two)
    return text_respon_two[0],text_respon_two[1]
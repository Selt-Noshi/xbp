import openai
import pyperclip
import os

# 環境変数からAPIキーを取得
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("APIキーが環境変数に設定されていません。")
else:
    openai.api_key = api_key

def gpt_request(prompt):
    # ChatGPT APIリクエスト関数
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']



def process_1():
    while True:
        print("1-翻訳、2-返信メールを選んでください。")
        choice = input("選択: ")
        
        if choice == "1":
            # 翻訳プロセス
            text_to_translate = input("翻訳したい内容を入力してください: ")
            result_1 = gpt_request(f"日本語に書き直してください：「{text_to_translate}」")
            
            print("1-である調、2-ですます調")
            tone_choice = input("選択: ")
            if tone_choice == "1":
                result_2 = gpt_request(f"「{result_1}」を である調に書き直してください。")
            elif tone_choice == "2":
                result_2 = gpt_request(f"「{result_1}」を ですます調に書き直してください。")
            
            while True:
                print("結果:", result_2)
                confirm = input("この翻訳でよろしいでしょうか？ Y/N: ")
                if confirm.upper() == "Y":
                    pyperclip.copy(result_2)
                    print("内容がコピーされました。")
                    return
                else:
                    result_2 = gpt_request(f"文法を直してください：「{result_2}」")

        elif choice == "2":
            # 返信メールプロセス
            email_content = input("返信内容を入力してください: ")
            result_1 = gpt_request(f"以下の内容を日本語のメールの方に書き直してください：「{email_content}」")
            
            while True:
                print("結果:", result_1)
                confirm = input("この翻訳でよろしいでしょうか？ Y/N: ")
                if confirm.upper() == "Y":
                    pyperclip.copy(result_1)
                    print("内容がコピーされました。")
                    return
                else:
                    rephrase_choice = input("1-やり直す、2-もっと丁寧に: ")
                    if rephrase_choice == "1":
                        result_1 = gpt_request(f"以下の内容をメールの方に書き直してください：「{email_content}」")
                    elif rephrase_choice == "2":
                        result_1 = gpt_request(f"もっと丁寧な日本語に書き直してください：「{email_content}」")

def process_2():
    while True:
        print("1-翻訳、2-返信メールを選んでください。")
        choice = input("選択: ")

        if choice == "1":
            text_to_translate = input("翻訳したい内容を入力してください: ")
            result_1 = gpt_request(f"Translate this text to English: 「{text_to_translate}」")
            while True:
                print("結果:", result_1)
                confirm = input("この翻訳でよろしいでしょうか？ Y/N: ")
                if confirm.upper() == "Y":
                    pyperclip.copy(result_1)
                    print("内容がコピーされました。")
                    return

        elif choice == "2":
            email_content = input("返信内容を入力してください: ")
            result_1 = gpt_request(f"I want to write an email in English with following information: 「{email_content}」")
            while True:
                print("結果:", result_1)
                confirm = input("この翻訳でよろしいでしょうか？ Y/N: ")
                if confirm.upper() == "Y":
                    pyperclip.copy(result_1)
                    print("内容がコピーされました。")
                    return

def process_3():
    while True:
        print("1-翻訳、2-返信メールを選んでください。")
        choice = input("選択: ")

        if choice == "1":
            text_to_translate = input("翻訳したい内容を入力してください: ")
            result_1 = gpt_request(f"翻译成中文: 「{text_to_translate}」")
            while True:
                print("結果:", result_1)
                confirm = input("この翻訳でよろしいでしょうか？ Y/N: ")
                if confirm.upper() == "Y":
                    pyperclip.copy(result_1)
                    print("内容がコピーされました。")
                    return

        elif choice == "2":
            email_content = input("返信内容を入力してください: ")
            result_1 = gpt_request(f"我想用以下内容写一封中文邮件: 「{email_content}」")
            while True:
                print("結果:", result_1)
                confirm = input("この翻訳でよろしいでしょうか？ Y/N: ")
                if confirm.upper() == "Y":
                    pyperclip.copy(result_1)
                    print("内容がコピーされました。")
                    return


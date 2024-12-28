import os
import shlex

def send_message(user, message):
    """
    通过 AppleScript 给指定 iMessage 用户发送消息。

    :param user: iMessage 的联系人或邮箱
    :param message: 要发送的消息内容
    """

    user_escaped = shlex.quote(user)
    message_escaped = shlex.quote(message)
    
    # AppleScript
    command = f"osascript -e 'tell application \"Messages\" to send {message_escaped} to buddy {user_escaped}'"
    
    # 执行命令
    exit_code = os.system(command)
    if exit_code == 0:
        print(f"Sent to {user}：{message}")
    else:
        print(f"Failed. Check user {user} ")

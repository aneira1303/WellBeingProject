def trim_messages(messages, max_messages=12):
    if len(messages) <= max_messages + 1:
        return messages
    return [messages[0]] + messages[-max_messages:]

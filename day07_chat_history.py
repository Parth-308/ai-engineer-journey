import json

chat_history = []


def add_message(role, content):
    chat_history.append({"role": role, "content": content})


add_message("system", "તમે એક મદદરૂપ AI mentor છો.")
add_message("user", "RAG શું છે?")
add_message("assistant", "RAG એટલે Retrieval-Augmented Generation.")
add_message("user", "એનું એક ઉદાહરણ આપો.")

print("કુલ messages:", len(chat_history))
print("છેલ્લો પ્રશ્ન:", chat_history[-1]["content"])

# Memory limit: system message + છેલ્લા 2 messages જ મોકલો
trimmed = [chat_history[0]] + chat_history[-2:]

# Unique roles શોધો (Set)
roles = set()
for message in chat_history:
    roles.add(message["role"])
print("Roles:", roles)

# LLM API ને મોકલાતી request (Dict)
request = {
    "model": "model-name",
    "messages": trimmed,
    "temperature": 0.7,
}

print(json.dumps(request, ensure_ascii=False, indent=2))
from core.services.mcp.parser import parse

examples = [
    "Напомни купить молоко",
    "Сделать отчёт по проекту",
    "Идея стартапа для заметки"
]

for text in examples:
    print(text)
    print(parse(text))
    print("-" * 40)

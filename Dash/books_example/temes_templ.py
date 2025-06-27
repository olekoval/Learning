import plotly.io as pio

# Отримати список доступних тем
available_themes = pio.templates

# Вивести назви всіх доступних тем
print("Доступні теми:")
for theme_name in available_themes:
    print(f"- {theme_name}")

# Якщо ви хочете побачити деталі конкретної теми (наприклад, 'plotly')
if 'plotly' in available_themes:
    print("\nДеталі теми 'plotly':")
    print(available_themes['plotly'])

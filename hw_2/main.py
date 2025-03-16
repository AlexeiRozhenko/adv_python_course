from latex_project_hw2.latex_generator import generate_latex_table, generate_latex_image

data = [
    ["ID", "Год", "Город"],
    [1, 25, "Сызрань"],
    [2, 30, "Ухта"],
    [3, 22, "Ухты"]
]

# # Генерируем LaTeX-код таблицы
latex_code = generate_latex_table(data)

# Сохраняем в .tex файл
with open("table_example.tex", "w", encoding="utf-8") as file:
    file.write(latex_code)

print("Файл table_example.tex успешно создан!")


# Генерируем PDF с картинкой
path = "random_pic.png"
latex_code = generate_latex_image(path)

# Сохраняем в .tex файл
with open("pic_example.tex", "w", encoding="utf-8") as file:
    file.write(latex_code)

print("Файл pic_example.tex успешно создан!")
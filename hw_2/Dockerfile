# Используем официальный Python-образ
FROM python:3.11-slim

# Устанавливаем необходимые пакеты (LaTeX + Python зависимости)
RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-lang-cyrillic \ 
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем проект внутрь контейнера
COPY . .

# Указываем команду, которая запустится при старте контейнера
CMD ["sh", "-c", "python /app/main.py && pdflatex -output-directory=/app /app/table_example.tex && pdflatex -output-directory=/app /app/pic_example.tex"]
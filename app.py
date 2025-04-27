from flask import Flask, render_template, request

app = Flask(__name__)

# Список моделей ноутбуков
laptops = [
    {
        "name": "ASUS VivoBook 15",
        "description": "Универсальный ноутбук с хорошей производительностью.",
    },
    {
        "name": "Lenovo IdeaPad 3",
        "description": "Надежный ноутбук для работы и учебы.",
    },
    {
        "name": "HP Pavilion 15",
        "description": "Стильный и мощный ноутбук для развлечений.",
    },
    {
        "name": "Acer Aspire 5",
        "description": "Отличный выбор для повседневных задач.",
    },
    {
        "name": "Dell Inspiron 15",
        "description": "Качественный ноутбук с хорошей сборкой.",
    },
]

@app.route('/')
def index():
    return render_template('index.html', laptops=laptops)

@app.route('/laptop/<int:laptop_id>')
def laptop(laptop_id):
    laptop = laptops[laptop_id]
    return render_template('laptop.html', laptop=laptop)

if __name__ == '__main__':
    app.run(debug=True)
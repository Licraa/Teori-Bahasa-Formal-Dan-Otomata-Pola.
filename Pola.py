from flask import Flask, render_template, request

app = Flask(__name__)

def search_pattern(text, pattern):
    """Search for the pattern in the given text."""
    position = text.find(pattern)
    if position == -1:
        return "Pola tidak ditemukan dalam teks."
    else:
        return f"Pola ditemukan pada posisi {position + 1} sampai {position + len(pattern)}."

def count_pattern(text, pattern):
    """Count occurrences of the pattern in the given text."""
    count = text.count(pattern)
    return f"Jumlah pola yang ditemukan: {count}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text = request.form['text']  # Memperbarui ini
    pattern = request.form['pattern']  # Memperbarui ini
    choice = request.form['choice']

    if choice == '1':
        result = search_pattern(text, pattern)
    elif choice == '2':
        result = count_pattern(text, pattern)
    else:
        result = "Pilihan tidak valid"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

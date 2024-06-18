from flask import Flask, render_template, request, send_file
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    url = request.form['url']
    img = qrcode.make(url)
    buffer = io.BytesIO()
    img.save(buffer, 'PNG')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.getvalue()).decode('ascii')
    img_data = f"data:image/png;base64,{img_str}"
    return render_template('index.html', img_data=img_data)

if __name__ == '__main__':
    app.run(debug=True)

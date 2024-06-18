# QR Code Generator

A simple QR code generator web application built with Flask, HTML, and CSS. This application allows users to input a URL and generate a QR code that links to the given URL.

## Features

- Generate QR codes for any URL
- Download the generated QR code as an image
- Simple and responsive web interface

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- qrcode (Python library)
- Pillow (Python Imaging Library)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/qr-code-generator.git
    cd qr-code-generator
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

## File Structure


- `static/`: Directory for static files (CSS, images, etc.)
- `templates/`: Directory for HTML templates
- `app.py`: Main Flask application
- `requirements.txt`: List of Python dependencies
- `README.md`: Project documentation
- `LICENSE`: License for the project

## Usage

1. Enter the URL you want to generate a QR code for.
2. Click the "Generate" button.
3. The QR code will be displayed on the screen.
4. Click the "Download" button to save the QR code as an image.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [qrcode](https://pypi.org/project/qrcode/) - The library used to generate QR codes
- [Pillow](https://pypi.org/project/Pillow/) - The Python Imaging Library

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

If you have any questions or suggestions, feel free to contact me at [your email address].

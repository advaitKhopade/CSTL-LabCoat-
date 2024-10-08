from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    file = request.files['file']
    file_path = './uploads/' + file.filename
    file.save(file_path)

    # Call the Python script to process the resume
    output = subprocess.check_output(['python', 'matchMakingAlgorithm1.py', file_path])

    # Extract the skills from the output
    skills = [line.strip() for line in output.decode('utf-8').splitlines()]

    return jsonify({'skills': skills})

if __name__ == '__main__':
    app.run(debug=True)
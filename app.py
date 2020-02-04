import json
import pprint
from flask import Flask, request, render_template

from formatter import format_data

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	template_data = {}

	if request.method == 'POST':
		input = request.form['input']
		template_data['input'] = input

		try:
			data = json.loads(input)
			template_data['output'] = format_data(data)
		except Exception as e:
			template_data['output'] = str(e)
		

	return render_template('index.html', **template_data)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)

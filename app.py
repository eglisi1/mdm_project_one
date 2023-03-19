from flask import Flask, request, render_template
import service.logger as logger

app = Flask(__name__)
log = logger.Logger()

# init model
from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(17)


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    text_input = ''
    predictions = []
    log.debug(f'request.method: {request.method}')
    if request.method == 'POST':
        text_input = request.form['text_input']
        predictions = predict(text_input)
    return render_template(template_name_or_list='index.html', input=text_input, predictions=predictions)


def predict(input: str) -> list[str] :
    log.debug(f'input: {input}')
    output = generator(input, max_length=30, num_return_sequences=5)
    output = [o['generated_text'] for o in output]
    log.debug('output:')
    for o in output:
        log.debug(f"  {o}")
    return output

if __name__ == '__main__':
    log.info('Starting Flask app')
    app.run()

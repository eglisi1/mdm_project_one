from transformers import pipeline, set_seed
from flask import Flask, request, render_template
import service.logger as logger

app = Flask(__name__)
log = logger.Logger()

# init model
generator = pipeline('text-generation', model='gpt2')
set_seed(17)

chat_history = list(tuple())


@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    question = ''
    log.debug(f'request.method: {request.method}')
    if request.method == 'POST':
        question = request.form['question']
        predict(question)
    else:
        chat_history.clear()
    return render_template(template_name_or_list='index.html', chat=chat_history)


def predict(question: str) -> None:
    log.debug(f'question: {question}')
    prediction = generator(question, max_length=500, num_return_sequences=1)
    output = prediction[0]['generated_text']
    # remove rest after last '.' (sentence)
    output = output[:output.rfind('.') + 1]
    log.debug(f'output: {output}')
    chat_history.append((question, output))


if __name__ == '__main__':
    log.info('Starting Flask app')
    app.run()

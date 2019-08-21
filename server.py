from flask import Flask, render_template, request
import data_manager
import util

app = Flask(__name__)


@app.route('/')
def index():
    questions = data_manager.get_list_all_records('question')
    for question in questions:
        question['submission_time'] = util.time_convert(question['submission_time'])
    return render_template('index.html', questions=questions)


@app.route('/question', defaults={'question_id': None})
@app.route('/question/<int:question_id>')
def question(question_id):
    question = data_manager.get_single_question_by_id(question_id)

    return render_template('qs_answers_list.html', question=question)


@app.route('/ask-question')
def ask_question():
    return render_template('ask-question.html')


@app.route('/get_form_which_question', methods=['GET', 'POST'])
def get_form():
    try:
        if request.method == 'POST':
            form_question = dict(request.form)
        else:
            raise ValueError
    except ValueError('Check form which question, non POST method?') as err:
        return err
    else:
        id_new_question = data_manager.add_new_question_to_base(form_question['title'], form_question['question'])
        print(id_new_question)
        return question(id_new_question)



if __name__ == '__main__':
    app.run(port=8000,
            debug=True)

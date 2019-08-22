from flask import Flask, render_template, request, redirect, url_for
import data_manager
import util

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def index():
    questions = data_manager.get_list_all_records('question')
    for question in questions:
        question['submission_time'] = util.time_convert(question['submission_time'])
    return render_template('index.html', questions=questions)


@app.route('/question', defaults={'question_id': None})
@app.route('/question/<int:question_id>')
def question(question_id):
    data_manager.increment_value(which_base='question', question_id=question_id, which_value='view_number')
    question = data_manager.get_single_question_by_id(question_id)
    question['submission_time'] = util.time_convert(question['submission_time'])

    answers = data_manager.get_all_answers_by_id(question_id)
    for answer in answers:
        answer['submission_time'] = util.time_convert(answer['submission_time'])
    # add +1 to visits;
    return render_template('qs_answers_list.html', question=question, answers=answers)


# / - - - post an answer - - - - -
@app.route('/question/<int:question_id>/new-answer')
def new_answer(question_id):
    question = data_manager.get_single_question_by_id(question_id)
    return render_template('answer.html', question=question)

#

@app.route('/answer_form', methods=['GET', 'POST'])
def get_answer():
    if request.method == 'POST':
        form = {'id':'q_id', 'answer':'answer'}
        insert_into = True
        if 'q_id' in request.form:
            form['id'] = request.form['q_id']
        else: insert_into = False
        if 'answer' in request.form:
            form['answer'] = request.form['answer']
        else: insert_into = False

        if insert_into:
            data_manager.add_new_answer_to_base(form['id'], form['answer'], image='None')

            return redirect(url_for('question', question_id=form['id']) )
        else:
            redirect(url_for('new_answer', question_id = form['id']))

    return redirect('/list')
#
#/ - - - - - - - - - - - - - - - -

#/ - - - - - - -Votes- - - - - - -
@app.route('/question/<int:question_id>/vote-up')
def vote_up_question(question_id):
    data_manager.increment_value('question', question_id, False, 'vote_number')
    return redirect(url_for('question', question_id=question_id))
#
@app.route('/question/<int:question_id>/vote-dowm')
def vote_down_question(question_id):
    data_manager.increment_value('question', question_id, False, 'vote_number', 'down')
    return redirect(url_for('question', question_id=question_id))
#

@app.route('/answer/<int:answer_id>/vote-up')
def vote_up_answer(answer_id):
    answer = data_manager.get_single_answer_by_id(answer_id)
    question_id = answer['question_id']

    data_manager.increment_value('answer', question_id, answer_id, 'vote_number')
    return redirect(url_for('question', question_id=question_id))
#
@app.route('/answer/<int:answer_id>/vote-dowm')
def vote_down_answer(answer_id):
    answer = data_manager.get_single_answer_by_id(answer_id)
    question_id = answer['question_id']

    data_manager.increment_value('answer', question_id, answer_id, 'vote_number', 'down')
    return redirect(url_for('question', question_id=question_id))

#/ - - - - - - - - - - - - - - - -


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
        return redirect(url_for('question', question_id=id_new_question))

@app.route('/question/<int:question_id>/delete')
def delete_question(question_id):
    return ""
#

@app.route('/question/<int:question_id>/edit')
def edit_question(question_id):
    question = data_manager.get_single_question_by_id(question_id)

    return render_template('ask-question.html', question = question)
#

if __name__ == '__main__':
    app.run(port=8000,
            debug=True)

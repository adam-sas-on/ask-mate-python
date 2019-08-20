from flask import Flask, render_template, request, url_for
import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    questions=data_manager.get_list_all_records('question')
    return render_template('index.html', questions=questions)


@app.route('/ask-question')
def ask_question():
    return render_template('ask-question.html')


@app.route('/get_form_which_question', methods=['GET', 'POST'])
def get_form():
    try:
        if request.method == 'POST':
            form_question = dict(request.form)
            print(form_question)
        else:
            raise ValueError
    except ValueError('Check form which question, non POST method?') as err:
        return err
    else:
        data_manager.add_new_question_to_base(form_question['title'], form_question['question'])
        return render_template('ask-question.html') # todo Change target to question details !!!!!




if __name__ == '__main__':
    app.run(port=8000,
            debug=True)

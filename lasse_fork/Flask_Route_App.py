''' Vi importer med vilje ikke  all (*), da det er grimt imo'''
from flask import Flask, render_template, request, jsonify
import Questions as Q
import Map as M

app = Flask(__name__)


def initialize():
    return app


def run_program():
    return app.run(debug=True, port=3050)

""" ##################### Initilize Local ####################### """

initialize()


""" ##################### Setup Routes ####################### """

@app.route('/')
def generate_index():

    return render_template('index.html',
     ip="127.0.0.1")


@app.route("/ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route("/map")
def map():
    result = M.execMap()
    desc = "This is a Interactive map showing the prices of 1kg bananas across the world in DKK currency"
    return render_template('chartPage.html',data=result, desc=desc)

@app.route("/faq")
def faq():
    routes = Q.getQuestions()
    return render_template('questions.html',data=routes)

""" ################ Setup Question Routes ################# """

""" ###################### Text Routes ################# """

@app.route("/1")
def question1():
    result = Q.execQ1()
    desc = Q.getQuestions().get(1)
    return render_template('textPage.html',data=result, desc=desc[0])

@app.route("/2")
def question2():
    result = Q.execQ2()
    desc = Q.getQuestions().get(2)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])

@app.route("/3")
def question3():
    result = Q.execQ3()
    desc = Q.getQuestions().get(3)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])

@app.route("/4")
def question4():
    result = Q.execQ4()
    desc = Q.getQuestions().get(4)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])

@app.route("/5")
def question5():
    result = Q.execQ5()
    desc = Q.getQuestions().get(5)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])

@app.route("/6")
def question6():
    result = Q.execQ6()
    desc = Q.getQuestions().get(6)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])

@app.route("/7")
def question7():
    result = Q.execQ7()
    desc = Q.getQuestions().get(7)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])

@app.route("/8")
def question8():
    result = Q.execQ8()
    desc = Q.getQuestions().get(8)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])

@app.route("/9")
def question9():
    result = Q.execQ9()
    desc = Q.getQuestions().get(9)
    return render_template('textPage.html',data=round(result,3), desc=desc[0])

@app.route("/10")
def question10():
    result = Q.execQ10()
    desc = Q.getQuestions().get(10)
    return render_template('textPage.html',data=round(result,3), desc=desc[0])

@app.route("/11")
def question11():
    result = Q.execQ11()
    desc = Q.getQuestions().get(11)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])

@app.route("/12")
def question12():
    result = Q.execQ12()
    desc = Q.getQuestions().get(12)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])

@app.route("/13")
def question13():
    result = Q.execQ13()
    desc = Q.getQuestions().get(13)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])

@app.route("/14")
def question14():
    result = Q.execQ14()
    desc = Q.getQuestions().get(14)
    return render_template('textPage.html',data=result[:10].to_html(), desc=desc[0])

@app.route("/15")
def question15():
    result = Q.execQ15()
    desc = Q.getQuestions().get(15)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])

@app.route("/16")
def question16():
    result = Q.execQ16()
    desc = Q.getQuestions().get(16)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])

@app.route("/17")
def question17():
    result = Q.execQ17()
    desc = Q.getQuestions().get(17)
    return render_template('textPage.html',data=result.to_html(), desc=desc[0])


""" ###################### Chart Routes ################# """

@app.route("/18")
def question18():
    result = Q.execQ18()
    desc = "This is a interactive chart over the price of Apple, Bananas & Oranges through the years"
    return render_template('chartPage.html',data=result, desc=desc)

@app.route("/19")
def question19():
    result = Q.execQ19()
    desc = "This is a interactive chart over the price of fruit in 2017 in %"
    return render_template('chartPage.html',data=result, desc=desc)


""" ##################### Start Local shit ####################### """

run_program()

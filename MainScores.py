# MainScores.py

from Score import current_score
from flask import Flask, render_template


# Function create score web page
def create_score_page():
    template_page_fh = open("templates/score.html", "w")
    template_page_fh.write('<html>\n<head>\n<title>Scores Game</title>\n</head>\n<body>\n<h1>The score is <div '
                           'id="score">%d</div></h1>\n</body>\n</html>\n' % current_score())
    template_page_fh.close()


# Function create error web page
def create_error_page():
    template_page_fh = open("templates/error.html", "w")
    template_page_fh.write('<html>\n<head>\n<title>Scores Game</title>\n</head>\n<body>\n<h1><div id="score" '
                           'style="color:red">{ERROR}</div></h1>\n</body>\n</html>')
    template_page_fh.close()


# Function serve the score
def score_server():
    app = Flask(__name__)

    @app.route("/")
    def score_page():
        create_score_page()
        return render_template("score.html")

    app.run()

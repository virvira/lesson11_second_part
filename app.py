import os
from utils import load_candidates, get_candidate, get_candidates_by_name, get_by_skill
from flask import Flask, render_template

candidates_file = os.path.join('data', 'candidates.json')

app = Flask(__name__)

candidates_list = load_candidates(candidates_file)


@app.route("/")
def show_main():
    return render_template('list.html', candidates_list=candidates_list)


@app.route("/candidate/<int:x>")
def show_candidate(x):
    candidate = get_candidate(x, candidates_list)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def show_candidates_with_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name, candidates_list)
    candidates_count = len(candidates)
    return render_template('search.html', candidates=candidates, candidate_name=candidate_name,
                           candidates_count=candidates_count)


@app.route("/skill/<skill_name>")
def show_candidates_with_skill(skill_name):
    candidates = get_by_skill(skill_name, candidates_list)
    candidates_count = len(candidates)
    return render_template('skill.html', candidates=candidates, skill_name=skill_name,
                           candidates_count=candidates_count)


app.run(port=5001)

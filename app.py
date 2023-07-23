"""Madlibs Stories."""
from flask import Flask, request, render_template


app = Flask(__name__)


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
story2 = Story(
   ["place", "noun", "verb", "adjective", "plural_noun"],
    """This weekend I am going camping with {plural_noun}. I packed my lantern, sleeping bag, and
        {noun}. I am so {adjective} to {verb} in a tent. I am {adjective} we
        might see a {place}, they are kind of dangerous.""" 
)

@app.route("/home")
def home_page():
    return render_template("form.html")

@app.route("/story")
def story_page():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]

    ans = {"place":place, "noun":noun, "verb":verb, "adjective":adjective, "plural_noun":plural_noun}

    madlibs_story = story.generate(ans)

    return render_template("story.html", place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun, madlibs_story=madlibs_story)
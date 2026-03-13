from flask import Flask

app = Flask(__name__)

# 1. 첫 번째 페이지: 홈 (Introduction)
@app.route("/")
@app.route("/home")
def index():
    return """
    <h1>KNU Open Source Programming - Sanghyeon's Blog</h1>
    <p>Welcome to my development journal!</p>
    <nav>
        <a href='/profile'>[Go to My Profile]</a> | 
        <a href='/tech'>[Go to Tech Notes]</a>
    </nav>
    """

# 2. 두 번째 페이지: 프로필 (Transition 1)
@app.route("/profile")
def profile():
    return """
    <h1>Sanghyeon's Profile</h1>
    <ul>
        <li>Name: Sanghyeon (KNU Student)</li>
        <li>Major Interest: Quantum Machine Learning (QML)</li>
    </ul>
    <a href='/'>[Back to Home]</a>
    """

# 3. 세 번째 페이지: 기술 노트 (Transition 2)
@app.route("/tech")
def tech():
    return """
    <h1>Git & OSS Technology</h1>
    <p>Git is a Distributed Version Control System (DVCS).</p>
    <p>Every developer has a full copy of the repository[cite: 120].</p>
    <a href='/'>[Back to Home]</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
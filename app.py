from flask import Flask, request

app = Flask(__name__)

# [개선] 데이터 관리를 위한 클래스 추출 (Primitive Obsession 해결)
class UserProfile:
    def __init__(self):
        self.interest = "QML"
        self.bio = "KNU undergraduate student"

    def add_interest(self, val):
        if val:
            self.interest += f", {val}"

    def add_bio(self, val):
        if val:
            self.bio += f", {val}"

profile_data = UserProfile()
study_list = ["Opensource programming"]

@app.route("/")
def index():
    return "<h1>Sanghyeon's Dev Log</h1><nav><a href='/profile'>Profile</a> | <a href='/study'>Study</a></nav>"

# [개선] 로직 분리 (Divergent Change 해결)
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        handle_profile_update()
    return render_profile_page()

def handle_profile_update():
    action = request.form.get('action')
    if action == 'update_interest':
        profile_data.add_interest(request.form.get('interest'))
    elif action == 'update_bio':
        profile_data.add_bio(request.form.get('bio'))

def render_profile_page():
    return f"""
    <h1>My Profile</h1>
    <p><strong>Interests:</strong> {profile_data.interest}</p>
    <p><strong>Bio:</strong> {profile_data.bio}</p>
    <hr>
    <form method="POST"><input type="hidden" name="action" value="update_interest">
        Add Interest: <input type="text" name="interest"><input type="submit" value="Add"></form>
    <form method="POST"><input type="hidden" name="action" value="update_bio">
        Add Bio: <input type="text" name="bio"><input type="submit" value="Add"></form>
    <br><a href='/'>[Back to Home]</a>
    """

@app.route("/study", methods=['GET', 'POST'])
def study():
    if request.method == 'POST':
        subject = request.form.get('subject')
        if subject:
            study_list.append(subject)
    return render_study_page()

def render_study_page():
    # [개선] UI 요소(뒤로가기 버튼 등)를 명확히 포함하여 외부 동작 유지
    subjects_html = "".join([f"<li>{s}</li>" for s in study_list])
    return f"""
    <h1>Study Room</h1>
    <ul>{subjects_html}</ul>
    <form method="POST">
        Subject: <input type="text" name="subject">
        <input type="submit" value="Add Subject">
    </form>
    <br><a href='/'>[Back to Home]</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
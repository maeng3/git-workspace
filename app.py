from flask import Flask, request

app = Flask(__name__)

# 데이터 저장 공간
user_profile = {"interest": "QML", "bio": "KNU undergraduate student"}
study_list = [] # 과목 이름을 담을 리스트

@app.route("/")
def index():
    # Current User 표시 제거
    return "<h1>Sanghyeon's Dev Log</h1><nav><a href='/profile'>Profile</a> | <a href='/study'>Study</a></nav>"


@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'update_interest':
            new_val = request.form.get('interest')
            if new_val:
                # 기존 데이터가 있으면 쉼표로 구분하여 추가
                if user_profile['interest']:
                    user_profile['interest'] += f", {new_val}"
                else:
                    user_profile['interest'] = new_val
                
        elif action == 'update_bio':
            new_val = request.form.get('bio')
            if new_val:
                if user_profile['bio']:
                    user_profile['bio'] += f", {new_val}"
                else:
                    user_profile['bio'] = new_val
    
    return f"""
    <h1>My Profile</h1>
    <p><strong>Interests:</strong> {user_profile['interest']}</p>
    <p><strong>Bio:</strong> {user_profile['bio']}</p>
    <hr>
    <form method="POST">
        <input type="hidden" name="action" value="update_interest">
        Add Interest: <input type="text" name="interest">
        <input type="submit" value="Add">
    </form>
    <form method="POST">
        <input type="hidden" name="action" value="update_bio">
        Add Bio: <input type="text" name="bio">
        <input type="submit" value="Add">
    </form>
    <br><a href='/'>[Back to Home]</a>
    """

@app.route("/study", methods=['GET', 'POST'])
def study():
    if request.method == 'POST':
        subject = request.form.get('subject')
        if subject: study_list.append(subject) # 과목 추가
    
    # 추가된 과목들을 리스트로 출력
    subjects_html = "".join([f"<li>{s}</li>" for s in study_list])
    return f"""
    <h1>Study Room</h1>
    <ul>{subjects_html}</ul>
    <form method="POST">
        Subject: <input type="text" name="subject">
        <input type="submit" value="Add Subject">
    </form>
    <a href='/'>Back</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
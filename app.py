from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

class UserProfile:
    """사용자의 프로필 정보를 관리하는 클래스입니다. 

    Attributes:
        interest (str): 사용자의 관심 분야 목록입니다. [cite: 78, 79]
        bio (str): 사용자의 자기소개 정보입니다. [cite: 78, 79]
    """
    def __init__(self):
        """기본 프로필 정보를 초기화합니다."""
        self.interest = "QML"
        self.bio = "KNU undergraduate student"

    def add_interest(self, val: str):
        """기본 관심 분야에 새로운 항목을 추가합니다. [cite: 90]

        Args:
            val (str): 추가할 새로운 관심 분야 문자열입니다. [cite: 92, 93]
        """
        if val:
            self.interest += f", {val}"

    def add_bio(self, val: str):
        """기본 자기소개에 새로운 내용을 덧붙입니다.

        Args:
            val (str): 추가할 자기소개 내용입니다.
        """
        if val:
            self.bio += f", {val}"

profile_data = UserProfile()
study_list = ["Opensource programming"]

@app.route("/")
def index():
    """메인 페이지를 렌더링합니다. 

    Returns:
        str: 홈 화면 HTML 코드입니다. [cite: 95, 97]
    """
    return "<h1>Sanghyeon's Dev Log</h1><nav><a href='/profile'>Profile</a> | <a href='/study'>Study</a></nav>"

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    """프로필 정보를 조회하거나 업데이트하는 엔드포인트입니다.

    .. code-block:: yaml

        ---
        
        tags:
          - Profile API
        parameters:
          - name: action
            in: formData
            type: string
            enum: [update_interest, update_bio]
            description: 업데이트할 항목의 종류입니다.
          - name: interest
            in: formData
            type: string
            description: 추가할 관심 분야입니다.
          - name: bio
            in: formData
            type: string
            description: 추가할 자기소개 내용입니다.
        responses:
          200:
            description: 프로필 페이지가 성공적으로 렌더링되었습니다.
    """
    if request.method == 'POST':
        handle_profile_update()
    return render_profile_page()

def handle_profile_update():
    """POST 요청으로부터 전달받은 데이터를 처리하여 프로필 객체를 업데이트합니다. """
    action = request.form.get('action')
    if action == 'update_interest':
        profile_data.add_interest(request.form.get('interest'))
    elif action == 'update_bio':
        profile_data.add_bio(request.form.get('bio'))

def render_profile_page():
    """프로필 정보와 수정 폼을 포함한 HTML을 생성합니다. [cite: 70]"""
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
    """학습 목록을 관리하고 조회하는 엔드포인트입니다.

    .. code-block:: yaml

        ---

        tags:
          - Study API
        parameters:
          - name: subject
            in: formData
            type: string
            description: 목록에 추가할 학습 과목명입니다.
        responses:
          200:
            description: 학습 목록 페이지가 성공적으로 로드되었습니다.
    """
    if request.method == 'POST':
        subject = request.form.get('subject')
        if subject:
            study_list.append(subject)
    return render_study_page()

def render_study_page():
    """현재 학습 중인 과목 목록과 입력 폼이 담긴 HTML을 생성합니다."""
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
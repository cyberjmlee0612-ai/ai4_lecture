from pathlib import Path
from html import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Preformatted
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
from pypdf import PdfReader

OUT=Path(r'C:\ai4_이정민\output\pcce')
pdfmetrics.registerFont(TTFont('Malgun',r'C:\Windows\Fonts\malgun.ttf'))
pdfmetrics.registerFont(TTFont('MalgunBold',r'C:\Windows\Fonts\malgunbd.ttf'))
pdfmetrics.registerFontFamily('Malgun',normal='Malgun',bold='MalgunBold',italic='Malgun',boldItalic='MalgunBold')
S={
'title':ParagraphStyle('title',fontName='MalgunBold',fontSize=24,leading=34,spaceAfter=17,wordWrap='CJK'),
'h':ParagraphStyle('h',fontName='MalgunBold',fontSize=16,leading=23,spaceBefore=8,spaceAfter=10,wordWrap='CJK'),
'sub':ParagraphStyle('sub',fontName='MalgunBold',fontSize=11.5,leading=18,spaceBefore=9,spaceAfter=6,wordWrap='CJK'),
'body':ParagraphStyle('body',fontName='Malgun',fontSize=10,leading=16,spaceAfter=7,wordWrap='CJK'),
'small':ParagraphStyle('small',fontName='Malgun',fontSize=8.8,leading=13.5,spaceAfter=5,wordWrap='CJK'),
'cell':ParagraphStyle('cell',fontName='Malgun',fontSize=9,leading=14,wordWrap='CJK'),
'code':ParagraphStyle('code',fontName='Malgun',fontSize=9,leading=13,spaceAfter=8),
}
story=[]; web=[]
def p(t,kind='body'):
    story.append(Paragraph(t,S[kind])); tag={'title':'h1','h':'h2','sub':'h3'}.get(kind,'p'); web.append(f'<{tag}>{t}</{tag}>')
def page(title):
    if story: story.append(PageBreak()); web.append('</section>')
    web.append('<section>'); p(title,'h')
def table(headers,rows,widths):
    data=[[Paragraph(escape(str(x)),S['cell']) for x in row] for row in [headers]+rows]
    t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8edf3')),('GRID',(0,0),(-1,-1),.5,colors.HexColor('#d9d9d9')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
    story.extend([t,Spacer(1,9)])
    web.append('<table><thead><tr>'+''.join('<th>'+escape(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+escape(str(x))+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>')
def code(t):
    story.append(Preformatted(t,S['code']));web.append('<pre>'+escape(t)+'</pre>')
def link(label,url):
    p(f'<a href="{escape(url,quote=True)}" color="#174b7a">{escape(label)}</a>','small')

web.append('<section>')
p('PCCE Python 600점 준비 계획','title')
p('2026년 10월 23일 금요일부터 10월 28일 수요일까지','sub')
p('학원은 평일 18시에 끝나고, 코딩은 처음 시작하는 사람을 위한 단기 실행 계획입니다. 목표는 PCCE Python 600점 이상인 Lv.2입니다. 오늘부터 시험 전날까지 순수 공부 17시간을 확보하고, 문법과 코드 읽기부터 코드 작성까지 단계적으로 연습합니다.')
p('계획의 전제','sub')
p('귀가와 저녁 식사에 90분을 두어 평일 19시 30분에 시작합니다. 주말에는 하루 5시간을 여러 구간으로 나눕니다. 주말 약속과 시험 시작 시간·장소는 확인되지 않았으므로 조정할 수 있게 구성했습니다. 시험 날짜는 사용자가 말한 다음 주 수요일인 10월 28일로 해석했으며, 해당 회차의 실제 접수 내역을 조회한 것은 아닙니다.')
table(['확인한 시험 정보','내용'],[
('시험 구성','50분 동안 총 10문항, 1,000점 만점 [1]'),
('문제 유형','빈칸 채우기, 디버깅, 코드 작성 [1]'),
('인증 점수','Lv.1 400~599 / Lv.2 600~749 / Lv.3 750~899 / Lv.4 900~1,000 [1]'),
('목표의 의미','400점 인증을 넘어서 600점 이상 목표. 학원 수료 기준이 별도라면 그 기준도 확인'),
('이번 계획의 한계','문항별 배점·부분점수 기준은 확인하지 못함. 정답 개수를 실제 점수로 환산하지 않음'),
],[115,390])
p('600점을 위해 무엇에 시간을 쓸까','sub')
p('먼저 자료형·조건문·반복문·리스트·함수 반환을 익힙니다. 이어서 기존 코드의 흐름을 추적하고 한 줄의 오류를 고치는 연습을 합니다. 주말에는 간단한 시뮬레이션과 2차원 리스트를 써서 코드 작성 문제도 풉니다. 복잡한 그래프 탐색·동적 계획법·클래스 심화는 이번 5일의 우선순위에서 뺍니다. 이는 단기 학습을 위한 권장 전략이며 출제 범위 제외를 뜻하지 않습니다.')
p('연습에서 기본 문제 8개 중 7개를 설명하며 풀고 코드 작성 1개를 스스로 완성하는 것을 중간 목표로 삼습니다. 이 기준은 학습 점검용이며 600점을 보장하는 환산표가 아닙니다. 노베이스에서 5일은 짧으므로 합격 확률을 수치로 약속할 근거도 없습니다.','small')
p('자료 확인일 2026년 10월 23일 · 출처와 확인 범위는 마지막 쪽 · 문제 링크는 4쪽','small')

page('날짜별 실행 일정 금요일과 토요일')
p('평일 공통 준비','sub')
p('18:00~19:30 이동·저녁·휴식. 준비가 일찍 끝나도 긴 강의를 추가하기보다 책상과 문제 링크를 준비합니다. 각 구간에는 아래 과제를 실제로 타이핑하고 실행합니다. 학습량은 풀이 속도에 따라 조절하고, 못 끝낸 문제는 다음 날 복습 시간에 우선 배치합니다.')
p('10월 23일 금요일 기초를 실제로 실행하기','sub')
table(['시간','할 일과 완료 기준'],[
('19:30~20:10','프로그래머스 로그인·Python3 선택. 출력·변수·int와 str·사칙연산 학습. 기초 출력 문제 1개 실행'),
('20:10~20:20','휴식'),
('20:20~21:10','if/elif/else, 비교, and/or, for와 range. 짧은 코드 결과를 먼저 예상하고 실행 6회'),
('21:10~21:20','휴식'),
('21:20~22:20','기출 A 1~3번 시도. 모르는 부분만 해설 확인. 마지막 15분에 답을 가리고 1문제 재풀이'),
],[108,397])
p('금요일 종료 기준: 문자열과 숫자 차이를 설명하고, 1부터 5까지 반복하며 짝수 개수를 세는 코드를 직접 쓸 수 있으면 됩니다. 막히면 7쪽 자체 연습 1·2번부터 하세요. 순수 학습 150분.')
p('10월 24일 토요일 리스트와 디버깅','sub')
table(['시간','할 일과 완료 기준'],[
('10:00~10:50','금요일 오답 20분. 리스트 인덱스·len·append·슬라이싱 30분'),
('11:00~11:50','for/while와 누적·개수 세기. 자체 연습 2·3번. 반복마다 값이 어떻게 변하는지 기록'),
('14:00~14:50','기출 A 4~5번. 조건·반복 범위·자료형을 말로 설명'),
('15:00~15:50','기출 A 6~8번. 각 문제 최대 12분 시도하고 남은 시간에 오답 분석'),
('19:00~19:50','def solution과 return, 매개변수 학습. 출력형과 함수형 구분. 자체 연습 4번'),
('20:00~20:50','A에서 틀린 문제 3개 답 없이 다시 풀기. 온라인 응시면 사전 테스트 20분 확보'),
],[108,397])
p('토요일 종료 기준: 리스트를 끝까지 순회하며 조건에 맞는 원소를 세고, 함수에서 결과를 return할 수 있습니다. 마지막 문제의 진도가 늦으면 새 문제를 줄이고 이 기준을 먼저 채웁니다. 순수 학습 300분.')
p('식사와 오후 휴식은 표 사이의 빈 시간에 충분히 둡니다. 매 구간 사이 최소 10분은 화면에서 눈을 떼세요. 수면을 줄여 밀린 분량을 만회하지 않습니다.','small')

page('날짜별 실행 일정 일요일부터 시험일까지')
p('10월 25일 일요일 코드 작성까지 확장하기','sub')
table(['시간','할 일과 완료 기준'],[
('10:00~10:50','A 1~8번 중 약한 4개 재풀이. 오답 원인을 문법·조건·반복·자료형으로 분류'),
('11:00~11:50','2차원 리스트의 행·열과 범위 확인. 작은 표를 손으로 그리고 이웃한 칸 원리 이해'),
('14:00~14:50','A 9번 코드 작성. 처음 20분 혼자 시도 후 필요한 힌트만 확인'),
('15:00~15:50','A 10번 필터링·정렬. 어렵다면 조건에 맞는 행만 고르는 부분까지 직접 구현'),
('19:00~19:50','9번을 빈 편집기에서 재구현. 최소 입력·가장자리 등 예외 테스트 3개'),
('20:00~20:50','10번 재풀이 또는 A 1~8번 약점 보완. 7쪽 자체 연습의 수치를 바꿔 다시 풀기'),
],[108,397])
p('순수 학습 300분. 월요일에 쓸 B 1~10번은 열어 보지 않고 남겨 둡니다. 미리 본 문제라면 결과를 실력 측정으로 해석하지 마세요.','small')
p('10월 26일 월요일 처음 보는 세트로 50분 연습','sub')
p('19:30~20:20 B 10문항을 50분 타이머로 풉니다. 메모·검색·AI·해설은 보지 않습니다. 20:20~20:30 휴식. 20:30~21:20 오답을 확인하고 틀린 이유를 적습니다. 21:20~21:30 휴식. 21:30~22:20 틀린 문제 중 기본 유형 2개와 코드 작성 1개를 답 없이 다시 풉니다. 순수 학습 150분.')
p('10월 27일 화요일 약점을 고치고 일찍 끝내기','sub')
p('19:30~20:20 A 전체 또는 A·B 오답 10개를 50분 안에 재풀이합니다. 이미 본 문제이므로 새로운 모의고사 점수로 취급하지 않습니다. 20:20~20:30 휴식. 20:30~21:10 가장 잦은 실수 3개를 고치고 코드 작성 1개 재현. 21:10~21:20 휴식. 21:20~21:50 사전 테스트 완료 여부·접수 내역·준비물 점검 후 종료합니다. 순수 학습 120분.')
p('10월 28일 수요일 시험 시작 시각 T를 기준으로','sub')
p('복습은 시험 전에 여유가 있을 때 20~30분만 합니다. 새 문제나 새 문법은 시작하지 않습니다. 온라인 일반 안내 기준으로 T-60분에 입실을 시작하고 T-40분까지 연결·신분 확인 완료를 목표로 합니다. 입실 허용은 T-60분부터 T-20분까지이므로 마감 직전 접속을 피하세요. 현장 단체시험이라면 주최 기관의 장소·집합 안내를 따릅니다. [6][7]')
p('총 17시간 = 금 2시간 30분 + 토 5시간 + 일 5시간 + 월 2시간 30분 + 화 2시간. 휴식·이동·식사와 시험 당일 복습은 제외했습니다. 시험이 18시 이전이거나 이동이 필요하면 학원 일정 조정을 미리 요청하세요.','small')

page('무료 학습 자료와 바로 풀 문제')
p('A는 학습용 공개 기출 10문항, B는 월요일 시간 연습용으로 구분했습니다. 이는 문서 안의 편의상 이름이며 공식 회차 명칭이 아닙니다. 링크를 연 뒤 언어를 Python3로 선택하세요. 로그인이나 무료 수강 시작이 필요할 수 있습니다.')
link('A 공식 PCCE 기출문제 10문항 무료 코스','https://school.programmers.co.kr/learn/courses/19274/19274-pcce-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-1%ED%9A%8C')
link('A 1번 변수와 자료형부터 시작','https://school.programmers.co.kr/learn/courses/19274/lessons/240596?language=python3')
link('A 9번 이웃한 칸 코드 작성 원문','https://school.programmers.co.kr/learn/courses/30/lessons/250125?language=python3')
link('A 10번 데이터 분석 코드 작성 원문','https://school.programmers.co.kr/learn/courses/30/lessons/250121?language=python3')
p('B는 월요일 19시 30분에 열기','sub')
for n,name,id in [(1,'문자 출력',340207),(2,'각도 합치기',340206),(3,'수 나누기',340205),(4,'병과분류',340204),(5,'심폐소생술',340203),(6,'물 부족',340202),(7,'버스',340201),(8,'닉네임 규칙',340200),(9,'지폐 접기',340199),(10,'공원',340198)]:
    link(f'B {n}번 {name}',f'https://school.programmers.co.kr/learn/courses/30/lessons/{id}?language=python3')
p('문법 보충은 필요한 부분만','sub')
link('기초 출력 연습 문자열 출력하기','https://school.programmers.co.kr/learn/courses/30/lessons/181952?language=python3')
link('공식 기초 문제 목록 조건문과 반복문 등 약점만 선택','https://school.programmers.co.kr/learn/challenges?languages=python3&levels=0&order=recent&page=1')
p('기초 문제 전체 완주나 긴 강의 정주행은 이번 일정에 넣지 않습니다. 개념을 10~15분 보고 바로 작은 코드 3개를 실행하세요. 해설은 스스로 시도한 뒤 막힌 한 부분을 확인하는 데만 씁니다.')
p('공개 기출에서 확인한 학습 우선순위','sub')
p('변수·출력과 자료형은 A 1번, 반복 조건과 한 줄 수정은 B 3·8번, 반복 시뮬레이션은 B 9번, 좌표·범위 검사는 A 9번, 조건 필터링과 정렬은 A 10번에서 직접 연습할 수 있습니다. 이는 공개 문제 관찰 결과이며 실제 시험의 유형별 출제 비율을 추정한 통계는 아닙니다. [2][3][4][5]')

page('문제를 푸는 방법과 준비 상태 점검')
p('문제 하나를 공부하는 순서','sub')
for t in ['1. 입력과 출력부터 읽고, 반환값이 숫자·문자열·리스트 중 무엇인지 적습니다.','2. 예시를 손으로 따라갑니다. 변수 값이 반복마다 어떻게 바뀌는지 3~5줄 표로 씁니다.','3. 한국어로 해결 순서를 2~4줄 적고 코드로 옮깁니다. 처음부터 짧은 코드를 만들 필요는 없습니다.','4. 연습에서 기본 문제는 8~12분, 코드 작성은 20분 혼자 시도합니다. 막히면 설명이나 힌트 한 부분만 보고 다시 작성합니다.','5. 정답 코드를 닫고 15~30분 뒤 다시 풉니다. 다음 날 한 번 더 풀어야 완료로 기록합니다.']:
    p(t)
p('오답은 정답 코드보다 원인을 남기기','sub')
p('기록 예시: 문제 A 5 / 내 실수 range 끝값 포함으로 착각 / 원인 마지막 인덱스를 넘김 / 바꿀 규칙 range(n)은 0부터 n-1 / 다음 날 혼자 성공 여부 O 또는 X. 코드를 통째로 베끼는 대신 다음 문제에서도 쓸 규칙 한 줄을 남기세요.')
p('50분 시간 배분 권장안','sub')
table(['경과 시간','행동'],[
('0~3분','전체를 훑어 즉시 풀 수 있는 문제부터 고르기'),
('3~25분','기본 문법·빈칸·디버깅 우선 해결. 2~3분 동안 진전이 없으면 표시하고 이동'),
('25~42분','남은 문제 중 코드 작성 등 해결 가능성이 높은 것에 집중'),
('42~48분','미해결 재검토. 최소 입력·경계값·반복 종료·반환 타입 검사'),
('48~50분','문제별 최종 제출 상태와 남은 빈칸을 확인'),
],[108,397])
p('월요일 결과에 따라 화요일을 바꾸기','sub')
p('<b>기본 유형에서 3개 이상 막혔다면</b> 화요일 첫 50분은 전체 세트 대신 조건·반복·리스트 오답에 씁니다. 어려운 코드 작성은 1개만 남깁니다. <b>기본 유형이 안정적이면</b> 첫 50분은 전체 재풀이, 다음 40분은 코드 작성과 경계값 검사에 씁니다.')
p('점검표: 기본 유형 8개 중 7개 이상을 해설 없이 해결 / 쉬운 코드 작성 1개를 15분 안에 완성 / 틀린 줄의 이유 설명 / 모든 시도한 문제의 제출 확인. 달성 여부는 연습 지표이고 실제 점수나 합격률은 아닙니다. 같은 문제를 외워 맞힌 것은 독립 해결에 포함하지 않습니다.','small')
p('시간이 크게 부족하다면','sub')
p('하루 90분만 가능하면 15분 문법 복습 + 50분 약점 문제 3~4개 + 25분 오답 재풀이를 지킵니다. 주말 한 날을 잃으면 기초 문제 추가 풀이와 어려운 코드 작성부터 줄이고, 50분 연습 1회와 사전 테스트는 유지합니다. 600점 준비의 여유가 줄어드는 만큼 기본 유형의 실수를 먼저 줄이세요.')

page('Python에서 반드시 익힐 문법')
p('예제를 눈으로 읽고 끝내지 말고 숫자와 조건을 바꿔 실행하세요. 아래는 기출의 정답 코드가 아닌 기초 학습 예시입니다.','small')
table(['개념','꼭 알아둘 동작'],[
('자료형','input()은 문자열. int("12")는 정수. "3" + "10"은 "310", 3 + 10은 13'),
('연산','/ 나눗셈, // 바닥 나눗셈, % 나머지. 17 // 2는 8, 17 % 2는 1. = 대입, == 비교'),
('조건문','if / elif / else 뒤 콜론과 들여쓰기. and는 모두 참, or는 하나라도 참'),
('반복','range(5)는 0~4. range(1, 6)은 1~5. while은 반복마다 종료 조건에 가까워져야 함'),
('리스트','a[0] 첫 값, a[-1] 마지막 값. 유효 인덱스는 0부터 len(a)-1. append(x)는 뒤에 추가'),
('문자열','s[:3]은 앞 3글자, s[-4:]는 끝 4글자. s.replace("a", "b") 결과는 새 문자열'),
('함수','def solution(...): 아래에 코드. return은 호출한 곳에 결과 전달. print는 화면 출력'),
('2차원 자료','board[r][c]는 r행 c열. 접근 전 0 <= r < 행 수, 0 <= c < 열 수 확인'),
('자주 쓰는 함수','len, sum, min, max, sorted. a.sort()는 원본 정렬 후 None 반환'),
],[98,407])
p('조건에 맞는 값의 개수와 합','sub')
code('def solution(nums):\n    count = 0\n    total = 0\n    for x in nums:\n        if x >= 10:\n            count += 1\n            total += x\n    return [count, total]')
p('solution([4, 10, 13])의 결과는 [2, 23]입니다. total과 count는 반복문 밖에서 초기화해야 앞의 결과가 유지됩니다.','small')
p('조건에 맞는 행만 고르고 정렬하기','sub')
code('rows = [["A", 8], ["B", 3], ["C", 10]]\nselected = []\nfor row in rows:\n    if row[1] < 10:\n        selected.append(row)\nselected.sort(key=lambda row: row[1])')
p('결과는 [["B", 3], ["A", 8]]입니다. lambda row: row[1]은 각 행의 두 번째 값을 정렬 기준으로 쓰겠다는 뜻입니다. 아직 이해가 어려우면 먼저 필터링 부분까지 혼자 작성하세요.','small')

page('처음 시작할 때 직접 풀 자체 연습')
p('다음 4문제는 이 계획을 위해 만든 기초 연습이며 공식 기출이나 모의 점수표가 아닙니다. 답을 가리고 5~10분씩 시도한 뒤 예시 결과를 확인하세요.')
p('1 숫자와 문자열','sub')
p('a = "7", b = 3일 때 a + str(b)와 int(a) + b의 결과를 각각 예상하고 실행하세요. 두 결과가 다른 이유를 한 문장으로 설명합니다.')
p('2 조건에 맞는 개수','sub')
p('정수 리스트 nums에서 짝수 개수를 return하는 solution(nums)를 만드세요. [1, 2, 4, 7]은 2, [3]은 0, [0, 2]는 2가 나와야 합니다.')
p('3 한 줄 수정','sub')
p('다음 함수는 양수의 합을 구하려 하지만 결과가 틀립니다. 한 줄만 고치세요. [1, -2, 3]의 결과는 4여야 합니다.')
code('def solution(nums):\n    total = 0\n    for x in nums:\n        if x > 0:\n            total = x\n    return total')
p('4 반복 종료','sub')
p('양의 정수 n을 2로 나눈 몫으로 계속 바꾸다가 1 이하가 될 때까지의 횟수를 return하세요. 10은 10 → 5 → 2 → 1이므로 3, 1은 0입니다. 함수 이름은 solution(n)으로 정합니다.')
p('정답과 확인할 이유','sub')
p('1번: 문자열 "73"과 정수 10. +는 자료형에 따라 이어붙이기 또는 덧셈으로 동작합니다. 3번: total = x를 total += x로 바꿉니다. 기존 코드는 합을 쌓지 않고 매번 덮어씁니다.','small')
code('# 2번\ndef solution(nums):\n    count = 0\n    for x in nums:\n        if x % 2 == 0:\n            count += 1\n    return count\n\n# 4번 별도로 실행\ndef solution(n):\n    count = 0\n    while n > 1:\n        n //= 2\n        count += 1\n    return count')
p('두 solution 함수는 각각 다른 문제의 예시이므로 따로 실행합니다. 다 푼 뒤 2번을 홀수 개수로, 4번을 3으로 나누는 문제로 바꿔 답 없이 작성해 보세요. 코드의 의미를 이해했는지 확인하는 연습입니다.','small')

page('시험 준비 체크와 조사 출처')
p('시험 전날까지 확인할 필수 사항','sub')
p('접수 내역에서 10월 28일의 시작 시각·Python 선택·온라인 또는 현장 응시·기관 요구 점수를 확인하세요. 날짜와 회차는 접수 내역이 최종 기준입니다. 온라인 응시는 사진이 있는 인정 신분증, PC, 마이크가 있는 웹캠, 휴대폰 카메라를 준비하고 사전 테스트로 실제 연결을 점검합니다. 일반 안내의 사전 테스트 기간은 시험 7일 전부터 1일 전까지이며, 해당 회차가 필수로 지정했다면 반드시 완료해야 합니다. [6][7]')
p('온라인 일반 규정은 한 PC·한 모니터 사용을 요구하고 외부 IDE·검색·메신저 사용을 금지합니다. 노트북은 내장 화면·키보드를 사용하며 외부 키보드는 허용되지 않습니다. 학생증은 일반 안내의 인정 신분증에 포함되지 않으므로 별도 규정 신분증을 준비하세요. 개별 단체시험의 지침이 다르면 주최 기관에 확인합니다. [6]')
p('풀고 나면 실행 결과만 확인하지 말고 각 문항의 최종 제출 여부를 확인하세요. 공개 문제의 빈칸 유형은 지정 영역만 채우며, 디버깅 유형은 한 줄만 수정하도록 제한합니다. 임의로 전체 코드를 갈아엎지 말고 화면의 안내를 먼저 읽습니다. [2][3]')
p('조사한 자료와 적용 범위','sub')
sources=[
('[1] 프로그래머스 공식 인증시험 소개 자료','https://business.programmers.co.kr/static/business/certification_proposal.pdf','시험 시간·문항·유형·등급 근거. 과거 발행 자료로 2026년 기관 안내 [8]과 교차 확인.'),
('[2] 공식 무료 PCCE 기출 코스','https://school.programmers.co.kr/learn/courses/19274/19274-pcce-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-1%ED%9A%8C','10문항 무료 공개 및 빈칸 채우기 학습 자료. 페이지 표시 최종 업데이트 2026년 8월 26일.'),
('[3] 공식 닉네임 규칙 문제','https://school.programmers.co.kr/learn/courses/30/lessons/340200','한 줄 수정 제한과 문자열·반복 학습 근거. 다른 B 문제도 공식 원문 확인.'),
('[4] 공식 이웃한 칸 문제','https://school.programmers.co.kr/learn/courses/30/lessons/250125','2차원 리스트·인덱스·범위 검사 학습 근거.'),
('[5] 공식 데이터 분석 문제','https://school.programmers.co.kr/learn/courses/30/lessons/250121','필터링·정렬 학습 근거. 위 코드 예시는 별도로 작성.'),
('[6] 공식 응시 규정 가이드','https://user-guide.grepp.co/en/articles/2-Certification-Test--Review-the-Regulations-5fa21dff','입실 시간·외부 프로그램·모니터·키보드·신분증 주의사항 근거.'),
('[7] 공식 시험 응시 가이드','https://user-guide.grepp.co/en/articles/3-Certification-Test--Take-the-Test-ab66dd8e','준비 기기·사전 테스트 기간·필수 여부 확인 근거.'),
('[8] 동양미래대 2026년 PCCE 접수 안내','https://www.dongyang.ac.kr/dmu/4580/subview.do?enc=Zm5jdDF8QEB8JTJGY29tYkJicyUyRmRtdSUyRjg0JTJGMjk0JTJGMjUxNjU0JTJGdmlldy5kbyUzRg%3D%3D','50분·Python 포함 선택 언어·400점 인증 기준 교차 확인. 사용자의 회차 안내는 아님.'),
]
for label,url,note in sources:
    link(label,url);p(note,'small')
p('확인 범위와 해석','sub')
p('인증시험 홈페이지의 직접 열람은 403 응답으로 제한되어 공식 공개 자료·공식 문제·공식 응시 가이드와 2026년 교육기관 공지를 함께 확인했습니다. 검색에 노출된 개인 후기와 문제 정답률은 모집단·선행 경험이 달라 개인 합격 확률 근거로 사용하지 않았습니다. 날짜별 시간표·연습 기준·시간 배분은 조사 사실을 바탕으로 설계한 권장안입니다.','small')

web.append('</section>')
css='''body{font-family:"Malgun Gothic",sans-serif;background:#f1f3f5;color:#15191e;margin:0;line-height:1.75}main{max-width:920px;margin:24px auto}section{background:white;padding:42px 48px;margin-bottom:20px}h1{font-size:32px}h2{font-size:24px}h3{font-size:17px;margin-top:24px}table{border-collapse:collapse;width:100%;font-size:14px}th,td{border:1px solid #d9d9d9;padding:10px;text-align:left}th{background:#e8edf3}a{color:#174b7a}pre{font-family:Consolas,"Malgun Gothic",monospace;white-space:pre-wrap;background:#f4f6f8;padding:16px}p{margin:10px 0}@media print{body{background:white}main{margin:0}section{padding:0;break-after:page;box-shadow:none}}@media(max-width:700px){section{padding:24px 18px}main{margin:0}h1{font-size:27px}}'''
(OUT/'PCCE_Python_600점_학습계획.html').write_text('<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PCCE Python 600점 준비 계획</title><style>'+css+'</style><main>'+''.join(web)+'</main></html>',encoding='utf-8')
def footer(c,doc):
    c.setFont('Malgun',8);c.setFillColor(colors.HexColor('#56616c'))
    c.drawString(45,25,'PCCE Python 600점 준비 계획  |  2026년 10월 23일 작성')
    c.drawRightString(550,25,str(doc.page))
pdf=OUT/'PCCE_Python_600점_학습계획.pdf'
doc=SimpleDocTemplate(str(pdf),pagesize=(595.28,841.89),leftMargin=45,rightMargin=45,topMargin=39,bottomMargin=43,title='PCCE Python 600점 준비 계획',author='학습 계획')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
r=PdfReader(str(pdf));print('PDF pages:',len(r.pages))
for i,pg in enumerate(r.pages):print(i+1,len(pg.extract_text()),pg.extract_text()[:45].replace('\n',' '))
print('Files:',*[str(x) for x in OUT.iterdir()],sep='\n')

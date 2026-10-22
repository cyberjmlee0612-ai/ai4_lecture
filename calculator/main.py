"""HTML 폼으로 사용하는 FastAPI 사칙연산 계산기."""

import re
from decimal import Decimal, ROUND_HALF_UP, localcontext
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="두 수 계산기")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")
SYMBOLS = {"add": "+", "subtract": "−", "multiply": "×", "divide": "÷"}


def parse_number(raw: str, label: str) -> Decimal:
    text = raw.strip()
    if not text:
        raise ValueError(f"{label}를 입력해 주세요.")
    if len(text) > 40 or not re.fullmatch(r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)", text):
        raise ValueError(f"{label}에는 숫자만 입력해 주세요. 예: -12.5")
    if "." in text and len(text.split(".")[1]) > 12:
        raise ValueError("소수점 아래는 최대 12자리까지 입력할 수 있습니다.")
    value = Decimal(text)
    if abs(value) > Decimal("1000000000000"):
        raise ValueError("숫자는 -1조부터 1조까지 입력할 수 있습니다.")
    return value


def calculate(a: str, b: str, operation: str) -> dict:
    if operation not in SYMBOLS:
        raise ValueError("올바른 연산을 선택해 주세요.")
    first = parse_number(a, "첫 번째 수")
    second = parse_number(b, "두 번째 수")
    # 허용한 입력의 곱과 나눗셈을 처리할 수 있는 정밀도입니다.
    with localcontext() as context:
        context.prec = 60
        if operation == "add":
            value = first + second
        elif operation == "subtract":
            value = first - second
        elif operation == "multiply":
            value = first * second
        else:
            if second == 0:
                raise ValueError("0으로 나눌 수 없습니다. 두 번째 수를 바꿔 주세요.")
            value = first / second
        rounded = value.quantize(Decimal("0.000000000001"), rounding=ROUND_HALF_UP)
    display = format(rounded, "f").rstrip("0").rstrip(".")
    if rounded == 0:
        display = "0"
    return {"value": display, "symbol": SYMBOLS[operation], "approximate": rounded != value}


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={})


@app.post("/calculate", response_class=HTMLResponse)
def submit(
    request: Request,
    a: Annotated[str, Form()] = "",
    b: Annotated[str, Form()] = "",
    operation: Annotated[str, Form()] = "",
):
    context = {"a": a, "b": b, "operation": operation}
    status_code = 200
    try:
        context["result"] = calculate(a, b, operation)
    except ValueError as exc:
        context["error"] = str(exc)
        status_code = 400
    return templates.TemplateResponse(
        request=request, name="index.html", context=context, status_code=status_code
    )

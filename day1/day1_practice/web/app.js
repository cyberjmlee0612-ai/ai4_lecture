"use strict";

const byId = (id) => document.getElementById(id);

function showResult(id, message, state = "") {
  const output = byId(id);
  output.textContent = message;
  output.className = `result ${state}`.trim();
}

function readInteger(id) {
  const value = byId(id).value.trim();
  if (!/^[+-]?\d+$/.test(value) || !Number.isSafeInteger(Number(value))) {
    throw new Error("정수를 입력하세요. 너무 큰 숫자는 사용할 수 없습니다.");
  }
  return Number(value);
}

function onSubmit(formId, resultId, action) {
  byId(formId).addEventListener("submit", (event) => {
    event.preventDefault();
    try { action(); }
    catch (error) { showResult(resultId, error.message, "error"); }
  });
}

onSubmit("variables-form", "variables-result", () => {
  const a = readInteger("number-1");
  const b = readInteger("number-2");
  if (!Number.isSafeInteger(a + b)) throw new Error("계산 결과가 너무 큽니다. 더 작은 정수를 입력하세요.");
  showResult("variables-result", `${a} + ${b} = ${a + b}`);
});

onSubmit("conditions-form", "conditions-result", () => {
  const score = readInteger("score");
  if (score < 0 || score > 100) throw new Error("점수는 0~100 사이여야 합니다.");
  showResult("conditions-result", `${score}점 → ${score >= 60 ? "합격" : "불합격"}`, score >= 60 ? "success" : "");
});

onSubmit("lists-form", "lists-result", () => {
  const values = byId("numbers").value.trim().split(/[,\s]+/);
  if (values.length !== 5 || values.some((value) => !/^[+-]?\d+$/.test(value) || !Number.isSafeInteger(Number(value)))) {
    throw new Error("쉼표 또는 공백으로 구분한 정수 5개를 입력하세요.");
  }
  const numbers = values.map(Number);
  const even = numbers.filter((number) => number % 2 === 0);
  showResult("lists-result", `입력 리스트: [${numbers.join(", ")}]\n짝수: ${even.length ? even.join(", ") : "없음"}`);
});

onSubmit("multiplication-form", "multiplication-result", () => {
  const horizontal = byId("table-mode").value === "by-row";
  const end = Number(byId("table-end").value);
  const table = document.createElement("table");
  const caption = table.createCaption();
  caption.textContent = horizontal ? `2~9단 · 곱하는 수 1~${end}` : `2~4단 · 곱하는 수 1~${end}`;
  const heading = table.createTHead().insertRow();
  const columns = horizontal ? 8 : end;
  for (let column = 0; column < columns; column++) {
    const th = document.createElement("th");
    th.scope = "col";
    th.textContent = horizontal ? `${column + 2}단` : `× ${column + 1}`;
    heading.append(th);
  }
  const body = table.createTBody();
  for (let row = 0; row < (horizontal ? end : 3); row++) {
    const tr = body.insertRow();
    for (let column = 0; column < columns; column++) {
      const dan = horizontal ? column + 2 : row + 2;
      const i = horizontal ? row + 1 : column + 1;
      tr.insertCell().textContent = `${dan} × ${i} = ${dan * i}`;
    }
  }
  const wrapper = document.createElement("div");
  wrapper.className = "table-scroll";
  wrapper.tabIndex = 0;
  wrapper.setAttribute("role", "region");
  wrapper.setAttribute("aria-label", "구구단 결과, 가로로 스크롤할 수 있습니다");
  wrapper.append(table);
  const output = byId("multiplication-result");
  output.className = "result";
  output.replaceChildren(wrapper);
});

let target;
let attempts;
let finished;

function resetGame() {
  target = Math.floor(Math.random() * 100) + 1;
  attempts = 0;
  finished = false;
  byId("guess").value = "";
  byId("guess").disabled = false;
  byId("guess-button").disabled = false;
  byId("game-history").replaceChildren();
  showResult("game-result", "첫 번째 숫자를 입력하세요. 시도 횟수: 0");
}

onSubmit("game-form", "game-result", () => {
  if (finished) return;
  const guess = readInteger("guess");
  if (guess < 1 || guess > 100) throw new Error("1~100 사이의 정수를 입력하세요.");
  attempts++;
  const hint = guess > target ? "정답보다 큽니다." : guess < target ? "정답보다 작습니다." : "정답입니다!";
  const record = document.createElement("li");
  record.textContent = `${guess} → ${hint}`;
  byId("game-history").prepend(record);
  // 최신 기록을 위에 표시하되 실제 시도 번호를 유지합니다.
  record.value = attempts;
  showResult("game-result", `${hint} 시도 횟수: ${attempts}`, guess === target ? "success" : "");
  if (guess === target) {
    finished = true;
    byId("guess").disabled = true;
    byId("guess-button").disabled = true;
  } else {
    byId("guess").select();
  }
});

byId("reset-game").addEventListener("click", () => {
  resetGame();
  byId("guess").focus();
});
resetGame();

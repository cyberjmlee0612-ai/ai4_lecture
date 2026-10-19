"""실행: python day2/pm/chat_filter.py"""

import re


def mask_bad_words(chat_message: str, bad_words: list[str]) -> str:
    """메시지에 포함된 금지어를 대소문자 구분 없이 별표로 가린다."""
    # 원본 글자를 리스트로 복사하면 특정 위치의 글자만 바꿀 수 있다.
    masked_characters = list(chat_message)

    for word in bad_words:
        # 빈 문자열은 금지어로 처리하지 않는다.
        if word == "":
            continue

        # escape는 '.', '*', '+' 같은 문자도 그대로 찾게 해 준다.
        # IGNORECASE는 'bad', 'BAD', 'Bad'를 모두 찾게 해 준다.
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        search_start = 0

        while True:
            # 항상 원본에서 찾으므로 먼저 가린 금지어가 다음 검색을 방해하지 않는다.
            match = pattern.search(chat_message, search_start)
            if match is None:
                break

            # 발견한 범위의 글자를 하나씩 별표로 바꾸어 문자열 길이를 유지한다.
            for index in range(match.start(), match.end()):
                masked_characters[index] = "*"

            # 한 글자 뒤에서 다시 찾아 서로 겹치는 금지어도 모두 가린다.
            search_start = match.start() + 1

    # 글자 리스트를 하나의 문자열로 합쳐 반환한다.
    return "".join(masked_characters)


def validate_mask_bad_words() -> None:
    """일반 입력, 경계값, 특수문자 및 겹치는 금지어를 검증한다."""
    cases = [
        ("너는 바보야!", ["바보"], "너는 **야!"),
        ("BAD, Bad, bad!", ["bad"], "***, ***, ***!"),
        ("바보 멍청이 바보", ["바보", "멍청이"], "** *** **"),
        ("즐거운 게임!", ["바보"], "즐거운 게임!"),
        ("", ["바보"], ""),
        ("그대로 유지", [], "그대로 유지"),
        ("빈 단어 무시", [""], "빈 단어 무시"),
        ("바보", ["", "바보", "바보"], "**"),
        ("a.b a+b [x] ab", ["a.b", "a+b", "[x]"], "*** *** *** ab"),
        ("ababa", ["aba"], "*****"),
        ("abcde", ["abc", "cde"], "*****"),
        ("abcde", ["cde", "abc"], "*****"),
        ("badly", ["bad"], "***ly"),
        ("  BaD!\n안녕\t바보🙂", ["bad", "바보"], "  ***!\n안녕\t**🙂"),
        ("", [], ""),
        ("", ["", "bad"], ""),
        ("bad", ["bad"], "***"),
        ("bad 시작", ["bad"], "*** 시작"),
        ("끝 bad", ["bad"], "끝 ***"),
        ("badbadBAD", ["bad"], "*********"),
        ("a A b", ["a"], "* * b"),
        ("ba", ["bad"], "ba"),
        ("b a d / b-ad", ["bad"], "b a d / b-ad"),
        ("aaaaa", ["aa"], "*****"),
        ("badly bad", ["bad", "badly"], "***** ***"),
        ("badly bad", ["badly", "bad"], "***** ***"),
        ("BAD bad", ["bad", "BAD", "bad"], "*** ***"),
        ("a*b a.b a+b a?b", ["a*b"], "*** a.b a+b a?b"),
        ("(bad)|^$", ["(", ")", "|", "^", "$"], "*bad****"),
        ("x\\y x/y", ["x\\y"], "*** x/y"),
        ("🙂바보🙂", ["🙂"], "*바보*"),
        ("  bad\r\n다음 줄  ", ["bad"], "  ***\r\n다음 줄  "),
        ("BADWORD", ["badword"], "*******"),
        ("앞 " + "bad " * 1000 + "끝", ["bad"], "앞 " + "*** " * 1000 + "끝"),
    ]
    for message, words, expected in cases:
        original_words = words.copy()
        actual = mask_bad_words(message, words)
        assert actual == expected, f"입력={message!r}: 기대={expected!r}, 실제={actual!r}"
        assert len(actual) == len(message), "원본 메시지의 길이가 바뀌었습니다."
        assert words == original_words, "입력 금지어 목록이 바뀌었습니다."
        assert isinstance(actual, str), "반환값이 문자열이 아닙니다."

    # bad의 대소문자 조합 8가지를 직접 만들어 동일한 결과인지 확인한다.
    combination_count = 0
    for first in "bB":
        for second in "aA":
            for third in "dD":
                word = first + second + third
                message = "시작 " + word + " 끝!"
                assert mask_bad_words(message, ["bad"]) == "시작 *** 끝!", word
                assert mask_bad_words("bad", [word]) == "***", word
                combination_count += 1

    # 같은 입력을 여러 번 호출해도 이전 호출의 상태가 남지 않아야 한다.
    for _ in range(3):
        assert mask_bad_words("bad 바보", ["bad"]) == "*** 바보"
        assert mask_bad_words("bad 바보", ["바보"]) == "bad **"
        assert mask_bad_words("bad 바보", []) == "bad 바보"

    print(f"고정 사례 {len(cases)}개, 대소문자 조합 {combination_count}개, 반복 호출 검증 통과")


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("assert 검증을 위해 -O 옵션 없이 실행하세요.")
    validate_mask_bad_words()
    print("모든 assert 검증을 통과했습니다.")
    print(mask_bad_words("너는 바보야! BAD player!", ["바보", "bad"]))

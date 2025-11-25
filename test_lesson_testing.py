import pytest
from lesson_testing import (
    square_eq_solver,
    is_palindrome_iterative,
    compute_factorial,
    show_result,
    main_first_script,
    main_second_script,
    main_third_script,
    main
)


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, -3, 2, [1.0, 2.0]),
        (1, -2, 1, []),     
        (1, 0, 1, []),           
    ],
)
def test_square_eq_solver(a, b, c, expected):
    result = square_eq_solver(a, b, c)
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize(
    "data,expected_text",
    [
        ([1.2345, 2.3456], "Корень номер 1 равен 1.23"),
        ([], "не имеет действительных корней"),
    ],
)
def test_show_result(data, expected_text, capsys):
    show_result(data)
    output = capsys.readouterr().out
    assert expected_text in output


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Level", True),
        ("А роза упала на лапу Азора", True),
        ("Python", False),
    ],
)
def test_is_palindrome_iterative(text, expected):
    assert is_palindrome_iterative(text) == expected


@pytest.mark.parametrize(
    "n,expected",
    [
        (5, 120),
        (0, 1),
        (1, 1),
    ],
)
def test_compute_factorial(n, expected):
    assert compute_factorial(n) == expected


def test_compute_factorial_negative():
    with pytest.raises(ValueError, match="Факториал отрицательного числа не определён"):
        compute_factorial(-5)


@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("1 -3 2", "Корень номер 1"),
        ("1 -2 1", "Корень номер 1"),
        ("1 0 1", "не имеет действительных корней"),
    ],
)
def test_main_first_script(monkeypatch, capsys, user_input, expected):
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    main_first_script()
    output = capsys.readouterr().out
    assert expected in output


@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("Level", "является палиндромом"),
        ("Python", "не является палиндромом"),
    ],
)
def test_main_second_script(monkeypatch, capsys, user_input, expected):
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    main_second_script()
    output = capsys.readouterr().out
    assert expected in output


@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("5", "120"),
        ("1", "1"),
        ("-3", "Ошибка"),
    ],
)
def test_main_third_script(monkeypatch, capsys, user_input, expected):
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    main_third_script()
    output = capsys.readouterr().out
    assert expected in output


@pytest.mark.parametrize(
    "inputs,expected",
    [
        (["1", "1 -3 2"], "Корень номер"),
        (["2", "Level"], "палиндром"),
        (["3", "5"], "120"),
        (["0"], "Выход"),
    ],
)
def test_main(monkeypatch, capsys, inputs, expected):
    inputs_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    main()
    output = capsys.readouterr().out
    assert expected in output

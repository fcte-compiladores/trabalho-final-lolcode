import subprocess
from pathlib import Path

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"
MAIN_COMMAND = ["python3", "-m", "lolcompiler.main"]

def run_lolcode(file, input_text=None):
    if input_text is None:
        result = subprocess.run(
            MAIN_COMMAND + [str(EXAMPLES_DIR / file)],
            capture_output=True,
            text=True
        )
    else:
        process = subprocess.Popen(
            MAIN_COMMAND + [str(EXAMPLES_DIR / file)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate(input=input_text)
        result = subprocess.CompletedProcess(
            args=process.args,
            returncode=process.returncode,
            stdout=stdout,
            stderr=stderr,
        )
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def clean_stderr(stderr: str) -> str:
    lines = stderr.splitlines()
    return '\n'.join(
        line for line in lines
        if not line.startswith("WARNING: ") and not line.endswith("parser.out")
    ).strip()

def test_helloworld():
    stdout, stderr, code = run_lolcode("helloworld.lol")
    assert stdout == 'HAI WORLD!'
    assert clean_stderr(stderr) == ''
    assert code == 0

def test_calculator():
    stdout, stderr, code = run_lolcode("calculator.lol")
    assert '42' in stdout
    assert '25' in stdout
    assert clean_stderr(stderr) == ''
    assert code == 0

def test_variables():
    stdout, stderr, code = run_lolcode("variables.lol")
    assert '42' in stdout
    assert clean_stderr(stderr) == ''
    assert code == 0

def test_error():
    stdout, stderr, code = run_lolcode("error.lol")
    assert "Caractere ilegal" in stdout
    assert "Oops" in stdout


def test_helloworld_exact_output():
    stdout, stderr, code = run_lolcode("helloworld.lol")
    assert stdout.strip() == "HAI WORLD!"
    assert clean_stderr(stderr) == ''
    assert code == 0

def test_calculator_has_sum_and_product():
    stdout, stderr, code = run_lolcode("calculator.lol")
    lines = stdout.strip().splitlines()
    assert any("42" in line for line in lines), "Soma 20 + 22 deveria aparecer"
    assert any("25" in line for line in lines), "Produto 5 * 5 deveria aparecer"
    assert clean_stderr(stderr) == ''
    assert code == 0

def test_variables_with_declared_and_undeclared():
    stdout, stderr, code = run_lolcode("variables.lol")
    assert "42" in stdout
    assert clean_stderr(stderr) == ''
    assert code == 0

def test_error_invalid_token():
    stdout, stderr, code = run_lolcode("error.lol")
    assert "Caractere ilegal" in stdout
    assert "Oops" in stdout

def test_boolean_conditional_true():
    stdout, stderr, code = run_lolcode("boolean.lol")
    assert "Flag is true!" in stdout
    assert "Flag is false!" not in stdout
    assert clean_stderr(stderr) == ''
    assert code == 0

def test_input_conditional_valid_input():
    stdout, stderr, code = run_lolcode("input_conditional.lol", input_text="32\n")
    assert "42" in stdout or "42.0" in stdout  # 32 + 10 = 42
    assert clean_stderr(stderr) == ''
    assert code == 0

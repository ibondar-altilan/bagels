from bagels import NUM_DIGITS
from bagels import get_secret, get_answer

class TestGetSecret:
    secret = get_secret()

    def test_secret_is_str(self):
        assert type(self.secret) == str

    def test_secret_len(self):
        assert len(self.secret) == NUM_DIGITS

    def test_secret_is_digit(self):
        assert self.secret.isdigit()

class TestGetAnswer:
    secret = get_secret()

    def test_answer_is_str(self):
        self.guess = self.secret
        self.answer = get_answer(self.guess, self.secret)
        assert type(self.answer) == str

    def test_answer_value_fermi(self):
        self.guess = self.secret
        self.answer = get_answer(self.guess, self.secret)
        assert self.answer == ('Fermi ' * len(self.guess))[:-1]  # all digits in the right place, all Fermi

    def test_answer_value_pico(self):
        self.guess = self.secret
        self.guess = self.secret[-1] + self.secret[:-1]  # one right shift
        self.answer = get_answer(self.guess, self.secret)
        assert self.answer == ('Pico ' * len(self.guess))[:-1]    # all Pico expected

    def test_answer_value_bagels(self):
        self.digit = 0
        while str(self.digit) in self.secret:  # search incorrect digit
            self.digit += 1
        self.guess = str(self.digit) * NUM_DIGITS
        self.answer = get_answer(self.guess, self.secret)
        assert self.answer == 'Bagels'

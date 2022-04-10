from datetime import date, timedelta


class Student:
    """ A Student class as a basis for method testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        """ Create the full name """
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        """ Create email addess """
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def alert_santa(self):
        """ Place student on Santa's list if student has been naughty """
        self.naughty_list = True

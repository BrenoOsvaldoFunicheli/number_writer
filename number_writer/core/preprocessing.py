class Processor:

    def __init__(self, cursive_numbers):
        super().__init__()
        self.cursive_numbers = cursive_numbers
        self.money_integer = self.cursive_numbers[-1]
        self.money_float = self.cursive_numbers[-2]
        self.separator = self.cursive_numbers[-3]

    def _if_exist(self, value: str, start: str = "", end: str = "", replace_by: str = "") -> str:
        """[summary]

        Args:
            value (str): value to check the value

            start (str, optional): Value that will be set
            on a prefix of the value. Defaults to "".

            end (str, optional): Value that will be set
            on a sufix of the value. Defaults to "".

            replace_by (str, optional): Value that will be
            returned if the value send there isn't. Defaults to "".

        Returns:
            str: This method returns coalesce
            value with sufix or prefix case the value is not None
            and concat start str and end str.
        """

        if value is not None and value != "":
            return str(start) + str(value) + str(end)
        else:
            return replace_by

    def _get_number_text(self, number_as_str: str = 0) -> str:
        """
        This method receive some value
        less than 101 and return it corespondece as string text.
        Defaults to 0.

        Args:
            number_as_str (str, optional): The number until one hundred.

        Returns:
            str: corespondence of number as a text
        """
        final_text = ""

        if len(number_as_str) == 3:

            teen = self._get_number_text(number_as_str[1:])
            hundred = self.cursive_numbers.get(int(number_as_str[0]+"00"))
            final_text = self._if_exist(hundred, end=" e ") + teen

            if number_as_str == "100":
                # the name cem an not cento
                return self.cursive_numbers.get(101)

        else:

            value = int(number_as_str)

            if value > 20:

                teen = int(number_as_str[0]+"0")
                last = int(number_as_str[1])

                final_text = self._if_exist(
                    self.cursive_numbers.get(last), start=" e ")
                final_text = self.cursive_numbers.get(teen) + final_text
            else:
                final_text = self.cursive_numbers.get(value)

        return final_text

    def _divide_number_part(self, number) -> str:
        """
        Divide problem between 3 parts and get each
        part as a text and returns as a text and return
        a tuple with this values.


        Args:
            number (str, int): The number that will
            be converted into a three parts of number.

        Returns:
            str: returns the number as a string.
        """
        text_number = str(number)

        hundred = self._if_exist(text_number[-3:], replace_by="0")
        thousand = self._if_exist(text_number[-6:-3], replace_by="0")
        millian = self._if_exist(text_number[-9:-6], replace_by="0")

        return (millian, thousand, hundred)

    def _prepare_value(self, number):
        number_as_string = str(number)
        values = number_as_string.split(",")

        if len(values) == 1:
            return values[0], "00"
        else:
            return values[0], values[1]

    def _process_result(self, integer_part, float_part):

        millian, thousand, hundred = self._divide_number_part(integer_part)
        cents = self._get_number_text(float_part)

        hundred_text = self._get_number_text(hundred)
        thousand_text = self._get_number_text(thousand)
        millian_text = self._get_number_text(millian)


        return self._if_exist(millian_text, end=" "+self.cursive_numbers.get(1000000) + " " + self.cursive_numbers.get(-3)+" ") + self._if_exist(thousand_text, end=" " + self.cursive_numbers.get(1000) + " " + self.cursive_numbers.get(-3)+" ") + self._if_exist(hundred_text, end=" "+self.money_integer) + self._if_exist(cents, start= " " + self.cursive_numbers.get(-3)+" ", end=self.money_float)

    def get_writted_number(self, number: any) -> str:
        """
        Interface method that will be call logic the program
        and will be concat the results

        Args:
            number (any): [description]

        Returns:
            str: [description]
        """

        integer_part, float_part = self._prepare_value(number)

        return self._process_result(integer_part, float_part)


if __name__ == "__main__":
    pass

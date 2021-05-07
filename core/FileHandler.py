class FileHandler:

    @staticmethod
    def read_input(input_path: str = "input.text"):
        """
        Read txt file and get all lines as text number
        and returns a list of lines without \n escapes.

        Args:
            input_path (str, optional): The file path to get,
            numbers. 
            Defaults to "input.text".

        Returns:
            array: with the values of each line.
        """

        lines = []

        with open(input_path) as f:
            lines = [line.replace("\n", "")for line in f.readlines()]

        return lines

    @staticmethod
    def write_output(array_line, path="output.txt"):
        with open(path, 'w') as f:
            for line in array_line:
                f.write(line+"\n")

class PTRules:

    @staticmethod
    def get_ordinal_rules():
        return {
            -3:"e", # and operator
            -2: "centavos", # cent name
            -1: "reais",# integer name
            0: "",
            1: "um",
            2: "dois",
            3: "três",
            4: "quatro",
            5: "cinco",
            6: "seis",
            7: "sete",
            8: "oito",
            9: "nove",
            10: "dez",
            11: "onze",
            12: "doze",
            13: "treze",
            14: "quatorze",
            15: "quinze",
            16: "dezesseis",
            17: "dezessete",
            18: "dezoito",
            19: "dezenove",
            20: "vinte",
            30: "trinta",
            40: "quarenta",
            50: "cinquenta",
            60: "sessenta",
            70: "setenta",
            80: "oitenta",
            90: "noventa",
            100: "cento",
            101: "cem",
            200: "duzentos",
            300: "trezentos",
            400: "quatrocentos",
            500: "quinhentos",
            600: "seiscentos",
            700: "setecentos",
            800: "oitocentos",
            900: "novecentos",
            1000: "mil",
            1000000: "milhão",

        }


pt_ordinal_numbers = PTRules.get_ordinal_rules()

if __name__ == "__main__":
    print(pt_ordinal_numbers)

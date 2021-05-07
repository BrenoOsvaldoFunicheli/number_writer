from . import pt_ordinal_numbers

class LanguageRules:

    @staticmethod
    def get_rules():
        return {
            "pt": pt_ordinal_numbers

        }

languages = LanguageRules.get_rules()

if __name__=='__main__':
    print(languages)
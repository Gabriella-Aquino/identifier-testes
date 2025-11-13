class Identifier:
    def validate_identifier(self, s: str) -> bool:
        valid_id = False

        if len(s) > 0:
            valid_id = self.valid_s(s[0])

            if len(s) > 1:
                for ch in s[1:]:
                    if not self.valid_f(ch):
                        valid_id = False
                        break

        if valid_id and 1 <= len(s) <= 6:
            return True
        else:
            return False

    def valid_s(self, ch: str) -> bool:
        return ch.isalpha()

    def valid_f(self, ch: str) -> bool:
        return ch.isalpha() or ch.isdigit()

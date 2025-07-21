from sly import Lexer

class LolLexer(Lexer):

    tokens = {
        HAI, KTHXBYE, VISIBLE, GIMMEH,
        I_HAS_A, ITZ,
        SUM_OF, DIFF_OF, PRODUKT_OF, QUOSHUNT_OF,
        O_RLY, YA_RLY, NO_WAI, OIC,
        NUMBR_F, NUMBR_I, YARN, IDENTIFIER,
        AN,
    }

    ignore = ' \t'
    ignore_comment = r'BTW.*'
    

    I_HAS_A = r'I HAS A'
    SUM_OF = r'SUM OF'
    DIFF_OF = r'DIFF OF'
    PRODUKT_OF = r'PRODUKT OF'
    QUOSHUNT_OF = r'QUOSHUNT OF'
    O_RLY = r'O RLY\?'
    YA_RLY = r'YA RLY'
    NO_WAI = r'NO WAI'
    AN = r'AN'
    @_(r'[a-zA-Z][a-zA-Z0-9_]*')

    def IDENTIFIER(self, t):

        keyword_map = {
            'HAI': 'HAI', 'KTHXBYE': 'KTHXBYE', 'VISIBLE': 'VISIBLE',
            'GIMMEH': 'GIMMEH', 'ITZ': 'ITZ', 'OIC': 'OIC'
        }
        if t.value in keyword_map:
            t.type = keyword_map[t.value]
        return t

    @_(r'"[^"]*"')
    def YARN(self, t):
        t.value = t.value[1:-1]
        return t

    @_(r'\d+\.\d+')
    def NUMBR_F(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def NUMBR_I(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print(f"Linha {self.lineno}: Caractere ilegal '{t.value[0]}'")
        self.index += 1
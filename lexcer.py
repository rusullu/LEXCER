DIGITS = '0123456789'
class Lexcer:
    def __init__(self, text):
        self.text = text
        self.index = 0
        
    def consume(self):   
        ch = self.text[self.index]
        self.index += 1
        return ch
    
    def peek(self):
        if self.index >= len(self.text):
            return None
        # else:
        return self.text[self.index]
    
    def tokinize(self):
        tokens = []
        buffer = ''
        while self.peek() is not None:
            if any(self.peek() == DIGIT for DIGIT in DIGITS):
                dot_count = 0
                while (self.peek() is not None) and (any(self.peek() == DIGIT for DIGIT in DIGITS) or self.peek() == '.'):
                    if self.peek() == '.':
                        dot_count += 1
                    buffer += self.consume()
                
                if dot_count > 1:
                    raise Exception("ОШИБКА")
                
                
                tokens.append(buffer)
                buffer = ''
                continue
            
            tok = self.consume()
            if tok == " ":
                continue
            tokens.append(tok)
        return tokens
 
while True:
    a = input()
    if a == 'exit':
        break
    lexer = Lexcer(a)
    print(lexer.tokinize())
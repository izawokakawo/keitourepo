class LispInterpreter:
    def __init__(self):
        self.env = {}

    def eval(self, expr):
        if isinstance(expr, str):
            return self.env.get(expr, expr)  # Возвращаем значение переменной или саму строку
        elif not isinstance(expr, list):
            return expr  # Если это не список, возвращаем значение (число)
        
        # Обработка списка
        operator = expr[0]
        if operator == 'define':
            _, var, value = expr
            self.env[var] = self.eval(value)
            return self.env[var]
        elif operator == 'lambda':
            _, params, body = expr
            return lambda *args: self.eval(body, dict(zip(params, args)))
        elif operator == 'if':
            _, test, conseq, alt = expr
            return self.eval(conseq) if self.eval(test) else self.eval(alt)
        else:
            # Обработка арифметических операций
            func = self.eval(operator)
            args = [self.eval(arg) for arg in expr[1:]]
            return func(*args)

    def run(self, code):
        return self.eval(self.parse(code))

    def parse(self, code):
        return self.read_from_tokens(self.tokenize(code))

    def tokenize(self, code):
        return code.replace('(', ' ( ').replace(')', ' ) ').split()

    def read_from_tokens(self, tokens):
        if len(tokens) == 0:
            raise SyntaxError("Unexpected EOF")
        token = tokens.pop(0)
        if token == '(':
            lst = []
            while tokens[0] != ')':
                lst.append(self.read_from_tokens(tokens))
            tokens.pop(0)  # Убираем ')'
            return lst
        elif token == ')':
            raise SyntaxError("Unexpected )")
        else:
            try:
                return int(token)  # Пробуем преобразовать в число
            except ValueError:
                return token  # Возвращаем строку

# Пример использования
interpreter = LispInterpreter()

# Определяем функции и переменные
interpreter.run("(define square (lambda (x) (* x x)))")
interpreter.run("(define x 5)")

# Вычисляем значения
result1 = interpreter.run("(square x)")
result2 = interpreter.run("(if (> x 3) (square x) x)")

print(result1)  # 25
print(result2)  # 25


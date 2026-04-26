from parser import parse
import json

if __name__ == '__main__':
    test_code = '''
    PROGRAM TESTE
        INTEGER A, B
        A = 10
        B = 20
        PRINT *, A + B
    END
    '''
    
    try:
        ast = parse(test_code)
        print(json.dumps(ast, indent=2))
    except Exception as e:
        print(f"Erro ao analisar: {e}")

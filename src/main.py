from lexer import lexer 

if __name__ == '__main__':
    test_code = '''
    PROGRAM TESTE
        ! Declaracao de variaveis
        INTEGER A, B
        REAL C
        
        A = 10
        B = 20
        C = 3.14
        
        ! Controlo de fluxo e operadores relacionais
        IF (.NOT. A .LT. B .AND. .TRUE. .AND. .FALSE. ) THEN
            PRINT *, 'A e menor que B'
            CALL MINHASUB(A)
        ENDIF
    END
    '''
    
    print("A iniciar análise léxica...\n")
    lexer.input(test_code)
    for tok in lexer:
        print(f"Token: {tok.type:12} | Valor: {tok.value}")
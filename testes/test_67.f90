PROGRAM MIXED_67
  ! Teste de complexidade 67
  CHARACTER*20 STR
  boll X(67)
  STR = "TESTE 67"
  DO 10 I = 1, 67
    X(I) = I * 2
10 CONTINUE
  PRINT *, STR, X(1)
END
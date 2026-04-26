import sys
import os
import json

# Adicionar o diretório src ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from parser import parse

def run_test(filename, verbose=False):
    try:
        with open(filename, 'r') as f:
            code = f.read()
        
        ast = parse(code)
        if verbose:
            print(f"PASS: {filename}")
        return True, None
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    test_dir = 'testes'
    test_files = [f for f in os.listdir(test_dir) if f.startswith('test_') and f.endswith('.f90')]
    test_files.sort()
    
    total = len(test_files)
    passed = 0
    errors = []

    print(f"A executar {total} testes...")
    
    for test in test_files:
        path = os.path.join(test_dir, test)
        success, err = run_test(path)
        if success:
            passed += 1
            print(".", end="", flush=True)
        else:
            errors.append((test, err))
            print("F", end="", flush=True)
        
        if (passed + len(errors)) % 20 == 0:
            print(f" {(passed + len(errors))}/{total}")

    print(f"\n\n{'='*50}")
    print(f"RESULTADOS FINAIS:")
    print(f"Sucessos: {passed}/{total}")
    print(f"Falhas:   {len(errors)}/{total}")
    print(f"{'='*50}")

    if errors:
        print("\nDETALHES DOS ERROS:")
        for test, err in errors:
            print(f"[{test}]: {err}")
        sys.exit(1)
    else:
        print("\nTodos os 67 testes passaram com sucesso!")
        sys.exit(0)

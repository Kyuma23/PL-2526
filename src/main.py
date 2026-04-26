import sys
import json
from parser import parse, ParseError

def main():
    if len(sys.argv) < 2:
        return

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as f:
            code = f.read()
        
        try:
            ast = parse(code)
            print(json.dumps(ast, indent=2))
        except ParseError as e:
            print(f"Syntax Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
            
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)

if __name__ == '__main__':
    main()

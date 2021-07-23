import sys

def main():
    table = {
            '\\a':' - Bell(alert)',
            '\\b':' - Baclspace',
            '\\n':' - New line',
            '\\t':' - Horizontal tab',
            '\\\\':' -  Backslash \ ',
            '\\"':'  - Double quotation mark "',
            "\\'":'  - Single quotation mark '
    }
    for k, v in table.items():
        print(k, v)

if __name__ == '__main__':
    if sys.version_info[0] < 3:
         raise Exception("Python 3 or more recent version is required")
    main()


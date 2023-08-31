import argparse, dis, sys

import frontend
import backends


_version = '0.4.0'


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'infile',
        help='Python source file to disassemble'
    )
    parser.add_argument(
        '-o',
        '--outfile',
        type=str,
        default='result',
        help='file to output the compiled program to'
    )
    parser.add_argument(
        '-f',
        '--format',
        choices=('c', 'spy'),
        default='c',
        const='c',
        nargs='?',
        help='Output format (default: %(default)s)'
    )
    parser.add_argument(
        '-a',
        '--attributes',
        action='store_true',
        help='List attributes of the Python program'
    )
    parser.add_argument(
        '-d',
        '--disassemble',
        action='store_true',
        help='Show Python bytecode disassembly'
    )
    parser.add_argument(
        '-x',
        '--hexdump',
        action='store_true',
        help='hexdump the compiled program'
    )
    return parser.parse_args()

def hexdump(binary):
    chars = "................................ !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~................................................................................................................................."
    disp = ''
    addr = 0
    while True:
        line = binary[addr:addr + 16]
        text = ''
        if line == b'': break
        if disp != '': disp += '\n'
        disp += '{:08X}  '.format(addr // 4)  # addr // 4 gives word addresses

        for b, byte in enumerate(line):   # Note that byte is an int when you iterate bytes
            disp += '{:02X} '.format(byte)
            text += chars[byte]
            if b % 4 == 3: disp += ' '

        disp += ' ' * (4 - (b // 4))
        for i in range(15 - b): disp += '   '
        disp += '|{}|'.format(text)
        addr += 16
    print(disp)

def formatDataSize(size, rounding=2):
    units = ('B', 'kB', 'MB', 'GB', 'TB', 'PB')
    selectedUnit = 0
    while size >= 1024:
        size /= 1024
        selectedUnit += 1
        if selectedUnit == len(units) - 1: break
    else: return str(round(size, rounding)) + units[selectedUnit]


if __name__ == '__main__':
    print('Compyle {} on Python {}'.format(_version, sys.version))

    args = getArgs()

    with open(args.infile, 'r') as infile:
        source = infile.read()
    print('Read {} from {}'.format(formatDataSize(len(source)), args.infile))

    codeObject = frontend.process(source, args.infile)

    backendMetadata = {
        'Compyle version': _version,
        'Python version': sys.version.replace('\n', ''),
        'Original filename': args.infile
    }

    result = backends.backends[args.format].process(codeObject, backendMetadata)

    if args.disassemble:
        dis.dis(source)

    if args.hexdump:
        hexdump(result)

    with open(args.outfile, 'wb') as outfile:
        outfile.write(result)
        
    print('Wrote {} to {}'.format(formatDataSize(len(result)), args.outfile))

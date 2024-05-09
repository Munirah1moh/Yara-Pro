import sys
from main_parameter_handler import *
import argparse

class bcolors:
    HEADER = '\033[95m'
    OHWHITE = '\033[97m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    banner_text = """


██╗   ██╗ █████╗ ██████╗  █████╗       ██████╗ ██████╗  ██████╗ 
╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗      ██╔══██╗██╔══██╗██╔═══██╗
 ╚████╔╝ ███████║██████╔╝███████║█████╗██████╔╝██████╔╝██║   ██║
  ╚██╔╝  ██╔══██║██╔══██╗██╔══██║╚════╝██╔═══╝ ██╔══██╗██║   ██║
   ██║   ██║  ██║██║  ██║██║  ██║      ██║     ██║  ██║╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
                                                                
                                                                                                                                                   
   """
    banner_pic = """
     
     
                  ,▄▄▄▄▄▄▄▄▄▄,
             ,▄███▀▀▀░░░░░░▀▀▀███▄
           ▄██▀░▄▄████▀▀▀▀████▄▄░▀██▄
         ▄█▀░▄██▀▀            ▀▀██▄⌠██▄
       ▄██░▄██`     ██,▄▄,██     ▀██▄░██
      ▄█▀░██▀       ▐██████        ▀██░██
     ▐█▌░██   ▄     ███████▌    ,▄  `██▒██
     ██░██'   ▀█▄▄▄██▒▒██▒▒██▄▄██▀   ▐█▌░█▌
     █▌░██      ▀▀██▒╢╢██▒▒▒██▀▀      ██▒██
     █▌░██   ,▄▄▄▄██╢╢╢██▒▒▒██▄▄▄▄    ██▒██
     ██░██⌐       ██▒╢╢██▒▒▒█▌       ▐█▌░█▌
     ▐█▌░██    ▄█████▒╢██▒▒█████▄    ██▒██
      ▀█▄░██, ██`   ▀██████▀   ▀██ ▄██░██▀
       ▀██░▀█▄         -`-       ▄██▀░██
         ██▄░▀██▄,            ▄▄██▀░█████▄
          `▀██▄░▀▀███▄▄▄▄▄████▀▀░▄████▒▒▒███▄▄▄
              ▀███▄▄▄░░⌠⌠░░▄▄▄███▀   ▀██▒╣███▀▀██,
                 `▀▀▀▀▀▀▀▀▀▀▀`         ▀███▀▒▒▒░▀██▄
                                        ██░▒▒▒▒▒▒▒▀██▄
                                         ▀██░▒▒▒▒▒▒▒░▀█▄
                                           ▀██░▒▒▒▒▒▒▒░▀██
                                             ▀██▄▒▒▒▒▒▒░██
                                               ▀██▄░▒▄██▀
                                                 `▀███▀
                                                                                                                                                                
     
   Developed by: 
   → Munirah Alsahli
   → Shahad Alrabaie
   → Maha Alshammari
   → jihan Sultan  
     """
    print(bcolors.OKBLUE + banner_text + bcolors.ENDC)
    print(bcolors.OHWHITE + banner_pic + bcolors.ENDC)


    # get the user flags
    parser = argparse.ArgumentParser(
        prog='Yara-Pro', description='A tool that preforms metadata extraction and file scaning for malware.', epilog='-h or --help to see all commands')
    parser.add_argument(
        '--yara', '-y', help='use only yara', action='store_true')
    parser.add_argument(
        '--custom', type=str, help='run yara on costum rules', metavar='yara rules file')
    parser.add_argument('--dir', type=str,
                        help='directory path', metavar='dir path')
    parser.add_argument('--file', type=str,
                        help='file path', metavar='file path')
    parser.add_argument(
        '--repo', help='yara scan with repository rules', action='store_true')
    parser.add_argument(
        '--update', '-u', help='update yara rules', action='store_true')
    parser.add_argument('--metadata', '-m', help='extract metadata only',
                        metavar='full file/folder path', type=str)
    parser.add_argument('--csv', '-c', type=str, help='export as csv',
                        metavar='csv file name and path', required=False, default='exiftool_report.csv')
    parser.add_argument('--report', '-r', type=str, help='export yara html report',
                        metavar='report name file name and path')
    parser.add_argument(
        '--all', '-a', help='metadata extraction and file scaning', action='store_true')

    # construct argparser object
    args = parser.parse_args()

    # call parser handler
    parserHandler(args)


if __name__ == "__main__":
    main()

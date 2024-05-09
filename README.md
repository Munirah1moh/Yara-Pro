# Yara Pro

A tool that preforms metadata extraction and file scaning for malware.

> **Attention** **Use At your own risk**

## Discription

The <a href=https://github.com/Munirah1moh/Yara-Pro>Yara Pro</a> is a simple command line tool that mix beteween exiftool and yara, This tool used as a file/s malware detector as well to extract all the file/s meta data

## Content

- [Yara Pro](#yara-pro)
  - [Discription](#discription)
  - [Content](#content)
  - [Features](#features)
  - [Installation](#installation)
  - [Flags](#flags)
  - [Examples](#examples)
  - [Reference](#reference)
  - [license](#license)

## Features

- Can Combine both exiftool metadata and yara match result in one report
- Suport yara scanner file/dir based on repository rules for more info <a href=https://github.com/iomoath/yara-scanner>Yara scanner by Moath Maharmeh </a>.
- Suport csv and html report extraction.

## Installation

- **`pip install -r requirements.txt`** or **`pip3 install -r requirements.txt`**

## Flags

The following table shows all the command line flags and their description :

| **Flag**          | **Description**                      |
| :---------------- | :----------------------------------- |
| `-h` , `--help`   | help                                 |
| `-y` , `--yara`   | use yara only                        |
| `--custom`        | run yara on cunstom rules            |
| `--dir`           | folder to be checked by yara         |
| `--file`          | file to be checked by yara           |
| `--repo`          | run yara on repository rules         |
| `u`,`--update`    | update yara-scanner repository rules |
| `-m`,`--metadata` | extract metadata only                |
| `-c` , `--csv`    | export csv file                      |
| `-r` , `--report` | generate report                      |
| `-a` , `--all`    | metadata extraction and file scaning |

_Table: Progam flags_

You can run exfy -h to see all the avialble command

```shell
python3 yara-pro.py -h




██╗   ██╗ █████╗ ██████╗  █████╗       ██████╗ ██████╗  ██████╗
╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗      ██╔══██╗██╔══██╗██╔═══██╗
 ╚████╔╝ ███████║██████╔╝███████║█████╗██████╔╝██████╔╝██║   ██║
  ╚██╔╝  ██╔══██║██╔══██╗██╔══██║╚════╝██╔═══╝ ██╔══██╗██║   ██║
   ██║   ██║  ██║██║  ██║██║  ██║      ██║     ██║  ██║╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝      ╚═╝     ╚═╝  ╚═╝ ╚═════╝




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

usage: Yara-Pro [-h] [--yara] [--custom yara rules file] [--dir dir path] [--file file path] [--repo] [--update]
                [--metadata full file/folder path] [--csv csv file name and path]
                [--report report name file name and path] [--all]

A tool that preforms metadata extraction and file scaning for malware.

options:
  -h, --help            show this help message and exit
  --yara, -y            use only yara
  --custom yara rules file
                        run yara on costum rules
  --dir dir path        directory path
  --file file path      file path
  --repo                yara scan with repository rules
  --update, -u          update yara rules
  --metadata full file/folder path, -m full file/folder path
                        extract metadata only
  --csv csv file name and path, -c csv file name and path
                        export as csv
  --report report name file name and path, -r report name file name and path
                        export yara html report
  --all, -a             metadata extraction and file scaning

-h or --help to see all commands
```

## Examples

To run metadata on dir or file

- **`python3 yara-pro.py --metadata  Images/`** {dir/file}

To run metadata on dir or file and export .csv report

> Attention **metadata report only support CSV**

- **`python3 yara-pro.py --metadata  Images/ --csv report.csv`** {dir/file}

To run yara{custom rules}

- **`python3 yara-pro.py --yara  --custom yarafile --file Images/file.jpg`** {file}
- **`python3 yara-pro.py --yara  --custom yarafile --dir Images/`** {dir}

To run yara{yara scanner repository rules} .html report

> Attention **yara-scanner report only support html**

- **`python3 yara-pro.py --yara --repo --dir Images/ --report report.html`** {dir}
- **`python3 yara-pro.py --yara --repo --dir Images/ --report report.html`** {file}

To run both yara{yara scanner repository rules} and exify and export .csv and .html report

> Attention **For all flag the report file doesn't has extention. It will auto generate report with both .csv and .html**

- **`python3 yara-pro.py --all --repo --dir Images/ --report report`** {directory}
- **`python3 yara-pro.py --all --repo --file Images/test.jpg --report report`** {file}

To run both yara{custom rules} and exify and export .csv and .html report

- **`python3 yara-pro.py --all --custom custom_rules/r1.yar --dir Images/ --report report`**

## Reference

- <https://github.com/VirusTotal/yara>
- <https://github.com/smarnach/pyexiftool>
- <https://github.com/iomoath/yara-scanner>

## license

This work is under [GNU GENERAL PUBLIC LICENSE](LICENSE)

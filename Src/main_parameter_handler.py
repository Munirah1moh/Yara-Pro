import sys
from exiftool_handler import *
from yara_handler import *
from all_handler import *
import yara_updater
import yara_scanner
import report_generator
import common_functions




def parserHandler(args):

    # parser yara rules update
    if(args.update):
        print("- Updating yara rules ...")
        yara_updater.update()
        return
       
    # parse exif tool
    if(args.metadata):

        if(args.csv):

            try:
                exifConvertToCsv(args.metadata, args.csv)
            except Exception as e:
                print(e)
                print('Please check the file/s path')

        else:
            try:
                exifExtractAll(args.metadata)
            except Exception as e:
                print(e)
                print('Please check the file/s path')


    # parse yara
    if(args.yara):
        
        # run yara with custom rule
        if(args.custom):
            
            try:
                if(args.file):
                    match_result = yaraRunRuleFromFile(args.custom,args.file)
             
                    
                if(args.dir):
                    match_result = yaraRunRuleFromDir(args.custom,args.dir)
          
                    
            except Exception as e:
                print(e)

        
        # run yara with repository rules
        elif(args.repo):

            try:
                if(args.file):
                    match_result = yara_scanner.scan_file(args.file)

                elif(args.dir):
                    match_result = yara_scanner.scan_directory(args.dir, 1)


                if match_result is None:
                    raise Exception()
            except:
                sys.exit(0)

        if(args.report):
            match = [match for match in match_result if match['match_list']]
            report = report_generator.generate_report(match)
            common_functions.write_to_file(args.report, report)
            print('[+] Report saved to "{}"'.format(args.report))
        
    # parse all
    if(args.all):

        # yara and exif tool with yara scanner 
        if(args.repo):

            try:

                if(args.file):

                    metadata = exifExtractAll(args.file)
                    match_result = yara_scanner.scan_file(args.file)

                elif(args.dir):

                    metadata = exifExtractAll(args.dir)
                    match_result = yara_scanner.scan_directory(args.dir, 1)

                if(args.report):
                        match = [match for match in match_result if match['match_list']]
                        ExportALLToCsv(metadata,match,args.report+'.csv')
                        ExportALLToHTML(metadata,match,args.report+'.html')
                    
            except Exception as e:
                print(e)


        elif(args.custom):

            try:

                if(args.file):
                        
                    metadata = exifExtractAll(args.file)

                    match_result = yaraRunRuleFromFileAll(args.custom,args.file)

            
                if(args.dir):
                        
                        metadata = exifExtractAll(args.dir)
                        
                        match_result = yaraRunRuleFromDirAll(args.custom,args.dir)

                        # generate reports
                        
                if(args.report):
                        match = [match for match in match_result if match['match_list']]
                        ExportALLToCsv(metadata,match,args.report+'.csv')
                        ExportALLToHTML(metadata,match,args.report+'.html')



            except Exception as e:
                print(e)
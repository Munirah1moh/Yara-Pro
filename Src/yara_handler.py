import yara
import os
from pathlib import Path


# def yara_scanner:
def list_files_in_directory(directory_path):
    isDerectory = False
    file_names = []
    file_name = ''

    try:
        # Ensure the directory path exists
        if not os.path.exists(directory_path):
            print(f"The directory '{directory_path}' does not exist.")
            return
        
        # Get a list of all files in the directory
        files = os.listdir(directory_path)
        isDerectory = True
        # Loop through the list of files
        for file_name in files:
            file_names.append(file_name)
           

        return isDerectory, file_names
    
    except:
        return isDerectory, file_names



def yaraRunRuleFromDirALL(rule_path,dir):
    dic = []
    try:
     
        rules = yara.compile(filepath=rule_path)

        try: 

            isdir, name_list = list_files_in_directory(dir)

            if isdir:
                for name in name_list:
                    
                    matches = rules.match(dir+name)
                    if len(matches)!=0:
                        record = {"file": dir+name, "yara_rules_file": rule_path, "match_list": matches}
                        dic.append(record)



        except Exception as e:
            print(e)

            
    except Exception as e:
        print(e)


    return dic



def yaraRunRuleFromDirAll(rule_path,dir):
    dic = []
    try:
     
        rules = yara.compile(filepath=rule_path)

        try: 

            isdir, name_list = list_files_in_directory(dir)

            if isdir:
                for name in name_list:
                    
                    matches = rules.match(dir+name)
                    if len(matches)!=0:
                        print('{}, rule match: {} '.format(name,matches))
                        record = {"file": dir+name, "yara_rules_file": rule_path, "match_list": matches}
                        dic.append(record)



        except Exception as e:
            print(e)

            
    except Exception as e:
        print(e)


    return dic

# run yara from file
def yaraRunRuleFromDir(rule_path,dir):
    dic = []
    try:
     
        rules = yara.compile(filepath=rule_path)

        try: 

            isdir, name_list = list_files_in_directory(dir)

            if isdir:
                for name in name_list:
                    
                    matches = rules.match(dir+name)
                    if len(matches)!=0:
                        print('{}, rule match: {} '.format(name,matches))
                        record = {"file": dir+name, "yara_rules_file": rule_path, "match_list": matches}
                        dic.append(record)



        except Exception as e:
            print(e)

            
    except Exception as e:
        print(e)


    return dic

    

def yaraRunRuleFromFileALL(rule,file):
    
    dic = []
    try:
        rules = yara.compile(filepath=rule)
        
        try:
            matches = rules.match(file)
            if len(matches)!=0:
                record = {"file": file, "yara_rules_file": rule, "match_list": matches}
                dic.append(record)

        except Exception as e:
            print(e)
            
    except Exception as e:
        print(e)


    return dic

# run yara from direct rule
def yaraRunRuleFromFile(rule,file):
    
    dic = []
    try:
        rules = yara.compile(filepath=rule)
        
        try:
            matches = rules.match(file)
            if len(matches)!=0:
                print('{}, rule match: {} '.format(file,matches))
                record = {"file": file, "yara_rules_file": rule, "match_list": matches}
                dic.append(record)

        except Exception as e:
            print(e)
            
    except Exception as e:
        print(e)


    return dic


def yaraRunRuleFromFileAll(rule,file):
    
    dic = []
    try:
        rules = yara.compile(filepath=rule)
        
        try:
            matches = rules.match(file)
            if len(matches)!=0:
                print('{}, rule match: {} '.format(file,matches))
                record = {"file": file, "yara_rules_file": rule, "match_list": matches}
                dic.append(record)

        except Exception as e:
            print(e)
            
    except Exception as e:
        print(e)


    return dic


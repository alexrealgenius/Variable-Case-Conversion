
from rapidfuzz import process
import re, pyperclip




def detect_cases(s):
        if "_" in s:
            return "snake"

        elif "-" in s:
            return "kebab"

        elif s[0].isupper():
            return "pascal"

        elif not((any(c.isupper() for c in s))):
            return "ambiguous"
        
        else:
            return "camel"



def get_user_choice(userInput):
    choices = ["snake", "kebab", "pascal", "camel"]

    result = process.extractOne(userInput, choices)
    result = result[0]
    return (result)

def convert_case(choice, variables):
    result_list = []
    ambiguous_result_list = []
    choice = get_user_choice(choice)
    
    for current_value in variables.split():
        key = detect_cases(current_value)
        match key:
            case "snake":
                result_list.append(convert_from_snake_case(current_value, choice))
            case "kebab":
                result_list.append(convert_from_kebab_case(current_value, choice))
            case "pascal":
                result_list.append(convert_from_pascal_case(current_value, choice))
            case "camel":
                result_list.append(convert_from_camel_case(current_value, choice))
            case "ambiguous": 
                ambiguous_result_list.append(current_value)
    
    result_string = "\n".join(result_list)
    ambiguous_result_string = "\n".join(ambiguous_result_list)
    return result_string, ambiguous_result_string

    


    
def convert_from_snake_case(input, requested_case):
    match requested_case:
        case "snake":
            return input.lower()
        
        case "kebab":
            return (input.replace("_" , "-")).lower()
        
        case "pascal":

            temp = ""
            split_string = input.split("_")
            for s in split_string:
                s = s.capitalize()
                temp += s
            return temp
        
        case "camel":

            words = input.split("_")
            pascal = "".join(w.capitalize() for w in words)
            return pascal[0].lower() + pascal[1:]
            
def convert_from_kebab_case(input, requested_case):
    match requested_case:
        case "snake":
            return input.replace("-" , "_")
        
        case "kebab":
            return input.lower()
        
        case "pascal":

            temp = ""
            split_string = input.split("-")
            for s in split_string:
                s = s.capitalize()
                temp += s
            return temp
        
        case "camel":

            words = input.split("-")
            pascal = "".join(w.capitalize() for w in words)
            return pascal[0].lower() + pascal[1:]        

def convert_from_camel_case(input, requested_case):

    match requested_case:
        case "snake":

            input = input[:1].upper() + input[1:]
            words = re.findall(r'[A-Z][^A-Z]*', input)
            words = [w.lower() for w in words]
            words[0] = words[0][:1].lower() + words[0][1:]
            return "_".join(words)
        
        
        case "kebab":

            input = input[:1].upper() + input[1:]
            words = re.findall(r'[A-Z][^A-Z]*', input)
            words = [w.lower() for w in words]
            words[0] = words[0][:1].lower() + words[0][1:]
            return "-".join(words)
        
        case "pascal":
            input = input[:1].upper() + input[1:]
            return input
        
        case "camel":
            return input       

def convert_from_pascal_case(input, requested_case):
    match requested_case:
        case "snake":

            words = re.findall(r'[A-Z][^A-Z]*', input)
            words = [w.lower() for w in words]
            return "_".join(words)
        
        
        case "kebab":

            words = re.findall(r'[A-Z][^A-Z]*', input)
            words = [w.lower() for w in words]
            return "-".join(words)
        
        case "pascal":
            return input
        
        case "camel":
            return input[:1].lower() + input[1:]


user_made_choice = False
while not(user_made_choice):
    entered_case_choice = input("\n---------\nEnter a casing convention you'd like to convert to. Currently supported are: \nsnake\nkebab\npascal\ncamel\n---------\n")
    found_choice = get_user_choice(entered_case_choice)
    user_yes_no_to_found_choice = input(f"\n---------\nConverting to {found_choice} case. Continue? Y/N\n---------\n")

    if user_yes_no_to_found_choice.lower() == "y":
        user_made_choice = True
    else:
        pass

variable_list = input("\n---------\nEnter a single string of variables delimited by whitespaces:\n---------\n")
result = (convert_case(found_choice, variable_list))

if not result[1]:
        print(f"{result[0]}")
        if input("\n---------\nCopy non-ambiguous results to clipboard? Y/N\n---------\n").lower() == "y":
            pyperclip.copy(result[0])
else:
        print(f"{result[0]}\n---------\nOne or more of your variables were ambiguous (couldn't resolve case):\n{result[1]}\n---------\n")
        if input("---------\nCopy non-ambiguous results to clipboard? Y/N\n---------\n").lower() == "y":
            pyperclip.copy(result[0])
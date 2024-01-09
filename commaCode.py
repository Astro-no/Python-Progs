# The solution
def format_list(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    else:
        formatted_list = ', '.join(items[:-1])
        formatted_list += ', and ' + items[-1]
        return formatted_list

spam = ['apples', 'bananas', 'tofu', 'cats']
formatted_string = format_list(spam)
print(formatted_string)

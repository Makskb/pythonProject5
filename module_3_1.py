calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    string = str(string)
    Rezult = (len(string), string.lower(), string.upper())
    count_calls()
    return Rezult
def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i].lower()) == string:
            Rezult = True
            break
        else:
            Rezult = False
            continue
    return Rezult

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
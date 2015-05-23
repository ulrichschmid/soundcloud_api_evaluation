__author__ = 'tobiasduemmling'

import soundcloud

def get_comments_in_string(tracks):
    reValue = []



def get_substring_ofcourse(string_array):
    reValue = []
    for substring in string_array:
        reValue += substring.split()
    return reValue


def get_map_key_value_from_string(string):
    reValue = {}
    for substring in string:
        reValue[substring] = string.count(substring)
    return reValue



print get_substring_ofcourse(["Ja,Nein,JA","Ja"])
print get_map_key_value_from_string(get_substring_ofcourse(["Ja Nein JA","Ja"]))
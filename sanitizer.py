'''
__author__ : Simbarashe Timothy Motsi
__copyright__ = "Copyright 2020, The WhatsApp Project"
__credits__ = ["Simbarashe Timothy Motsi"]
__license__ = "GPL"
__maintainer__ = "Simbarashe Timothy Motsi"
__email__ = "simbamotsi1@gmail.com"
__status__ = "Test"

*.WhatsApp Sanitizer Script.*

'''
import re
import os
# location of unsanitized chats
chat_location = "Chats/"
sanitized_scripts = "Sanitized scripts/"

for chat_file in os.listdir(chat_location):
    # opening the txt file
    opened_file = open(chat_location + chat_file, "r", encoding="utf8")
    # regex to remove the time
    regex_list = [r"(\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\s)(\w+)(\s)(-)"]
    # function to clean the code
    def clean_text(regex_list, text):
        new_text = text
        for rgx_match in regex_list:
            new_text = re.sub(rgx_match, '', new_text)
        return new_text
    # reading the actual file
    read_opened_file = opened_file.read()
    # assignig the cleaned chatto the new file
    clean_chat = clean_text(regex_list, read_opened_file)
    opened_file.close()
    
    ## 
    # writing to a new sanitized file
    ##
    f = open(sanitized_scripts + "cleaned " + chat_file, 'w', encoding='utf-8')
    f.write(clean_chat)
    f.close()
    print("Done sanitizing " +  chat_file)
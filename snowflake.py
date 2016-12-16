#Snowflake Hash Library

def snowflake(version_no, string, key, cycle_value):
    if version_no == 1:
        key_ghost = key
        string_list = "".join(list(string)[::-1])
        cycle_count = 0
        #Key cycling
        while cycle_count != cycle_value:
            key_iterator = list(key_ghost)
            key_value = ""
            key_redo = ""
            for x in key_iterator:
                value = ord(x) + 2
                key_value = key_value + chr(value)
                value2 = ord(x) + 7
                key_redo = key_redo + chr(value2)
            #Embedding key_value and key_redo
            key_value = list(key_value)
            key_redo = list(key_redo)
            embed_count = 0
            embed_result = ""
            for x in key_redo:
                key_redo_var = key_redo[embed_count]
                key_value_var = key_value[embed_count]
                embed_count = embed_count + 1
                embed_result = embed_result + key_value_var + key_redo_var
            key_ghost = embed_result
            cycle_count = cycle_count + 1
            
        cycle_count = 0
        while cycle_count != cycle_value:
            string_iterator = list(string_list)
            string_value = ""
            string_redo = ""
            for x in string_iterator:
                value = ord(x) + 2
                string_value = string_value + chr(value)
                value2 = ord(x) + 7
                string_redo = string_redo + chr(value2)
            #Embedding string_value and string_redo
            string_value = list(string_value)
            string_redo = list(string_redo)
            embed_countstr = 0
            embed_resultstr = ""
            for x in string_redo:
                string_redo_var = string_redo[embed_countstr]
                string_value_var = string_value[embed_countstr]
                embed_countstr = embed_countstr + 1
                embed_resultstr = embed_resultstr + string_value_var + string_redo_var
            string_list = embed_resultstr
            cycle_count = cycle_count + 1
        embed_result = list(embed_result)
        embed_resultstr = list(embed_resultstr)
        embed_stred = []
        oddoreven = 0
        embed_counter = 0
        for x in embed_resultstr:
            if oddoreven == 0:
                oddoreven = oddoreven + 1
                embed_stred.append(chr(ord(x) + 7))
            elif oddoreven == 1:
                oddoreven = oddoreven - 1
                embed_stred.append(chr(ord(x) + 4))
            else:
                pass
        embedstr_final = "".join(embed_stred)
        #Threading key into string
        max_count_key = len(list(embed_result))
        max_count_string = len(list(embedstr_final))
        thread_position = 0
        key_level = 0
        result = []
        while thread_position != max_count_string:
            if key_level == max_count_key:
                key_level = 0
            else:
                result.append(embed_resultstr[thread_position])
                result.append(embed_result[key_level])
                thread_position = thread_position + 1
                key_level = key_level + 1
        return "".join(result)
    else:
        raise(Exception("Not a valid version!"))
            
print(snowflake(1, "Hello", "Hello", 11))
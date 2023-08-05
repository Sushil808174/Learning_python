def longest_common_prefix(strs):
    prefix = ""
    for chars in zip(*strs):
        # print(chars)
        if len(set(chars)) == 1:
            prefix += chars[0]
        else:
            break
    return prefix
input_list = ["flower", "flow", "flight"]
output = longest_common_prefix(input_list)
print(output)

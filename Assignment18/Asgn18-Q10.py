""" python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
} """

sample_dict = {'C': 92,'Java': 66,'Python': 85}
a = min(sample_dict.values())
print([i for i in sample_dict if sample_dict[i]==a])
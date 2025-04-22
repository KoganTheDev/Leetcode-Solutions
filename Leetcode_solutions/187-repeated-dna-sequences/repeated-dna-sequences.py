class Solution(object):
    def findRepeatedDnaSequences(self, s):
        string_length = len(s)
        if string_length < 10:
            return []

        DNA_sequence_set = set()
        result_list = set()

        for i in range(string_length - 9):
            dna_slice = s[i:i+10]
            if dna_slice in DNA_sequence_set:
                result_list.add(dna_slice)
            else:
                DNA_sequence_set.add(dna_slice)

        return list(result_list)

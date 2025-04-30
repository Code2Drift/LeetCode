class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def check_max_iter(list_words):
            list_long = []
            for word in list_words:
                list_long.append(len(word))
            
            return min(list_long)

        prefix = ""
        temp_char = []
        count_words = len(strs)
        max_iter = check_max_iter(strs)

        ## char iteration
        for i in range(max_iter):
            
            for words in strs:
                temp_char.append(words[i])
            
            count_prefix = temp_char.count(temp_char[0])

            if count_prefix != count_words:
                return prefix
            
            else:
                prefix += temp_char[0]
            
            temp_char = []
    
        return prefix
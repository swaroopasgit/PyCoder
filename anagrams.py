import logging
class Anagrams:
    def are_anagrams(self, a, b):
        """
        Implement if  teo strings are anagrams
        :param a: string
        :param b: string
        :return: boolean
        """

        c={}
        d={}
        if len(a) != len(b):
            return False
        for i in a:
            if i in c:
                c[i] += 1
            else:
                c[i]=1

        for i in b:
            if i in d:
                d[i] += 1
            else:
                d[i]=1

        print(c)
        print(d)

        for key,value in c.items():
            if key not in d:
                return False
            if value != d[key]:
                return False


        return True


anagrams_object = Anagrams()
assert anagrams_object.are_anagrams("abcde", "abecd") is True

assert anagrams_object.are_anagrams("ab", "de") is False
print("SUCCESS")


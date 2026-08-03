class Solution:
    def encode(self, strs: list[str]) -> str:
        str_result = ''
        for string in strs:
            str_result += f'{len(string)}#{string}'
        return str_result
    def decode(self, s: str) -> list[str]:
        lista_str = []

        i = start = 0
        while i < len(s):
            str_final = ''
            while s[i] != '#':
                i += 1

            num_characters = int(s[start:i])

            for k in range(i+1, i + 1 + num_characters):
                str_final += s[k]
            # str_final = s[i+1 : i + 1 + num_characters]   Escrevendo a etapa de cima em fatiamento

            lista_str.append(str_final)
            i += num_characters + 1
            start = i
        
        return lista_str
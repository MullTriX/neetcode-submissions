class Solution:
    def encode(self, strs: List[str]) -> str:
        sizes = []
        encoded_string = ""
        for s in strs:
            sizes.append(len(s))
        for size in sizes:
            encoded_string += str(size)
            encoded_string += ","
        encoded_string += "#"
        for s in strs:
            encoded_string += s
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        sizes = []
        i = 0
        while s[i] != "#":
            curr = ""
            while s[i] != ",":
                curr += s[i]
                i+=1
            sizes.append(int(curr))
            i+=1
        i+=1
        for size in sizes:
            decoded_string.append(s[i:i+size])
            i+=size
        return decoded_string

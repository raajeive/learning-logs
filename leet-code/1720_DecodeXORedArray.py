class Solution:
    def decode(self, encoded, first):
        out = [first]
        for i in range(len(encoded)):
            out.append(encoded[i] ^ out[i])
        return out

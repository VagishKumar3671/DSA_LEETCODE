class Solution(object):
    def hasGroupsSizeX(self, deck):
        # Step 1: Count frequencies manually
        freq = {}
        for card in deck:
            if card in freq:
                freq[card] += 1
            else:
                freq[card] = 1

        # Step 2: Extract frequency values
        values = list(freq.values())

        # Step 3: Define our own gcd function
        def find_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Step 4: Compute GCD of all frequencies
        g = values[0]
        for v in values[1:]:
            g = find_gcd(g, v)

        # Step 5: Return True if GCD > 1
        return g > 1

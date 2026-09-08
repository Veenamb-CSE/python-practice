chars = list(s)

        letters = "abcdefghijklmnopqrstuvwxyz"

        for i in range(len(chars)):

            if chars[i] == "?":

                for letter in letters:

                    # Check left neighbor
                    if i > 0 and chars[i - 1] == letter:
                        continue

                    # Check right neighbor
                    if i < len(chars) - 1 and chars[i + 1] == letter:
                        continue

                    # Valid letter found
                    chars[i] = letter
                    break

        return "".join(chars)

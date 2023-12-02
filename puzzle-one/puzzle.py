import logging
def build_trie():
    nums = {"one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8,
            "nine": 9}
    trie = {}
    for name, val in nums.items():
        cur = trie
        for i in range(len(name) - 1):
            if name[i] not in cur:
                cur[name[i]] = {}
            cur = cur.get(name[i])
        cur[name[-1]] = {"val": val}
    return trie


def solution():
    # Build a trie of the number in characters a build a trie that ends in the expected val
    trie = build_trie()

    # EDGE CASE "eightwo"
    # make sure we consider this eight and two. luckily, there is only one letter overlap
    result = 0
    for line in open("input.txt", "r").readlines():
        first, second = -1, -1
        # Reset trie to the beginning
        cur = trie
        for ii in range(len(line)):
            if ord('0') <= ord(line[ii]) <= ord('9'):
                parsed = int(line[ii])
            else:
                jj = ii
                while jj < len(line) and line[jj] in cur:
                    cur = cur[line[jj]]
                    jj += 1
                parsed = cur.get("val", None)
            if isinstance(parsed, int) and first == -1:
                first = parsed
                second = first
            elif isinstance(parsed, int):
                second = parsed
            cur = trie
        result += (first * 10) + second
    logging.Logger("name").critical(result)


solution()

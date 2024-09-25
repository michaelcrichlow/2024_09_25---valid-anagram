def valid_anagram(s1: str, s2: str) -> bool:
    # guard clause
    if len(s1) != len(s2):
        return False

    local_list_01 = []
    for val in s1:
        local_list_01.append(val)
    local_list_01.sort()

    local_list_02 = []
    for val in s2:
        local_list_02.append(val)
    local_list_02.sort()

    for i, val in enumerate(local_list_01):
        if val != local_list_02[i]:
            return False

    return True


def isAnagram(self, s: str, t: str) -> bool:

    # handle trivial case
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


def main() -> None:
    val_01 = "rat"
    val_02 = "car"
    val = valid_anagram(val_01, val_02)
    print(val)


if __name__ == '__main__':
    main()

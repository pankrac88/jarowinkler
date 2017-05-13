def main():
    string1 = 'DWAYNE'
    string2 = 'DUANE'
    print('Jaro Winkler distance between {} and {} is: {}'.format(string1, string2, jaro_winkler_distance(string1, string2)))


def jaro_winkler_distance(string1, string2):
    jaro = jaro_distance(string1, string2)
    prefix = 0
    for index, char in enumerate(string1[:4]):
        if char == string2[index]:
            print(char)
            prefix = prefix + 1
        else:
            break

    if (jaro > 0.7):
        return jaro + ((prefix * 0.1) * (1 - jaro))
    else:
        return jaro

def jaro_distance(string1, string2):

    if len(string1) < len(string2):
        longerString = string2
        shorterString = string1
    else:
        longerString = string1
        shorterString = string2
    
    # Should be rounded down
    allowedRange = (len(longerString) // 2) - 1
    mappingIndices = [-1] * len(shorterString)
    shortMached = []
    longMatched = []
    matches = 0

    for index, char in enumerate(shorterString):
        for secondIndex in range(max(0, index - allowedRange), min(len(longerString), index + allowedRange + 1)):
            if char == longerString[secondIndex]:
                matches = matches + 1
                mappingIndices[index] = secondIndex
                shortMached.append(char)
                longMatched.insert(secondIndex, char)
                break

    halfTranspositions = 0
    for naturalIndex in range(0, len(shortMached)):
        if (mappingIndices[naturalIndex] != naturalIndex)  & (shortMached[naturalIndex] != longMatched[naturalIndex]):
            halfTranspositions = halfTranspositions + 1
    
    return ((matches / len(longerString)) + (matches / len(shorterString)) + ((matches - (halfTranspositions // 2))/matches)) / 3


if __name__ == "__main__":
    main() 
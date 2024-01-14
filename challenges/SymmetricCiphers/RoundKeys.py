from StructureOfAES import matrix2bytes
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]
round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]
def add_round_key(s, k):
    added_round_key = [
        [scolumn ^ kcolumn for scolumn, kcolumn in zip(scol, kcol)]
        for scol, kcol in zip(s, k)
    ]
    return added_round_key

#print("The added round key is: \n ", add_round_key(state, round_key))
#print("The byte array is: \n ", matrix2bytes(add_round_key(state, round_key)))

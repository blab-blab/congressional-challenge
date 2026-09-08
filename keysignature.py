notesSharp = "C,C#,D,D#,E,F,F#,G,G#,A,A#,B".split(",")
notesFlat = "C,Db,D,Eb,E,F,Gb,G,Ab,A,Bb,B".split(",")

key_name = "C Major"


def major_or_minor(key):
    if "Major" in key:
        return "major"
    elif "Minor" in key:
        return "minor"
    else:
        return "unknown"
def get_flat_sharp(key):
    #print(key)
    if len(key) == 1:
        return("n")
    if key[1] == "b":
        return("f")
    elif key[1] == "#":
        return("s")
    else:
        return("n")

def return_key_name(key):
    #print(key)
    if len(key) == 1:
        return key[0]
    if get_flat_sharp(key) == "f":
        return key[0:2]
    elif get_flat_sharp(key) == "s":
        return key[0:2]
    else:
        return key[0]


def generate_key_starting_with_note(note):
    if get_flat_sharp(note) == "s":
        index = notesSharp.index(note)
        key_notes = []
        for i in range(12):
            key_notes.append(notesSharp[(index + i) % 12])
        return key_notes
    elif get_flat_sharp(note) == "f":
        index = notesFlat.index(note)
        key_notes = []
        for i in range(12):
            key_notes.append(notesFlat[(index + i) % 12])
        return key_notes
    else:
        index = notesFlat.index(note)
        key_notes = []
        for i in range(12):
            key_notes.append(notesFlat[(index + i) % 12])
        return key_notes

print(generate_key_starting_with_note("Db"))



def return_key_notes(key):
    #print(key)
    notes = generate_key_starting_with_note(return_key_name(key))
    keysignature = []
    index = 0
    if major_or_minor(key) == "major":
        while index < 12:
            keysignature.append(notes[index])
            if index == 4 or index == 11:
                index += 1
            else:
                index += 2
    elif major_or_minor(key) == "minor":
        while index < 12:
            keysignature.append(notes[index])
            if index == 2 or index == 9:
                index += 1
            else:
                index += 2
    return keysignature

print(return_key_notes("D Major"))
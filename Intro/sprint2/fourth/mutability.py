from copy import copy, deepcopy
import weakref

dna_ta = ["T", "A"]
dna_gc = ["G", "C"]

class DNAchain:
    def __init__(self, ta_piece, gc_piece, sets):
        self.dna_segment = [*ta_piece, *gc_piece] #destructuring also holds the same reference
        ta_piece += gc_piece #modifies the original one
        self.sets = sets
        print('Checking validity of segments...')
        for x,y in zip(self.dna_segment, ta_piece+gc_piece):
            print(id(x), id(y))

if __name__ == "__main__":
    print("Copying DNA segments...")
    dna_first = list(dna_ta)
    dna_second = dna_gc[:] #shallow copy -> new container, but same references
    print("Is that the same dna piece? ", dna_first is dna_ta )
    print("But does it do its job? ", dna_first == dna_ta )

    print("Is that the same dna piece? ", dna_second is dna_gc )
    print("But does it do its job? ", dna_second == dna_gc )

    dna_first.append("T")
    print(dna_ta, dna_first)

    dna_ta.append("T")
    print(dna_ta, dna_first)

    dna_chain = [dna_first, dna_second, tuple(dna_first)]
    dna_chain_2 = list(dna_chain)
    print(dna_chain, dna_chain_2, dna_chain == dna_chain_2, dna_chain is dna_chain_2)
    dna_chain[0][0] = 1 #container is different but the references inside are the same
    print(dna_chain, dna_chain_2, dna_chain == dna_chain_2, dna_chain is dna_chain_2)

    print(id(dna_chain_2), id(dna_chain))
    for x,y in zip(dna_chain, dna_chain_2):
        print(id(x), id(y))

    dna_chain[-1] += (1,) #tuple got mutated so a new one was created - no longer the same reference, is it still considered a shallow copy?
    print("\n", id(dna_chain_2), id(dna_chain))
    for x,y in zip(dna_chain, dna_chain_2):
        print(id(x), id(y))

    available_modes = {*dna_ta, *dna_gc}
    dna = DNAchain(dna_ta, dna_gc, available_modes)
    callback = weakref.finalize(available_modes, print, "Hello")
    callback_dna = weakref.finalize(dna, print, "Dna destructed")
    dna_shared = copy(dna)
    dna_backup = deepcopy(dna)
    dna.dna_segment.append("T")
    dna_shared.dna_segment.append("A")
    print(dna.dna_segment, dna_shared.dna_segment, dna_backup.dna_segment)
    #del dna

    l = dna_ta+dna_gc
    dna_gc.remove("C")
    print(l, dna_ta)
    print(id(dna_gc))
    print(id([*dna_gc]))

    print(weakref.getweakrefs(dna.dna_segment))
    print(weakref.getweakrefs(available_modes))
    
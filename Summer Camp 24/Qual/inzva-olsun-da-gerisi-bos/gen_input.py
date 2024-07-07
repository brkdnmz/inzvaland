import random
from string import ascii_lowercase

n = 100
q = 20
with open("input.txt", "w") as f:
    s = "sampletestcaseuretmekzorisneyazsambilemediminzvaolsundagerisiboskalpnediryacokuzunneyseneyseinzvaolsundagerisibossiyahkalpsiziseviyorumkucukturucsoruyuumarimcozersinizoptumbayiyieglencelerkedilerguzeldirerdemmezunolmadimidahabunuokuduysanizclarificationatinkamptasizehediyeveririm"
    n = len(s)
    # s = "".join(random.choices("inzvaolsundagerisiboskalp", k=n))
    f.write(f"{s}\n{q}\n")
    for _ in range(q - 1):
        t = random.randint(1, 2)
        f.write(f"{t} ")
        if t == 1:
            i = random.choice(range(1, n + 1))
            f.write(f"{i}\n")
        else:
            i, j = sorted(random.choices(range(1, n + 1), k=2))
            # i, j = 2, n - 1
            f.write(f"{i} {j}\n")
    f.write(f"2 1 {n}")

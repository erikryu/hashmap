nomes = [
    "Ana", "Maria", "Laura", "Sofia", "Alice",
    "Beatriz", "Helena", "Valentina", "Clara", "Isabel",
    "Lorena", "Gabriela", "Rafaela", "Marina", "Olivia",
    "Sara", "Carolina", "Camila", "Eduarda", "Yara",
    "Joana", "Bianca", "Nicole", "Daniela", "Emanuelly",
    "Melissa", "Kamilly", "Rebeca", "Stela", "Livia",
    "Pedro", "Lucas", "Gabriel", "Mateus", "Davi",
    "Miguel", "Arthur", "Bernardo", "Heitor", "Samuel",
    "Felipe", "Enzo", "Joao", "Guilherme", "Benicio",
    "Lorenzo", "Noah", "Isaac", "Daniel", "Henrique",
    "Murilo", "Elias", "Bryan", "Kevin", "Leandro",
    "Caua", "Vinicius", "Erick", "Otavio", "Thiago",
    "Bruno", "Diego", "Ricardo", "Fabio", "Roger",
    "Sandro", "William", "Leonardo", "Nathan", "Igor",
    "Renato", "Sergio", "Marcus", "Caio", "Raul",
    "Thomas", "Henry", "Alex", "Victor", "Hugo",
    "Ian", "Dario", "Elias", "Benjamim", "Martin",
    "Simon", "Paul", "David", "George", "Patrick",
    "Brian", "Alan", "Oliver", "Ryan", "Dylan",
    "Jason", "Kyle", "Brandon", "Justin", "Adrian"
]

def hsh_nome(nome: str) -> int:
    alfabeto = [
            'a', 'b', 'c', 'd', 'e', 
            'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 
            'z'
            ]

    hsh = 0;
    for l in nome.lower():
        ordem = alfabeto.index(l) + 1
        hsh = hsh + ordem

    return int(hsh/10)

hashes = [
        [], [], [], [], [], 
        [], [], [], [], []
        ]

for nome in nomes:
    hsh = hsh_nome(nome)
    if hsh >= 0 and hsh < 9:
        hashes[hsh].append([hsh, nome])
    
    if hsh > 9:
        hashes[0].append([hsh, nome])

for g in hashes:
    print(g, end='\n')

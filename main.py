from googlesearch import search

n = int(input("Quantos resultados exibir?: "))
t = str(input("Qual o termo de pesquisa?: "))

filter = ["Amazon", "Mercado", "Comprar", "comprar", "amazon", "mercado"]
a = 0

while (a != n+1):
    result = search(term=t, lang="pt-br", advanced=True, num_results=1)
    lresult = list(result)
    for i in lresult:
        for i2 in filter:
            if (i2 in i.title or i2 in i.description or i2 in i.url):
                break
            else:
                print(f"-----------------")
                print(f"{i.title}")
                print(f"{i.description}")
                print(f"{i.url}")
                print(f"-----------------")
                a += 1
                break

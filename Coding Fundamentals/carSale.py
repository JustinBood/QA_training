companies =['Ford Motor Company', 'Volkswagen UK', 'Mercedes-Benz UK', 'Vauxhall Motors', 'BMW'] 
diction = {0:[16629,10390,40755,18074,19892,22049,17049,10764], 1:[13224,7960,38335,15161,15737,20474,15183,11334], 2: [12249,6088,33536,11739,14431,14947,12056,5040], 3 : [12250,4905,37769,10639,13461,15540,10398,4864], 5 : [9553,6870,30330,10868,12415,19985,9198,4853]}




sale = open("carSale.txt", "w")

for x in range(len(companies)):
    sale.write(f"{companies[x]}: ")
    if x == 4:
        sale.write(f"{diction[5]}")
    elif x in diction:
        sale.write(f"{diction[x]}\n")



sale.close()
inp = [input('Enter AC'),(input('Enter attack')),(input('Enter number of attacks'))]

def hit(ac,bns,num):
    try:
        chance = round(((21-(ac-bns))/20)*100)
        newchance = [chance -x*25 for x in range(num)]
        for i,nmb in enumerate(newchance):
            if nmb < 5:
                newchance[i] = 5
            if nmb > 95:
                newchance[i] = 95
        return [str(str(newchance[x]) +'% chance to hit with attack number '+ str(x+1)) for x in range(num)]
    except ValueError:
        print('Only numbers please.')

print(hit(int(inp[0]),int(inp[1]),int(inp[2])))

liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def getPool(token1, token2):
    if token1 < token2:
        return liquidity[(token1, token2)]
    else:
        return liquidity[(token2, token1)][1], liquidity[(token2, token1)][0]

def swap(inVal, token1, token2, op = False):
    a, b = getPool(token1, token2)
    inVal *= 0.997
    prod = a * b
    new1 = a + inVal
    new2 = prod / new1
    outVal = b - new2
    if op:
        if token1 < token2:
            liquidity[(token1, token2)] = (new1, new2)
        else:
            liquidity[(token2, token1)] = (new2, new1)
    return outVal

def main():
    token = 'tokenB'
    val = 5
    tokenNames = {}
    for k in liquidity.keys():
        tokenNames[k[0]] = 0
        tokenNames[k[1]] = 0

    fin = False
    swapList = []
    
    while not fin:
        M = 0
        tup = ('','')
        for tk1 in tokenNames.keys():
            if tk1 == token:
                continue
            for tk2 in tokenNames.keys():
                if tk2 == token or tk2 == tk1:
                    continue
                temp = val
                temp = swap(temp, token, tk1)
                temp = swap(temp, tk1, tk2)
                temp = swap(temp, tk2, token)
                if temp > M:
                    M = temp
                    tup = (tk1, tk2)
        for tk1 in tokenNames.keys():
            if tk1 == token:
                continue
            for tk2 in tokenNames.keys():
                if tk2 == token or tk2 == tk1:
                    continue
                for tk3 in tokenNames.keys():
                    if tk3 == token or tk3 == tk2 or tk3 == tk1:
                        continue
                    temp = val
                    temp = swap(temp, token, tk1)
                    temp = swap(temp, tk1, tk2)
                    temp = swap(temp, tk2, tk3)
                    temp = swap(temp, tk3, token)
                    if temp > M:
                        M = temp
                        tup = (tk1, tk2, tk3)
        if M > val:
            for tk in tup:
                swapList.append(tk)
            swapList.append(token)
            cur = token
            for tk in tup:
                #print('swap from ' + cur + ' to ' + tk + ': ', end='')
                #print('amountIn = ' + str(val), end=', ')
                val = swap(val, cur, tk, True)
                #print('amountOut = ' + str(val))
                cur = tk
            #print('swap from ' + cur + ' to ' + token + ': ', end='')
            #print('amountIn = ' + str(val), end=', ')
            val = swap(val, cur, token, True)
            #print('amountOut = ' + str(val))
        else:
            fin = True

    i = 0
    while i+2 < len(swapList):
        if swapList[i] == swapList[i+2]:
            swapList.pop(i+1)
            swapList.pop(i+1)
        else:
            i += 1
    
    print('path: ' + token, end='')
    for tk in swapList:
        print('->' + tk, end = '')
    print(', ' + token + ' balance=' + str(val))

if __name__ == "__main__":
    main()
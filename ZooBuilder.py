herbCost, carniCost, aquaCost = map(int, input().split())
cost = [herbCost, carniCost, aquaCost]
herbArea, carniArea, aquaArea = map(int, input().split())
herb1, herb2 = map(int, input().split())
carni1, carni2 = map(int, input().split())
aqua1, aqua2 = map(int, input().split())
totalArea = int(input())
maxCost = max(cost)
minCost = min(cost)
if herbCost == maxCost:
    herbAreaReq = herb1*herb2
    if carniCost == minCost:
        carniAreaReq = carniArea
        aquaAreaReq = totalArea-carniAreaReq-herbAreaReq
    elif aquaCost == minCost:
        aquaAreaReq = aquaArea
        carniAreaReq = totalArea-aquaAreaReq-carniAreaReq
    totalCost = herbAreaReq*herbCost + carniAreaReq*carniCost + aquaAreaReq*aquaCost

if carniCost == maxCost:
    carniAreaReq = carni1*carni2
    if herbCost == minCost:
        herbAreaReq = herbArea
        aquaAreaReq = totalArea-carniAreaReq-herbAreaReq
    elif aquaCost == minCost:
        aquaAreaReq = aquaArea
        herbAreaReq = totalArea-aquaAreaReq-carniAreaReq
    totalCost = herbAreaReq*herbCost + carniAreaReq*carniCost + aquaAreaReq*aquaCost
if aquaCost == maxCost:
    aquaAreaReq = aqua1*aqua2
    if herbCost == minCost:
        herbAreaReq = herbArea
        carniAreaReq = totalArea-aquaAreaReq-herbAreaReq
    elif aquaCost == minCost:
        aquaAreaReq = aquaArea
        herbAreaReq = totalArea-aquaAreaReq-carniAreaReq
    totalCost = herbAreaReq*herbCost + carniAreaReq*carniCost + aquaAreaReq*aquaCost
print(totalCost)
print(bin(10)[2:].zfill(4))

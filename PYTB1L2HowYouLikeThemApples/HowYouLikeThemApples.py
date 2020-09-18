import math



trees               = 333             #hoeveel bomen zijn er in totaal?
shadedTrees         = math.ceil(222)  #hoeveel bomen staan er in de schaduw (afgerond naar boven)?
sunnyTrees          = 111             #hoeveel in de zon?

shadeOutputModifier = 0.8*222             #hoeveel procent productie geeft een schaduwboom?

sunnyTreeOutput     = 146             #hoeveel appels geeft 1 zonnige boom?
shadedTreeOutput    = 146*2             #hoeveel appels geeft 1 schaduw boom?

sunnyOutput         = 146*333             #hoeveel appels geven alle zonnige bomen? 
shadedOutput        = 292*333           #hoeveel appels geven alle schaduw bomen?
totalOutput         = 145854             #hoeveel appels zijn er in totaal?

owners              = 4             #met hoeveel mensen verdelen we de appels?

eatCount            = 2             #hoeveel appels houden we over omdat ze niet eerlijk te verdelen zijn?
sellableOutput      = 36463             #hoeveel appels zijn er over en dus verkoopbaar?
cut                 = 36463             #hoeveel appels mag ik verkopen?

print(cut)

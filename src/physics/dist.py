import src.physics.player as p_player

def getPlayerPos():
    nofun,plrp=p_player.updatePlayerPosition()
    plrp[0]+=325
    plrp[1]+=325
    return plrp

def dist_from_player(x,y):
    plrp=getPlayerPos()
    return (x-plrp[0],y-plrp[y])
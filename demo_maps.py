from map import Map
from units import *
from items import *

def build_demo1():
    demo1 = Map()
    demo1.add_unit(TahmKench(row=4, col=3, star_level=1, team=1))
    demo1.add_unit(TahmKench(row=4, col=4, star_level=1, team=1))
    demo1.add_unit(TahmKench(row=3, col=3, star_level=2, team=2))
    return demo1

def build_demo2():
    demo = Map()
    demo.add_unit(TahmKench(row=4, col=3, star_level=2, team=1))
    demo.add_unit(Vayne(row=7, col=4, star_level=1, team=1))
    demo.add_unit(Vayne(row=7, col=3, star_level=1, team=1))
    demo.add_unit(TahmKench(row=3, col=2, star_level=1, team=2))
    demo.add_unit(TahmKench(row=3, col=3, star_level=1, team=2))
    demo.add_unit(Vayne(row=0, col=3, star_level=2, team=2))
    return demo

def build_demo3():
    demo = Map()
    demo.add_unit(TahmKench(row=4, col=0, star_level=2, team=1))
    demo.add_unit(TahmKench(row=4, col=1, star_level=2, team=1))
    demo.add_unit(TahmKench(row=4, col=2, star_level=2, team=1))
    demo.add_unit(TahmKench(row=4, col=3, star_level=2, team=1))
    demo.add_unit(TahmKench(row=4, col=4, star_level=2, team=1))
    demo.add_unit(TahmKench(row=4, col=5, star_level=2, team=1))
    demo.add_unit(TahmKench(row=4, col=6, star_level=2, team=1))
    demo.add_unit(Vayne(row=7, col=2, star_level=1, team=1))
    demo.add_unit(Vayne(row=7, col=3, star_level=1, team=1))
    demo.add_unit(Vayne(row=7, col=4, star_level=1, team=1))
    demo.add_unit(Vayne(row=7, col=5, star_level=1, team=1))
    demo.add_unit(Vayne(row=7, col=5, star_level=1, team=1))
    demo.add_unit(TahmKench(row=3, col=0, star_level=1, team=2))
    demo.add_unit(TahmKench(row=3, col=1, star_level=1, team=2))
    demo.add_unit(TahmKench(row=3, col=2, star_level=1, team=2))
    demo.add_unit(TahmKench(row=3, col=3, star_level=1, team=2))
    demo.add_unit(TahmKench(row=3, col=4, star_level=1, team=2))
    demo.add_unit(TahmKench(row=3, col=5, star_level=1, team=2))
    demo.add_unit(TahmKench(row=3, col=6, star_level=1, team=2))
    demo.add_unit(Vayne(row=0, col=0, star_level=2, team=2))
    demo.add_unit(Vayne(row=0, col=1, star_level=2, team=2))
    demo.add_unit(Vayne(row=0, col=2, star_level=2, team=2))
    demo.add_unit(Vayne(row=0, col=3, star_level=2, team=2))
    demo.add_unit(Vayne(row=0, col=4, star_level=2, team=2))
    demo.add_unit(Vayne(row=0, col=5, star_level=2, team=2))
    demo.add_unit(Vayne(row=0, col=6, star_level=2, team=2))
    return demo


def build_demo4():
    demo = Map()
    demo.add_unit(TahmKench(row=4, col=4, star_level=1, team=1, items=[Rod(), BrambleVest(), DragonsClaw()]))
    demo.add_unit(Vayne(row=7, col=5, star_level=1, team=1, items=[Bow()]))
    demo.add_unit(Nami(row=7, col=6, star_level=2, team=1, items=[BlueBuff()]))
    demo.add_unit(Wukong(row=3, col=2, star_level=1, team=2, items=[Gloves()]))
    demo.add_unit(Wukong(row=3, col=4, star_level=1, team=2, items=[Cloak(), Belt()]))
    demo.add_unit(Vayne(row=0, col=3, star_level=2, team=2, items=[Deathblade()]))
    return demo


def build_demo5():
    demo = Map()
    demo.add_unit(TahmKench(row=3, col=2, star_level=2, team=2, items=[FrozenHeart()]))
    demo.add_unit(Vayne(row=0, col=1, star_level=1, team=2, items=[GiantSlayer()]))
    demo.add_unit(Vayne(row=0, col=0, star_level=1, team=2, items=[]))
    demo.add_unit(TahmKench(row=4, col=4, star_level=2, team=1, items=[FrozenHeart()]))
    demo.add_unit(Vayne(row=7, col=5, star_level=1, team=1, items=[GuinsooRageblade()]))
    demo.add_unit(Vayne(row=7, col=6, star_level=1, team=1, items=[]))
    return demo


def build_demo_isoteam():
    demo = Map()
    demo.add_unit(Vayne(row=0, col=1, star_level=1, team=2, items=[]))
    demo.add_unit(Vayne(row=0, col=2, star_level=1, team=1, items=[]))
    return demo


def build_demo51():
    demo = Map()
    demo.add_unit(Leona(row=3, col=2, star_level=2, team=2, items=[]))
    demo.add_unit(Ziggs(row=0, col=1, star_level=1, team=2, items=[JeweledGauntlet()]))
    demo.add_unit(Gragas(row=2, col=3, star_level=1, team=2, items=[Belt()]))
    demo.add_unit(Aatrox(row=4, col=5, star_level=2, team=1, items=[BrambleVest()]))
    demo.add_unit(Vladimir(row=4, col=6, star_level=1, team=1, items=[]))
    demo.add_unit(Vayne(row=7, col=6, star_level=1, team=1, items=[RunaansHurricane()]))
    return demo


def build_demo52():
    demo = Map()
    demo.add_unit(Zyra(row=0, col=1, star_level=2, team=2, items=[BlueBuff()]))
    demo.add_unit(Diana(row=3, col=5, star_level=2, team=2, items=[RadiantWarmogsArmor()]))
    demo.add_unit(Velkoz(row=1, col=5, star_level=1, team=2, items=[RadiantSpearOfShojin()]))
    demo.add_unit(Viego(row=1, col=5, star_level=1, team=2, items=[BlueBuff()]))
    demo.add_unit(Sett(row=4, col=1, star_level=2, team=1, items=[]))
    demo.add_unit(Rell(row=4, col=3, star_level=1, team=1, items=[SpearOfShojin()]))
    demo.add_unit(Nidalee(row=7, col=3, star_level=2, team=1, items=[Rod()]))
    demo.add_unit(Vayne(row=7, col=5, star_level=2, team=1, items=[BF()]))
    demo.add_unit(Vayne(row=7, col=6, star_level=2, team=1, items=[Bow()]))
    demo.add_unit(Vayne(row=7, col=4, star_level=2, team=1, items=[Belt()]))
    return demo


def build_demo53():
    demo = Map()
    demo.add_unit(Ivern(row=3, col=6, star_level=2, team=2, items=[]))
    demo.add_unit(Fiddlesticks(row=3, col=3, star_level=2, team=2, items=[]))
    demo.add_unit(Volibear(row=3, col=1, star_level=2, team=2, items=[]))
    demo.add_unit(Pyke(row=1, col=6, star_level=2, team=2, items=[]))
    demo.add_unit(Diana(row=0, col=5, star_level=2, team=2, items=[FrozenHeart()]))
    demo.add_unit(Nocturne(row=0, col=3, star_level=3, team=2, items=[InfinityEdge(), LastWhisper(), RadiantRunaansHurricane()]))
    demo.add_unit(Viego(row=0, col=0, star_level=2, team=2, items=[BlueBuff()]))

    demo.add_unit(Ivern(row=4, col=1, star_level=2, team=1, items=[]))
    demo.add_unit(Fiddlesticks(row=4, col=3, star_level=2, team=1, items=[]))
    demo.add_unit(Volibear(row=4, col=5, star_level=2, team=1, items=[]))
    demo.add_unit(Pyke(row=6, col=0, star_level=2, team=1, items=[]))
    demo.add_unit(Diana(row=7, col=1, star_level=2, team=1, items=[FrozenHeart()]))
    demo.add_unit(Nocturne(row=7, col=3, star_level=2, team=1, items=[InfinityEdge(), LastWhisper(), RadiantRunaansHurricane()]))
    demo.add_unit(Viego(row=7, col=6, star_level=2, team=1, items=[BlueBuff()]))
    return demo

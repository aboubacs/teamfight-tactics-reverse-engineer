# skipped:
# kalista (projectile)
# kled (shield)
# lissandra (projectile)
# warwick (state)
# udyr (shield)
# brand (shred + unowned tick)
# kennen (move ability)
# sett (non circular aoe + shred)
# soraka (new effect)
# syndra (move ability)
# thresh (move ability)
# trundle (to research)
# varus (on hit effect)
# ashe (projectile)
# katarina (move ability)
# lux (projectile)

from .unit import Unit

from .set45.garen import Garen
from .set45.tahm_kench import TahmKench
from .set45.vayne import Vayne as Vayne45
from .set45.wukong import Wukong
from .set45.nami import Nami

from .set5.aatrox import Aatrox
from .set5.leona import Leona
from .set5.gragas import Gragas
from .set5.khazix import Khazix  # miss innate assassin
from .set5.vayne import Vayne
from .set5.kalista import Kalista
from .set5.senna import Senna
from .set5.brand import Brand
from .set5.vladimir import Vladimir
from .set5.ziggs import Ziggs
from .set5.poppy import Poppy  # manalock ?
from .set5.nautilus import Nautilus
from .set5.sejuani import Sejuani
from .set5.viktor import Viktor
from .set5.lee_sin import LeeSin
from .set5.lulu import Lulu
from .set5.syndra import Syndra
from .set5.nunu import Nunu
from .set5.riven import Riven
from .set5.jax import Jax
from .set5.olaf import Olaf
from .set5.kled import Kled
from .set5.udyr import Udyr
from .set5.tristana import Tristana
from .set5.hecarim import Hecarim
from .set5.irelia import Irelia
from .set5.soraka import Soraka
from .set5.varus import Varus
from .set5.thresh import Thresh
from .set5.yasuo import Yasuo
from .set5.ashe import Ashe
from .set5.rakan import Rakan
from .set5.zyra import Zyra
from .set5.pyke import Pyke
from .set5.kennen import Kennen
from .set5.sett import Sett
from .set5.nocturne import Nocturne
from .set5.monstrosity import Monstrosity
from .set5.miss_fortune import MissFortune
from .set5.nidalee import Nidalee
from .set5.lux import Lux
from .set5.aphelios import Aphelios
from .set5.draven import Draven
from .set5.diana import Diana
from .set5.fiddlesticks import Fiddlesticks
from .set5.galio import Galio
from .set5.karma import Karma
from .set5.garen import Garen
from .set5.volibear import Volibear
from .set5.ivern import Ivern
from .set5.daisy import Daisy
from .set5.rell import Rell
from .set5.velkoz import Velkoz
from .set5.viego import Viego
from .set5.voidspawn import Voidspawn

UNIT_STR_TO_CLS = {
    'gragas': Gragas,
    'aatrox': Aatrox,
    'leona': Leona,
    'khazix': Khazix,
    'vayne': Vayne,
    'vladimir': Vladimir,
    'ziggs': Ziggs,
    'poppy': Poppy,
    'nautilus': Nautilus,
    'sejuani': Sejuani,
    'hecarim': Hecarim,
    'lee_sin': LeeSin,
    'lulu': Lulu,
    'syndra': Syndra,
    'nunu': Nunu,
    'riven': Riven,
    'jax': Jax,
    'olaf': Olaf,
    'kled': Kled,
    'udyr': Udyr,
    'kalista': Kalista,
    'senna': Senna,
    'brand': Brand,
    'tristana': Tristana,
    'irelia': Irelia,
    'soraka': Soraka,
    'varus': Varus,
    'thresh': Thresh,
    'yasuo': Yasuo,
    'ashe': Ashe,
    'rakan': Rakan,
    'zyra': Zyra,
    'pyke': Pyke,
    'kennen': Kennen,
    'sett': Sett,
    'nocturne': Nocturne,
    'monstrosity': Monstrosity,
    'miss_fortune': MissFortune,
    'nidalee': Nidalee,
    'lux': Lux,
    'aphelios': Aphelios,
    'draven': Draven,
    'diana': Diana,
    'fiddlesticks': Fiddlesticks,
    'galio': Galio,
    'karma': Karma,
    'garen': Garen,
    'volibear': Volibear,
    'ivern': Ivern,
    'daisy': Daisy,
    'rell': Rell,
    'velkoz': Velkoz,
    'viego': Viego,
    'voidspawn': Voidspawn,
}
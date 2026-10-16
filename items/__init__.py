# skiped:
# Thieves gloves (no table available)
# zzrot (stage issue)

from .item import Item
from .components.bow import Bow
from .components.tear import Tear
from .components.bf import BF
from .components.rod import Rod
from .components.vest import Vest
from .components.cloak import Cloak
from .components.belt import Belt
from .components.gloves import Gloves
from .full_items.archangels_staff import ArchangelsStaff
from .full_items.banshees_claw import BansheesClaw
from .full_items.bloodthirster import BloodThirster
from .full_items.blue_buff import BlueBuff
from .full_items.bramble_vest import BrambleVest
from .full_items.chalice import Chalice
from .full_items.deathblade import Deathblade
from .full_items.dragons_claw import DragonsClaw
from .full_items.frozen_heart import FrozenHeart
from .full_items.gargoyle_stoneplate import GargoyleStoneplate
from .full_items.guardian_angel import GuardianAngel
from .full_items.giant_slayer import GiantSlayer
from .full_items.guinsoo_rageblade import GuinsooRageblade
from .full_items.hand_of_justice import HandOfJustice
from .full_items.hextech_gunblade import HextechGunblade
from .full_items.infinity_edge import InfinityEdge
from .full_items.ionic_spark import IonicSpark
from .full_items.jeweled_gauntlet import JeweledGauntlet
from .full_items.last_whisper import LastWhisper
from .full_items.locket_of_the_iron_solari import LocketOfTheIronSolari
from .full_items.morellonomicon import Morellonomicon
from .full_items.quicksilver import Quicksilver
from .full_items.rabadons_deathcap import RadabonsDeathcap
from .full_items.rapid_firecannon import RapidFirecannon
from .full_items.redemption import Redemption
from .full_items.runaans_hurricane import RunaansHurricane
from .full_items.shroud_of_stillness import ShroudOfStillness
from .full_items.spear_of_shojin import SpearOfShojin
from .full_items.statikk_shiv import StatikkShiv
from .full_items.sunfire_cape import SunfireCape
from .full_items.titans_resolve import TitansResolve
from .full_items.warmogs_armor import WarmogsArmor
from .full_items.zekes_herald import ZekesHerald
from .full_items.zephyr import Zephyr
from .full_items.zzrot_portal import ZzrotPortal
from .full_items.radiant_archangels_staff import RadiantArchangelsStaff
from .full_items.radiant_banshees_claw import RadiantBansheesClaw
from .full_items.radiant_bloodthirster import RadiantBloodThirster
from .full_items.radiant_blue_buff import RadiantBlueBuff
from .full_items.radiant_bramble_vest import RadiantBrambleVest
from .full_items.radiant_chalice import RadiantChalice
from .full_items.radiant_deathblade import RadiantDeathblade
from .full_items.radiant_dragons_claw import RadiantDragonsClaw
from .full_items.radiant_frozen_heart import RadiantFrozenHeart
from .full_items.radiant_gargoyle_stoneplate import RadiantGargoyleStoneplate
from .full_items.radiant_giant_slayer import RadiantGiantSlayer
from .full_items.radiant_guardian_angel import RadiantGuardianAngel
from .full_items.radiant_guinsoo_rageblade import RadiantGuinsooRageblade
from .full_items.radiant_hand_of_justice import RadiantHandOfJustice
from .full_items.radiant_hextech_gunblade import RadiantHextechGunblade
from .full_items.radiant_infinity_edge import RadiantInfinityEdge
from .full_items.radiant_ionic_spark import RadiantIonicSpark
from .full_items.radiant_jeweled_gauntlet import RadiantJeweledGauntlet
from .full_items.radiant_last_whisper import RadiantLastWhisper
from .full_items.radiant_locket_of_the_iron_solari import RadiantLocketOfTheIronSolari
from .full_items.radiant_morellonomicon import RadiantMorellonomicon
from .full_items.radiant_quicksilver import RadiantQuicksilver
from .full_items.radiant_rabadons_deathcap import RadiantRadabonsDeathcap
from .full_items.radiant_rapid_firecannon import RadiantRapidFirecannon
from .full_items.radiant_redemption import RadiantRedemption
from .full_items.radiant_runaans_hurricane import RadiantRunaansHurricane
from .full_items.radiant_shroud_of_stillness import RadiantShroudOfStillness
from .full_items.radiant_spear_of_shojin import RadiantSpearOfShojin
from .full_items.radiant_sunfire_cape import RadiantSunfireCape
from .full_items.radiant_statikk_shiv import RadiantStatikkShiv
from .full_items.radiant_titans_resolve import RadiantTitansResolve
from .full_items.radiant_warmogs_armor import RadiantWarmogsArmor
from .full_items.radiant_zekes_herald import RadiantZekesHerald
from .full_items.radiant_zephyr import RadiantZephyr

ITEM_STR_TO_CLS = {
	'bow': Bow,
	'tear': Tear,
	'bf': BF,
	'rod': Rod,
	'vest': Vest,
	'cloak': Cloak,
	'belt': Belt,
	'gloves': Gloves,
	'archangels_staff': ArchangelsStaff,
	'banshees_claw': BansheesClaw,
	'bloodthirster': BloodThirster,
	'blue_buff': BlueBuff,
	'bramble_vest': BrambleVest,
	'chalice': Chalice,
	'deathblade': Deathblade,
	'dragons_claw': DragonsClaw,
	'frozen_heart': FrozenHeart,
	'gargoyle_stoneplate': GargoyleStoneplate,
	'giant_slayer': GiantSlayer,
	'guardian_angel': GuardianAngel,
	'guinsoo_rageblade': GuinsooRageblade,
	'hand_of_justice': HandOfJustice,
	'hextech_gunblade': HextechGunblade,
	'infinity_edge': InfinityEdge,
	'ionic_spark': IonicSpark,
	'jeweled_gauntlet': JeweledGauntlet,
	'last_whisper': LastWhisper,
	'locket_of_the_iron_solari': LocketOfTheIronSolari,
	'morellonomicon': Morellonomicon,
	'quicksilver': Quicksilver,
	'rabadons_deathcap': RadabonsDeathcap,
	'rapid_firecannon': RapidFirecannon,
	'redemption': Redemption,
	'runaans_hurricane': RunaansHurricane,
	'shroud_of_stillness': ShroudOfStillness,
	'spear_of_shojin': SpearOfShojin,
	'sunfire_cape': SunfireCape,
	'statikk_shiv': StatikkShiv,
	'titans_resolve': TitansResolve,
	'warmogs_armor': WarmogsArmor,
	'zekes_herald': ZekesHerald,
	'zephyr': Zephyr,
	'zzrot_portal': ZzrotPortal,
	'radiant_archangels_staff': RadiantArchangelsStaff,
	'radiant_banshees_claw': RadiantBansheesClaw,
	'radiant_bloodthirster': RadiantBloodThirster,
	'radiant_blue_buff': RadiantBlueBuff,
	'radiant_bramble_vest': RadiantBrambleVest,
	'radiant_chalice': RadiantChalice,
	'radiant_deathblade': RadiantDeathblade,
	'radiant_dragons_claw': RadiantDragonsClaw,
	'radiant_frozen_heart': RadiantFrozenHeart,
	'radiant_gargoyle_stoneplate': RadiantGargoyleStoneplate,
	'radiant_giant_slayer': RadiantGiantSlayer,
	'radiant_guardian_angel': RadiantGuardianAngel,
	'radiant_guinsoos_rageblade': RadiantGuinsooRageblade,
	'radiant_hand_of_justice': RadiantHandOfJustice,
	'radiant_hextech_gunblade': RadiantHextechGunblade,
	'radiant_infinity_edge': RadiantInfinityEdge,
	'radiant_ionic_spark': RadiantIonicSpark,
	'radiant_jeweled_gauntlet': RadiantJeweledGauntlet,
	'radiant_last_whisper': RadiantLastWhisper,
	'radiant_locket_of_the_iron_solari': RadiantLocketOfTheIronSolari,
	'radiant_morellonomicon': RadiantMorellonomicon,
	'radiant_quicksilver': RadiantQuicksilver,
	'radiant_rabadons_deathcap': RadiantRadabonsDeathcap,
	'radiant_rapid_firecannon': RadiantRapidFirecannon,
	'radiant_redemption': RadiantRedemption,
	'radiant_runaans_hurricane': RadiantRunaansHurricane,
	'radiant_shroud_of_stillness': RadiantShroudOfStillness,
	'radiant_spear_of_shojin': RadiantSpearOfShojin,
	'radiant_sunfire_cape': RadiantSunfireCape,
	'radiant_statikk_shiv': RadiantStatikkShiv,
	'radiant_titans_resolve': RadiantTitansResolve,
	'radiant_warmogs_armor': RadiantWarmogsArmor,
	'radiant_zekes_herald': RadiantZekesHerald,
	'radiant_zephyr': RadiantZephyr,
}
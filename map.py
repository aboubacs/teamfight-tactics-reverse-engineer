import pygame
import utils
import json
import random
import uuid
from tile import Tile
from units import *
from items import *
from synergies import *

hexagon = pygame.image.load('./images/hexagon.png')
hexagon = pygame.transform.smoothscale(hexagon, (80, 80))

class Map:
    def __init__(self):
        self.tiles = [
            [Tile() for _ in range(7)]
            for _ in range(8)
        ]
        self.ticked = False
        self.units = []
        self.projectiles = []
        self.game_log = []
        self.synergies_team1 = []
        self.synergies_team2 = []
        self.deaths_team1 = 0
        self.deaths_team2 = 0
        self._TIME = 0

    @classmethod
    def from_boards(cls, board1, board2):
        map = cls()
        board1_data = json.loads(board1['board_data'])
        board2_data = json.loads(board2['board_data'])
        for row_id, row in enumerate(board1_data):
            for col_id, cell in enumerate(row):
                if cell and 'name' in cell:
                    unit_cls = UNIT_STR_TO_CLS[cell['name']]
                    unit = unit_cls(row=3-row_id, col=6-col_id, star_level=cell['starLevel'], team=1, forgotten_stacks=cell.get('forgottenStacks', 0))
                    for item_name in cell['items']:
                        if item_name:
                            unit.items.append(ITEM_STR_TO_CLS[item_name]())
                    map.add_unit(unit)
        for row_id, row in enumerate(board2_data):
            for col_id, cell in enumerate(row):
                if cell and 'name' in cell:
                    unit_cls = UNIT_STR_TO_CLS[cell['name']]
                    unit = unit_cls(row=row_id+4, col=col_id, star_level=cell['starLevel'], team=2, forgotten_stacks=cell.get('forgottenStacks', 0))
                    for item_name in cell['items']:
                        if item_name:
                            unit.items.append(ITEM_STR_TO_CLS[item_name]())
                    map.add_unit(unit)

        return map

    @property
    def winner(self):
        if not self.units:
            return 3
        if all(u.team == 2 for u in self.units):
            return 2
        if all(u.team == 1 for u in self.units):
            return 1

    def create_synergies(self):
        for synergy_cls in ALL_SYNERGIES:
            units_team1 = [u for u in self.units if u.team == 1]
            units_team2 = [u for u in self.units if u.team == 2]
            if synergy_cls.is_active(units_team1):
                # print(synergy_cls, 'active at', synergy_cls.get_active_step(units_team1), 'for team 1')
                if synergy_cls == Abomination:
                    syn = synergy_cls(synergy_cls.get_active_step(units_team1), monstrosity_cls=Monstrosity)
                else:
                    syn = synergy_cls(synergy_cls.get_active_step(units_team1))
                self.synergies_team1.append(syn)
            if synergy_cls.is_active(units_team2):
                # print(synergy_cls, 'active at', synergy_cls.get_active_step(units_team2), 'for team 2')
                if synergy_cls == Abomination:
                    syn = synergy_cls(synergy_cls.get_active_step(units_team2), monstrosity_cls=Monstrosity)
                else:
                    syn = synergy_cls(synergy_cls.get_active_step(units_team2))
                self.synergies_team2.append(syn)

    def spawn_unit(self, unit):
        self.units.append(unit)
        if unit.team == 1:
            for synergy in self.synergies_team1:
                synergy.apply_on_unit_spawn(unit)
        elif unit.team == 2:
            for synergy in self.synergies_team2:
                synergy.apply_on_unit_spawn(unit)

    def on_spell_cast(self, unit):
        for u in self.units:
            if u.spellweaver_ap_gain_per_cast > 0 and u.spellweaver_stacks < 10:
                u.spellweaver_stacks += 1
                u.flat_bonus_spell_power_modifiers.add_component(uuid.uuid4(), unit._TIME, 9999, u.spellweaver_ap_gain_per_cast)
            if u.team != unit.team:
                for item in u.items:
                    zap_value = item.get_zap_mana_percentage_value()
                    if zap_value and u.distance(unit.row, unit.col) <= item.range:
                        u.deal_magic_damage(unit, unit.get_effective_total_mana() * zap_value / 100)

    def draw(self, screen, time):
        for i, tile_row in enumerate(self.tiles):
            for j, tile in enumerate(tile_row):
                screen.blit(hexagon, utils.xy_pos_from_ij_tile(i, j))

        for unit in self.units:
            unit.draw(screen, time)

        for unit in self.units:
            unit.draw2(screen, time)

        for projectile in self.projectiles:
            projectile.draw(screen, time)

    def unit_at(self, row, col):
        for unit in self.units:
            if unit.row == row and unit.col == col:
                return unit
        return None

    def is_tile_empty(self, row, col):
        return self.unit_at(row, col) is None or self.unit_at(row, col).is_dead

    def play(self, log):
        time = 0
        while not self.winner in (1, 2, 3):
            self.tick(time, log=log)
            time += 0.01

    def tick(self, time, log=False):
        self._TIME = time
        if not self.ticked:
            for unit in self.units:
                unit.trigger_items_add(self)
            self.create_synergies()
            for synergy in self.synergies_team1:
                synergy.on_start_fight([u for u in self.units if u.team == 1])
                for u in self.units:
                    if u.team == 1:
                        synergy.apply_on_unit_spawn(u)
            for synergy in self.synergies_team2:
                synergy.on_start_fight([u for u in self.units if u.team == 2])
                for u in self.units:
                    if u.team == 2:
                        synergy.apply_on_unit_spawn(u)

        self.ticked = True

        for synergy in self.synergies_team1:
            synergy.tick(time, [u for u in self.units if u.team == 1])
        for synergy in self.synergies_team2:
            synergy.tick(time, [u for u in self.units if u.team == 2])

        random.shuffle(self.units)
        for projectile in self.projectiles:
            projectile.tick(time)

        for unit in self.units:
            unit.tick(self, time)

        for unit in self.units:
            if unit.health <= 0 and not unit.is_under_revive:
                unit.die(time)
                if unit.is_dead:
                    if unit.team == 1:
                        self.deaths_team1 += 1
                        for synergy in self.synergies_team1:
                            synergy.on_death(self, time, self.deaths_team1)
                    else:
                        self.deaths_team2 += 1
                        for synergy in self.synergies_team2:
                            synergy.on_death(self, time, self.deaths_team2)

                    for f in self.units:
                        f.fiddle_crowstorm_extend(unit)
        self.units = [u for u in self.units if u.health > 0 or u.is_under_revive]

        for p in self.projectiles:
            if p.destroyed:
                p.on_destroy(self, time)
        self.projectiles = [p for p in self.projectiles if not p.destroyed]

        if log and (int(time * 100) % 10 == 0 or self.winner):
            self.log(time)

    def log(self, time):
        self.game_log.append({
            'time': time,
            'data': {
                'units': [unit.to_log_json() for unit in self.units],
                'projectiles': [projectile.to_log_json(time) for projectile in self.projectiles],
            }
        })

    def add_unit(self, unit):
        self.units.append(unit)
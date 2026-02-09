from .EliteCard import EliteCard
print("=== DataDeck Ability System ===\n")


elite = EliteCard("Arcane Warrior", 4, "melee")

print("EliteCard capabilities:")

print(
    "- Card: ['play', 'get_card_info', 'is_playable']"
    )

print("- Combatable:", [
    "attack", "defend", "get_combat_stats"
])

print("- Magical:", [
    "cast_spell", "channel_mana", "get_magic_stats"
])

print("\nPlaying Arcane Warrior (Elite Card):")

print("\nCombat phase:")
attack_result = elite.attack("Enemy")
print("Attack result:", attack_result)

defense_result = elite.defend(5)
print("Defense result:", defense_result)

print("\nMagic phase:")
spell_result = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
print("Spell cast:", spell_result)

mana_result = elite.channel_mana(7)
print("Mana channel:", mana_result)

print("\nMultiple interface implementation successful!")
print(elite.get_combat_stats())
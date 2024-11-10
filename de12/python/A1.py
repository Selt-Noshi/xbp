import random

list1 = [
    "100-神", "90-魔王", "80-精霊王", "70-天使", "60-悪魔", "80-巨人", "70-精霊", 
    "60-大魔法使い", "50-人間", "40-亜人", "80-自動販売機", "70-カレーライス", 
    "60-電車", "50-PS5", "40-AirPods"
]
list2 = [
    "150-道用先生の加護", "140-Xbusinessの力", "130-メガサイズのカレーライスの加護", 
    "120-エレメントの加護", "110-人類の意志の加護", "100-地球の加護", "1-Noshiの加護"
]
list3 = [
    "5-UR", "4-SSR", "3-SR", "2-R", "1-N"
]

def extract_value(item):
    try:
        parts = item.split('-')
        if parts[0].strip() == "":
            raise ValueError(f"wrong num: '{item}'")
        return int(parts[0].strip())
    except (ValueError, IndexError):
        print(f"warn '{item}' wrong num")
        return 0 

# 1. 
num_people = int(input("参加人数を入力してください: "))

# 2. 
participants = {}

# 3. 
for i in range(num_people):
    name = input(f" {i+1} 名前を入力してください: ")
    weapon = input(f" {name} 武器を入力してください: ")
    
    # 種族
    race_draw = random.choice(list1)
    race_value = extract_value(race_draw) 
    race_name = race_draw.split('-')[1] if '-' in race_draw else "？？？"

    # 加護
    blessing_draw = random.choice(list2)
    blessing_value = extract_value(blessing_draw)
    blessing_name = blessing_draw.split('-')[1] if '-' in blessing_draw else "？？？"

    # 資質
    potential_draw = random.choice(list3)
    potential_value = extract_value(potential_draw) 
    potential_name = potential_draw.split('-')[1] if '-' in potential_draw else "？？？"

    # 戦闘力
    power = (race_value + blessing_value) * potential_value

    # 結果
    participants[name] = {
        'weapon': weapon,
        'race': race_name,
        'race_value': race_value,
        'blessing': blessing_name,
        'blessing_value': blessing_value,
        'potential': potential_name,
        'potential_value': potential_value,
        'power': power
    }

# プリント
print("\nみんなの結果:")
for name, details in participants.items():
    print(f"{name}，あなたの種族は {details['race']}，あなたの加護は{details['blessing']}，あなたの資質は {details['potential']}。")
    print(f"戦闘力: {details['power']}")

# 4. 
names = list(participants.keys())
random.shuffle(names)

print("\n战斗结果:")

while len(names) > 1:
    # 
    fighter1 = names.pop()
    fighter2 = names.pop()

    # 
    power1 = participants[fighter1]['power']
    power2 = participants[fighter2]['power']

    if power1 > power2:
        winner = fighter1
        loser = fighter2
    else:
        winner = fighter2
        loser = fighter1

    # 結果
    print(f"{winner} は {participants[winner]['weapon']} を使用して {loser}を倒した！！！")

    # 
    names.insert(0, winner)

# 最终胜者
print(f"\n勝利者は{names[0]}！")

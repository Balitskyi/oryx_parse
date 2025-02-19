import requests
import re
from bs4 import BeautifulSoup
from datetime import date, timedelta
import sys

today = date.today().strftime('%d-%m-%Y')
yesterday = (date.today() - timedelta(days=1)).strftime('%d-%m-%Y')
#some_day = '07-09-2023'


# Зчитайте значення для some_day з аргументів командного рядка або використайте значення за замовчуванням
if len(sys.argv) > 1:
    some_day = sys.argv[1]
else:
    some_day = '18-08-2024'

def rus_losses():
    url = 'https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html'
    response = requests.get(url)
    response.text

    soup = BeautifulSoup(response.text, 'html.parser')

    # Отримання тексту таблиці з втратами
    text = soup.find('div', class_='post-body entry-content').get_text()

    # Видалення зайвих елементів з тексту
    loses = re.sub(r'[\xa0\n]|Special thanks to[\s\S]*$', '', text[text.index(
        "(Click on the numbers to get a picture of each individual captured or destroyed vehicle)") + len(
        "(Click on the numbers to get a picture of each individual captured or destroyed vehicle)"):]).strip()

    total_loses = re.findall(r' - (.*?)Tanks', loses, flags=re.DOTALL | re.MULTILINE)[0].strip()
    total_loses = re.sub(r'which:', 'which', total_loses)
    vehicles = "Tanks " + re.findall(r'(?<=\dTanks\b)(.*$)', loses, flags=re.DOTALL | re.MULTILINE)[0].strip()
    # нижній рядок забирає з виводу дуже класну напоминалку про розмочений рахунок по підводним субмаринах, в пітон ОБОВ'ЯЗКОВО це треба буде вернути
    vehicles = re.sub(r'\sand\sSubmarines', '', vehicles)
        
    if ") 1R-325BMVjamming" in vehicles:
        vehicles = re.sub(r'\)\s1R-325BMVjamming', ') 1 R-325BMV jamming', vehicles)
    vehicles = re.sub(r'(\))(\d+)(BMPT)', r'\1 \2 \3', vehicles)
    vehicles = re.sub(r'(\))(\d+)(T-\d+)', r'\1 \2 \3', vehicles)
    vehicles = re.sub(r'Vehicles\(', 'Vehicles (', vehicles)
    vehicles = re.sub(r'(\))(\d+)(Uran-6)', r'\1 \2 \3', vehicles)
    vehicles = re.sub(r'(\))(\d+)(BPM-97)', r'\1 \2 \3', vehicles)


    def summary_losses():
        tanks_summary = re.findall(r'^(.*?)(?=\d+\sT-\d+)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip()
        afv_summary = re.findall(r'^(.*?)(?=\d+\sBMPT\s)', 'Armoured ' + re.findall(r'(?<=Armoured\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        ifv_summary = re.findall(r'^(.*?)(?=\d+\sBMP.)', 'Infantry ' + re.findall(r'(?<=Infantry\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        apc_summary = re.findall(r'^(.*?)(?=\d+\sBTR-)', 'Armoured Personnel ' + re.findall(r'(?<=Armoured\sPersonnel\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        mrap_summary = re.findall(r'^(.*?)(?=\d+\sKamAZ.\d{5})', 'Mine-' + re.findall(r'(?<=Mine.)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        mrap_summary = re.sub(r'\(MRAP\)', 'MRAP', mrap_summary)
        imv_summary = re.findall(r'^(.*?)(?=\d+\sBPM)', 'Infantry Mobility ' + re.findall(r'(?<=Infantry\sMobility\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        cpacs_summary = re.findall(r'^(.*?)(?=\d+\sBMP.\dKSh)', 'Command ' + re.findall(r'(?<=Command\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        evae_summary = re.findall(r'^(.*?)(?=\d+\sUR.)', 'Engineering ' + re.findall(r'(?<=Engineering\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        ugv_summary = re.findall(r'^(.*?)(?=\d+\sUran)', 'Unmanned Ground ' + re.findall(r'(?<=Unmanned Ground\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        spatms_summary = re.findall(r'^(.*?)(?=\d+\s9P148)', 'Self-Propelled Anti-Tank ' + re.findall(r'(?<=Self-Propelled Anti-Tank\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        asvae_summary = re.findall(r'^(.*?)(?=1V110)', 'Artillery Support ' + re.findall(r'(?<=Artillery Support\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        ta_summary = re.findall(r'^(.*?)(?=\d+\s82mm)', 'Towed ' + re.findall(r'(?<=Towed\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        spa_summary = re.findall(r'^(.*?)(?=\d+\s120mm)', 'Self-Propelled Artillery ' + re.findall(r'(?<=Self-Propelled Artillery\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        mrls_summary = re.findall(r'^(.*?)(?=\d+\s122mm)', 'Multiple ' + re.findall(r'(?<=Multiple\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        aag_summary = re.findall(r'^(.*?)(?=\d+\s23mm)', 'Anti-Aircraft ' + re.findall(r'(?<=Anti-Aircraft\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        spaag_summary = re.findall(r'^(.*?)(?=\d+\sBTR-ZD Skrezhet)', 'Self-Propelled Anti-Aircraft ' + re.findall(r'(?<=Self-Propelled Anti-Aircraft\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        stams_summary =re.findall(r'^(.*?)(?=\d+\s9K33 Osa)', 'Surface-To-Air ' + re.findall(r'(?<=Surface-To-Air\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        radars_summary = re.findall(r'^(.*?)(?=\d+\s9S36)', 'Radars ' + re.findall(r'(?<=Radars\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        jads_summary = re.findall(r'^(.*?)(?=\d+\sR-325BMV)', 'Jammers ' + re.findall(r'(?<=Jammers\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        aircraft_summary = re.findall(r'^(.*?)(?=\d+\sMiG)', 'Aircraft (' + re.findall(r'(?<=Aircraft\s.\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        helicopters_summary = re.findall(r'^(.*?)(?=\d+\sMi-8)', 'Helicopters ' + re.findall(r'(?<=Helicopters\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        ucav_summary = re.findall(r'^(.*?)(?=\d+\sOrion)', 'Unmanned Combat ' + re.findall(r'(?<=Unmanned Combat\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        rcav_summary = re.findall(r'^(.*?)(?=\d+\sForpost)', 'Reconnaissance  ' + re.findall(r'(?<=Reconnaissance\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        navalships_summary = re.findall(r'^(.*?)(?=\d+\sProject\s1164)', 'Naval  ' + re.findall(r'(?<=Naval\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        trucks_summary = re.findall(r'^(.*?)(?=\d+\sGAZ-51)', 'Trucks' + re.findall(r'(?<=Trucks\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()

        total = 'Total vehicle losses of russia (' + total_loses + ')' + '\n' + tanks_summary + '\n' + afv_summary + '\n' + ifv_summary + '\n' + apc_summary + '\n' + mrap_summary + '\n' + imv_summary + '\n' + cpacs_summary + '\n' + evae_summary + '\n' + ugv_summary + '\n' + spatms_summary + '\n' + asvae_summary + '\n' + ta_summary + '\n' + spa_summary + '\n' + mrls_summary + '\n' + aag_summary + '\n' + spaag_summary + '\n' + stams_summary + '\n' + radars_summary + '\n' + jads_summary + '\n' + aircraft_summary + '\n' + helicopters_summary + '\n' + ucav_summary + '\n' + rcav_summary + '\n' + navalships_summary + '\n' + trucks_summary
        total = re.sub(r'\sof\swhich', '', total)
        total = re.sub(r'^(?!.*damaged.*$).*destroyed:\s\d+', r'\g<0>, damaged: 0', total, flags=re.MULTILINE)
        total = re.sub(r'^(?!.*abandoned.*$).*damaged:\s\d+', r'\g<0>, abandoned: 0', total, flags=re.MULTILINE)
        total = re.sub(r'^(?!.*captured.*$).*abandoned:\s\d+', r'\g<0>, captured: 0', total, flags=re.MULTILINE)

        return (total)


    def cleaning_data():
        clean_data = re.findall(r'^(.*?)(?=\d+\s\w.\w{2}\s)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip() + ' ' + re.sub(r'ed\)', r'ed) ', re.search(r'(?=\d+\s\w.\w{2}\s)(.*$)', vehicles).group(1))
        clean_data = re.sub(r'(?<=\s\d)(?=\w-\d{2}\w)', ' ', clean_data)
        clean_data = re.sub(r'(?<=\)\s\d)(?=\w{3,4})', ' ', clean_data)
        clean_data = re.sub(r'(\d+)(BMPT|BMP-97|Sobolyatnik|MT-LB|MP-2IM|1V110|9A317|RB-636|Project|BPM|Super|9A310M1|T-55)', r'\1 \2', clean_data)
        clean_data = re.sub(r'(?<=\d)(?=9S)', ' ', clean_data)
        clean_data = re.sub(r'(\d+\))(\d+)', r'\1 \2', clean_data)
        clean_data = re.sub(r'\s\s', ' ', clean_data)
        clean_data = re.sub(r'(?<=:)(?=\(\d,)', ' ', clean_data)
        clean_data = re.sub(r'(?<=:)(?=\(\d\s)', ' ', clean_data)
        clean_data = re.sub(r'(?<=und\))(?=\d+)', ' ', clean_data)
        clean_data = re.sub(r'(und\)\s\d+)(?=\w+)', r'\1', clean_data)
        clean_data = re.sub(r'(?<=\w|\d)(?=\(-)', ' ', clean_data)
        clean_data = re.sub(r'(?<=sunk\))(?=\d+)', ' ', clean_data)
        clean_data = re.sub(r'sunk', 'destroyed', clean_data)
        clean_data = re.sub(r'(?<=cle)(?=\(\d)', ': ', clean_data)
        clean_data = re.sub(r'igence,', 'igence', clean_data)
        clean_data = re.sub(r'damagd', 'damaged', clean_data)
        clean_data = re.sub(r'abanonded', 'abandoned', clean_data)
        clean_data = re.sub(r'with ZU-23 AA gun, |later |stripped|ambulance, |in a non-combat related incident| on the ground| beyond economical repair| beyond economical repair on the ground|with Arbalet-DM turret, |with RP337VM1 jammer, |with RP-337VM1 jammer, |withRP-337VM1 jammer, |withRP-377VM1 jammer, |with RP-377VM1 jammer, ', '', clean_data)
        clean_data = re.sub(r'ed\sand\s', 'ed, ', clean_data)
        clean_data = re.sub(r'\)\s\(', ' ', clean_data)
        clean_data = re.sub(r'(?<=\d)\sand\s(?=\d)|(?<=,)\sand\s(?=\d)|\s\sand\s', ' ', clean_data)
        clean_data = re.sub(r'\s\s', ' ', clean_data)
        clean_data = re.sub(r'(\d+)\s(destroyed)', r'\1, \2', clean_data)
        clean_data = re.sub(r'(152mm)(2)', r'\1 \2', clean_data)
        clean_data = re.sub(r'(\d+)\s(\d+\b)', r'\1, \2', clean_data)
        clean_data = re.sub(r'\)\(', ' ', clean_data)
        clean_data = re.sub(r'(ed)\)(\s\d+,)', r'\1 \2', clean_data)
        clean_data = re.sub(r'(ed\)\s\d+)(Il-22)', r'\1 \2', clean_data)
        clean_data = re.sub(r'(ed\)\s\d+)(Mohajer)', r'\1 \2', clean_data)
        clean_data = re.sub(r'(BMP-2),\s(675-sb3KDZ)', r'\1 \2', clean_data)
        clean_data = re.sub(r'Unknown T-54/55', r'Unknown T-54/55: ', clean_data)
        clean_data = re.sub(r'(ed\))(\d+\sT-55)', r'\1 \2', clean_data)
        clean_data = re.sub(r'(\bfor)(\w)', r'\1 \2', clean_data)
        clean_data = re.sub(r'(\bfor)(ward)', r'\1\2', clean_data)
        clean_data = re.sub(r'(\w)(with)', r'\1 \2', clean_data)
        clean_data = re.sub(r'(with)(\w)', r'\1 \2', clean_data)

        clean_data = re.sub(r'damaged, abandoned', 'abandoned', clean_data)
        clean_data = re.sub(r'abandoned, destroyed', 'destroyed', clean_data)
        clean_data = re.sub(r'damaged, captured', 'captured', clean_data)
        clean_data = re.sub(r'captured, destroyed', 'destroyed', clean_data)

        while re.search(r'(destroyed\s\d+,)(?=\s\d+)', clean_data):
            clean_data = re.sub(r'(destroyed\s\d+,)(?=\s\d+)', r'\1 destroyed', clean_data)
        while re.search(r'(:\s\(\d+)(?=\s\d+,\sdestroyed)', clean_data):
            clean_data = re.sub(r'(:\s\(\d+)(?=\s\d+,\sdestroyed)', r'\1, destroyed', clean_data) #перевірка на патерн типу: ": 1 2, destroyed" на початку рядка
        while re.search(r'(\d+,\s)(?=\d+,\sdestroyed)', clean_data):
            clean_data = re.sub(r'(\d+,\s)(?=\d+,\sdestroyed)', r'\1destroyed ', clean_data)

        while re.search(r'(damaged\s\d+,)(?=\s\d+)', clean_data):
            clean_data = re.sub(r'(damaged\s\d+,)(?=\s\d+)', r'\1 damaged', clean_data)
        while re.search(r'(:\s\(\d+)(?=\s\d+,\sdamaged)', clean_data):
            clean_data = re.sub(r'(:\s\(\d+)(?=\s\d+,\sdamaged)', r'\1, damaged', clean_data)
        while re.search(r'(\d+,\s)(?=\d+,\sdamaged)', clean_data):
            clean_data = re.sub(r'(\d+,\s)(?=\d+,\sdamaged)', r'\1damaged ', clean_data)

        while re.search(r'(abandoned\s\d+,(?!\s\d+,\s*\d+\s)\d+)', clean_data):
            clean_data = re.sub(r'(abandoned\s\d+,(?!\s\d+,\s*\d+\s)\d+)', r'\1 abandoned', clean_data)
        while re.search(r'(:\s\(\d+)(?=\s\d+,\sabandoned)', clean_data):
            clean_data = re.sub(r'(:\s\(\d+)(?=\s\d+,\sabandoned)', r'\1, abandoned', clean_data)
        while re.search(r'(\d+,\s)(?=\d+,\sabandoned)', clean_data):
            clean_data = re.sub(r'(\d+,\s)(?=\d+,\sabandoned)', r'\1abandoned ', clean_data)

        while re.search(r'(captured\s\d+,)(?=\s\d+)', clean_data):
            clean_data = re.sub(r'(captured\s\d+,)(?=\s\d+)', r'\1 captured', clean_data)
        while re.search(r'(:\s\(\d+)(?=\s\d+,\scaptured)', clean_data):
            clean_data = re.sub(r'(:\s\(\d+)(?=\s\d+,\scaptured)', r'\1, captured', clean_data)
        while re.search(r'(\d+,\s)(?=\d+,\scaptured)', clean_data):
            clean_data = re.sub(r'(\d+,\s)(?=\d+,\scaptured)', r'\1captured ', clean_data)


        return(clean_data)

    def write_to_file():
        with open('clean_data_ru_{}.txt'.format(today), 'w') as f1:
            f1.write(cleaning_data())
        #with open('vehicles.txt', 'w') as f2:
        #    f2.write(vehicles)
        with open('Loses_ru_{}.txt'.format(today), 'w') as f3:
            f3.write(summary_losses())
        # with open('my_strange_data.txt', 'w') as f5:
        #     f5.write(a)

    write_to_file()

    with open('Loses_ru_{}.txt'.format(today), 'r') as f3, open('Loses_ru_{}.txt'.format(some_day), 'r') as f4:
        input1 = f3.read()
        input2 = f4.read()

    def parse_losses(input_str: str) -> dict[str, list[int]]:
        losses = {}
        lines = input_str.strip().split('\n')
        for line in lines:
            parts = line.split('(')
            vehicle_type = parts[0].strip()
            counts = [int(x.strip()) for x in re.findall(r"(\d+)(?:(?:,|\s)?\w+:)?", parts[1])]
            losses[vehicle_type] = counts
        return losses

    def compare_files(input1, input2):
        # Parse the losses for both inputs
        losses1 = parse_losses(input1)
        losses2 = parse_losses(input2)

        # Check that both inputs have the same types of vehicles
        if losses1.keys() != losses2.keys():
            print("Error: the input files do not have the same types of vehicles (ru).")
            return

        # Calculate the differences between the two inputs
        diff = {vehicle_type: [0] * 5 for vehicle_type in losses1}

        for vehicle_type in losses1:
            if len(losses1[vehicle_type]) != len(losses2[vehicle_type]):
                print(
                    "Error: the input files do not have the same number of entries (ru) for vehicle type " + vehicle_type + ".")
                continue
            for j in range(5):
                diff[vehicle_type][j] = (losses2[vehicle_type][j] - losses1[vehicle_type][j])*(-1)

        output = ""
        for vehicle_type in diff.keys():
            losses = diff[vehicle_type]
            if sum(losses) == 0:
                output += vehicle_type + ": no recent losses were observed;\n"
            else:
                loss_str = ''
                if losses[0] != 0:
                    loss_str += " +" + str(losses[0]) + ", of which:"
                if losses[1] != 0:
                    loss_str += " +" + str(losses[1]) + " destroyed,"
                if losses[2] != 0:
                    loss_str += " +" + str(losses[2]) + " damaged,"
                if losses[3] != 0:
                    loss_str += " +" + str(losses[3]) + " abandoned,"
                if losses[4] != 0:
                    loss_str += " +" + str(losses[4]) + " captured"
                output += vehicle_type + ":" + loss_str[:] + ";\n"

        output = output.strip()
        output = re.sub(r',;', ';', output)
        output = re.sub(r'\+-', '-', output)
        return output

    # print(compare_files(input1, input2))

    with open('diff_total_ru_{}_{}.txt'.format(some_day, today), 'w') as f5:
        f5.write(compare_files(input1, input2)) #може бути помилка якшо додався в новий файл новий вид техніки. тоді треба додати його ручками в той, з яким порівнювати

    def veh_type_loss():
        with open('clean_data_ru_{}.txt'.format(today), 'r') as f6:
            data = f6.read()

        # шукаємо кількість втраченої техніки для кожного типу
        matches = re.findall(r"(\d+) ([a-zA-Z0-9А-Яа-я- ‘’'.()/]+):\s\((.*?)\)", data)

        with open('output_ru.txt', 'w') as f7:   # відкриття файлу для запису
            for match in matches:
                num_lost = int(match[0])
                vehicle_type = match[1]
                lost = match[2].split(') (')
                output_str = f"{num_lost} {vehicle_type}: {lost}\n"
                f7.write(output_str)

    veh_type_loss()

    def final_data():
        with open('output_ru.txt', 'r') as f8:
            infor = f8.read()

        # шаблон для відбору числа перед "destroyed", "damaged", "abandoned" або "captured"
        num_pattern = r'\d+(?=, (?:destroyed|damaged|abandoned|captured))'

        # ітерація по рядках змінної infor
        with open('vehicle_data_ru_{}.txt'.format(today), 'w') as f9:   # відкриття файлу для запису
            lines = []
            for line in infor.split('\n'):
                # відбір числа перед ключовим словом (якщо воно є)
                num = re.findall(num_pattern, line)
                num = int(num[0]) if num else 0

                # відбір ключових слів та підрахунок їх кількості
                destroyed = line.count('destroyed')
                damaged = line.count('damaged')
                abandoned = line.count('abandoned')
                captured = line.count('captured')

                # форматування та додавання рядка до списку
                match = re.match(r'(\d+) ([a-zA-Z0-9А-Яа-я- ‘’\'.()/]+):\s', line)
                location = match.group(0) if match else ''
                final = f"{location}{destroyed} destroyed, {damaged} damaged, {abandoned} abandoned, {captured} captured\n"
                lines.append(final)

            # запис останніх двох рядків до файлу
            f9.writelines(lines[:-1])

    final_data()

    def validation():
        with open('vehicle_data_ru_{}.txt'.format(today), 'r') as f10:
            numbers = f10.read()

        tank_counts = []
        for line in numbers.split('\n'):
            match = re.search(r'^(\d+).+?(\d+) destroyed, (\d+) damaged, (\d+) abandoned, (\d+) captured$', line)
            if match:
                total_tanks = int(match.group(1))
                destroyed = int(match.group(2))
                damaged = int(match.group(3))
                abandoned = int(match.group(4))
                captured = int(match.group(5))

                if total_tanks == destroyed + damaged + abandoned + captured:
                    tank_counts.append(True)
                else:
                    tank_counts.append(False)


        with open('validation_ru.txt', 'w') as f11:
            for i, result in enumerate(tank_counts):
                f11.write('{} {}\n'.format(i+1, result))

    validation()

    with open('vehicle_data_ru_{}.txt'.format(today), 'r') as f12, open('vehicle_data_ru_{}.txt'.format(some_day), 'r') as f13:
        input_veh1 = f12.read()
        input_veh2 = f13.read()

    def parse_veh_losses(input_str: str) -> dict[str, list[int]]:
        losses = {}
        lines = input_str.strip().split('\n')
        for line in lines:
            parts = line.split(':')
            vehicle_type = re.sub(r'^\s*\d+\s*', '', parts[0]).strip()
            counts = [int(x.strip()) for x in re.findall(r"\d+", parts[1])]
            total = sum(counts[:4])
            counts.insert(0, total)
            losses[vehicle_type] = counts
        return losses

    testdata1 = parse_veh_losses(input_veh1)
    testdata2 = parse_veh_losses(input_veh2)

    def update_dictionary(testdata1, testdata2):
        d3 = {}
        for k2 in testdata1:
            d3[k2] = testdata2.get(k2) or [0, 0, 0, 0, 0]
        return d3

    input_veh2 = update_dictionary(testdata1, testdata2)

    def compare_veh_files(input_veh1, input_veh2):
        # Parse the losses for both inputs
        losses_ru1 = parse_veh_losses(input_veh1)
        losses_ru2 = input_veh2

        # Check that both inputs have the same types of vehicles
        if losses_ru1.keys() != losses_ru2.keys():
            print("Error: the input files do not have the same types of vehicles (ru).")
            return

        # Calculate the differences between the two inputs
        diff = {vehicle_type: [0] * 5 for vehicle_type in losses_ru1}

        for vehicle_type in losses_ru1:
            if len(losses_ru1[vehicle_type]) != len(losses_ru2[vehicle_type]):
                print(
                    "Error: the input files do not have the same number of entries (ru) for vehicle type " + vehicle_type + ".")
                continue
            for j in range(5):
                diff[vehicle_type][j] = (losses_ru2[vehicle_type][j] - losses_ru1[vehicle_type][j])*(-1)

        output = ""
        for vehicle_type in diff.keys():
            losses = diff[vehicle_type]
            if sum(losses) == 0:
                output += vehicle_type + ": no recent losses were observed;\n"
            else:
                loss_str = ''
                if losses[1] != 0:
                    loss_str += " +" + str(losses[1]) + " destroyed,"
                if losses[2] != 0:
                    loss_str += " +" + str(losses[2]) + " damaged,"
                if losses[3] != 0:
                    loss_str += " +" + str(losses[3]) + " abandoned,"
                if losses[4] != 0:
                    loss_str += " +" + str(losses[4]) + " captured"
                output += vehicle_type + ":" + loss_str[:] + ";\n"
        output = output.strip()
        output = re.sub(r',;', ';', output)
        output = re.sub(r'\+-', '-', output)
        return output

    compare_veh_files(input_veh1, input_veh2)

    def remove_no_losses(text):
        lines = text.split('\n')
        filtered_lines = [line for line in lines if "no recent losses were observed;" not in line]
        filtered_text = '\n'.join(filtered_lines)
        return filtered_text

    with open('diff_veh_ru_{}_{}.txt'.format(some_day, today), 'w') as f14:
        f14.write(remove_no_losses(compare_veh_files(input_veh1, input_veh2)))
rus_losses()

def ua_losses():
    url = 'https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-ukrainian.html'
    response = requests.get(url)
    response.text

    soup = BeautifulSoup(response.text, 'html.parser')

    # Отримання тексту таблиці з втратами
    text = soup.find('div', class_='post-body entry-content').get_text()

    # Видалення зайвих елементів з тексту
    loses = re.sub(r'[\xa0\n]|Special thanks to[\s\S]*$', '', text[text.index(
        "(Click on the numbers to get a picture of each individual captured or destroyed vehicle)") + len(
        "(Click on the numbers to get a picture of each individual captured or destroyed vehicle)"):]).strip()

    total_loses = re.findall(r' - (.*?)Tanks', loses, flags=re.DOTALL | re.MULTILINE)[0].strip()
    total_loses = re.sub(r'which:', 'which', total_loses)
    vehicles = "Tanks " + re.findall(r'(?<=\dTanks\b)(.*$)', loses, flags=re.DOTALL | re.MULTILINE)[0].strip()
    vehicles = re.sub(r"(\(\d+\sdestroyed\)93,)", '(92, destroyed) (93,', vehicles)  #########################
    if "oyed) Downg" in vehicles:
        vehicles = re.sub(r'oyed\)\sDowng', 'oyed) 1 Downg', vehicles)
    if ")180mm B-8" in vehicles:
        vehicles = re.sub(r'\)180mm B-8', ') 1 180mm B-8', vehicles)
    if ")1BTR-ZD" in vehicles:
        vehicles = re.sub(r'\)1BTR-ZD', ') 1 BTR-ZD', vehicles)
    if ")1 BMPT" in vehicles:
        vehicles = re.sub(r'\)1 BMPT', ') 1 BMPT', vehicles)
    if ")1THeMIS" in vehicles:
        vehicles = re.sub(r'\)1THeMIS', ') 1 THeMIS', vehicles)

    def summary_losses():
        tanks_summary = re.findall(r'^(.*?)(?=\d+\sM-55S:)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip()
        afv_summary = re.findall(r'^(.*?)(?=\s\d+\sBMPT)', 'Armoured ' + re.findall(r'(?<=Armoured\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        ifv_summary = re.findall(r'^(.*?)(?=\d+\sBMP.)', 'Infantry ' + re.findall(r'(?<=Infantry\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        apc_summary = re.findall(r'^(.*?)(?=\d+\sBTR.60PB)', 'Armoured Personnel ' + re.findall(r'(?<=Armoured\sPersonnel\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        mrap_summary = re.findall(r'^(.*?)(?=\d+\sVepr)', 'Mine-' + re.findall(r'(?<=Mine.)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        mrap_summary = re.sub(r'\(MRAP\) ', '', mrap_summary)
        mrap_summary = re.sub(r'cles\(', 'cles (', mrap_summary)
        imv_summary = re.findall(r'^(.*?)(?=\d+\sKrAZ Cobra)', 'Infantry Mobility ' + re.findall(r'(?<=Infantry\sMobility\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        cpacs_summary = re.findall(r'^(.*?)(?=\d+\sBMP-1KSh)', 'Command ' + re.findall(r'(?<=Command\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        evae_summary = re.findall(r'^(.*?)(?=\d+\sIMR-2)', 'Engineering ' + re.findall(r'(?<=Engineering\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        ugv_summary = re.findall(r'^(.*?)(?=\d+\sTHeMIS UGV)', 'Unmanned Ground ' + re.findall(r'(?<=Unmanned Ground\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        spatms_summary = re.findall(r'^(.*?)(?=\d+\s9P148)', 'Self-Propelled Anti-Tank ' + re.findall(r'(?<=Self-Propelled Anti-Tank\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        asvae_summary = re.findall(r'^(.*?)(?=\d+\s1V13 battery)', 'Artillery Support ' + re.findall(r'(?<=Artillery Support\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        ta_summary = re.findall(r'^(.*?)(?=\d+\s100mm)', 'Towed ' + re.findall(r'(?<=Towed\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        spa_summary = re.findall(r'^(.*?)(?=\d+\s120mm Bars-8MMK)', 'Self-Propelled Artillery ' + re.findall(r'(?<=Self-Propelled Artillery\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        mrls_summary = re.findall(r'^(.*?)(?=\d+\s180mm B-8)', 'Multiple Rocket Launchers ' + re.findall(r'(?<=Multiple Rocket Launchers\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        aag_summary = re.findall(r'^(.*?)(?=\d+\s23mm ZU)', 'Anti-Aircraft ' + re.findall(r'(?<=Anti-Aircraft\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        spaag_summary = re.findall(r'^(.*?)(?=\d+\sBTR-ZD Skrezhet)', 'Self-Propelled Anti-Aircraft ' + re.findall(r'(?<=Self-Propelled Anti-Aircraft\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        stams_summary = re.findall(r'^(.*?)(?=\d+\s9K33 Osa)', 'Surface-To-Air ' + re.findall(r'(?<=Surface-To-Air\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        radars_summary = re.findall(r'^(.*?)(?=\d+\sP-14)', 'Radars ' + re.findall(r'(?<=Radars\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        jads_summary = re.findall(r'^(.*?)(?=\d+\sNOTA)', 'Jammers ' + re.findall(r'(?<=Jammers\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        jads_summary = re.sub(r'whichdestroyed', 'which destroyed', jads_summary)
        aircraft_summary = re.findall(r'^(.*?)(?=\d+\sMiG)', 'Aircraft (' + re.findall(r'(?<=Aircraft\s.\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        helicopters_summary = re.findall(r'^(.*?)(?=\d+\sMi-2)', 'Helicopters ' + re.findall(r'(?<=Helicopters\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        ucav_summary = re.findall(r'^(.*?)(?=\d+\sBayraktar)', 'Unmanned Combat ' + re.findall(r'(?<=Unmanned Combat\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        rcav_summary = re.findall(r'^(.*?)(?=\d+\sA1-SM Fury)', 'Reconnaissance  ' + re.findall(r'(?<=Reconnaissance\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        navalships_summary = re.findall(r'^(.*?)(?=\d+\sKrivak III-class)', 'Naval  ' + re.findall(r'(?<=Naval\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()
        trucks_summary = re.findall(r'^(.*?)(?=\d+\sKrAZ-214)', 'Trucks' + re.findall(r'(?<=Trucks\b)(.*$)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip(), flags=re.DOTALL | re.MULTILINE)[0].strip()

        total = 'Total vehicle losses of Ukraine (' + total_loses + ')' + '\n' + tanks_summary + '\n' + afv_summary + '\n' + ifv_summary + '\n' + apc_summary + '\n' + mrap_summary + '\n' + imv_summary + '\n' + cpacs_summary + '\n' + evae_summary + '\n' + ugv_summary + '\n' + spatms_summary + '\n' + asvae_summary + '\n' + ta_summary + '\n' + spa_summary + '\n' + mrls_summary + '\n' + aag_summary + '\n' + spaag_summary + '\n' + stams_summary + '\n' + radars_summary + '\n' + jads_summary + '\n' + aircraft_summary + '\n' + helicopters_summary + '\n' + ucav_summary + '\n' + rcav_summary + '\n' + navalships_summary + '\n' + trucks_summary
        total = re.sub(r'\sof\swhich', '', total)
        total = re.sub(r'^(?!.*damaged.*$).*destroyed:\s\d+', r'\g<0>, damaged: 0', total, flags=re.MULTILINE)
        total = re.sub(r'^(?!.*abandoned.*$).*damaged:\s\d+', r'\g<0>, abandoned: 0', total, flags=re.MULTILINE)
        total = re.sub(r'^(?!.*captured.*$).*abandoned:\s\d+', r'\g<0>, captured: 0', total, flags=re.MULTILINE)
        total = re.sub(r'(\(\d,\s)(captured:\s\d)', r'\1destroyed: 0, damaged: 0, abandoned: 0, \2', total)

        return (total)

    def cleaning_data():
        clean_data = re.findall(r'^(.*?)(?=\d+\s\w.\w{2}\s)', vehicles, flags=re.DOTALL | re.MULTILINE)[0].strip() + ' ' + re.sub(r'ed\)', r'ed) ', re.search(r'(?=\d+\s\w.\w{2}\s)(.*$)', vehicles).group(1))
        clean_data = re.sub(r'(?<=\s\d)(?=\w-\d{2}\w)', ' ', clean_data)
        clean_data = re.sub(r'(MT-LB with ZU-23 AA gun)', 'MT-LB with ZU-23 АА gun', clean_data)
        clean_data = re.sub(r'(\d+\))(\d+)', r'\1 \2', clean_data)
        clean_data = re.sub(r'(\d+)(Sisu|AN/TPQ|PRP|ATs|KrAZ|Primoco|Avenger|L-39|120mm|Bergepanzer|SkyGuard|MT-LB|Roshel|MLS|AN|INKAS|9S470M1|Control|Iveco|MT-T|IRM|MTO|KrAZ-260|KrAZ-255B|PZM|UMP|Ural-4320|AK-04|155mm|152mm|122mm|Stormer|Launcher|5N66M|ST-68U|PRV-16ML|TRML|Bukovel|Airbus|Spaitech|ITEC|Mara-2M|ScanEagle|GAZ-|MAZ|Mercedes|Pinzgauer|UAZ|Peugeot|130mm|79K6|UMS|Project)', r'\1 \2', clean_data)
        clean_data = re.sub(r"('BG\s\d+',)", '', clean_data)
        clean_data = re.sub(r'(\d+)\sand\s(\d+)', r'\1, \2', clean_data)
        clean_data = re.sub(r"(\sand|with ZU-23-2 cannon|with ATGM|Kremenchuk 'P177',|Akkerman 'P174',|Vyshhorod 'P179',|'DSHK-1 Stanislav',|BG-32 'Donbass'|with M2 HMG|with KPV HMG|\sby|later|with ZU-23 AA gun|with 23mm ZU-23|on the ground|beyond economical repair|with 82mm 2B9 Vasilek mortar|unknown ID,)",'', clean_data)
        clean_data = re.sub(r"sunk", 'destroyed', clean_data)
        clean_data = re.sub(r"Lubny 'P178', destroyed but  raised Russia", 'captured', clean_data)
        clean_data = re.sub(r'scuttled to prevent capture Russia', 'damaged', clean_data)
        clean_data = re.sub(r'(:)(\(\d+)|(\d+\))(\d+)', r'\1 \2', clean_data)
        clean_data = re.sub(r'(\)\()', r') (', clean_data)
        clean_data = re.sub(r'\s+', ' ', clean_data)
        clean_data = re.sub(r"''", '"', clean_data)
        clean_data = re.sub(r"radr", 'radar', clean_data)
        clean_data = re.sub(r'(ed\))(\d+\s)', r'\1 \2', clean_data)
        clean_data = re.sub(r'whichdestroyed', r'which destroyed', clean_data)
        clean_data = re.sub(r'(\)\s\()', r', ', clean_data)
        clean_data = re.sub(r'(\d+)\s(destroyed)', r'\1, \2', clean_data)
        clean_data = re.sub(r"\s,", '', clean_data)
        clean_data = re.sub(r'(destroyed|damaged|abandoned|captured),(\s)', r'\1\2', clean_data)
        clean_data = re.sub(r'(ed\)\s)(\w+)', r'\1\n\2', clean_data)
        clean_data = re.sub(r'(\d)(YAD)', r'\1 \2', clean_data)
        clean_data = re.sub(r'(M88A1)(armoured)', r'\1 \2', clean_data)
        clean_data = re.sub(r'(155mm)(\w+)', r'\1 \2', clean_data)

        clean_data = re.sub(r'damaged abandoned', 'abandoned', clean_data)
        clean_data = re.sub(r'abandoned destroyed', 'destroyed', clean_data)
        clean_data = re.sub(r'damaged captured', 'captured', clean_data)
        clean_data = re.sub(r'captured destroyed', 'destroyed', clean_data)

        while re.search(r'(destroyed\s\d+,)(?=\s\d+)', clean_data):
            clean_data = re.sub(r'(destroyed\s\d+,)(?=\s\d+)', r'\1 destroyed', clean_data)
        while re.search(r'(:\s\(\d+)(?=\s\d+,\sdestroyed)', clean_data):
            clean_data = re.sub(r'(:\s\(\d+)(?=\s\d+,\sdestroyed)', r'\1, destroyed', clean_data) #перевірка на патерн типу: ": 1 2, destroyed" на початку рядка
        while re.search(r'(\d+,\s)(?=\d+,\sdestroyed)', clean_data):
            clean_data = re.sub(r'(\d+,\s)(?=\d+,\sdestroyed)', r'\1destroyed ', clean_data)

        while re.search(r'(damaged\s\d+,)(?=\s\d+)', clean_data):
            clean_data = re.sub(r'(damaged\s\d+,)(?=\s\d+)', r'\1 damaged', clean_data)
        while re.search(r'(:\s\(\d+)(?=\s\d+,\sdamaged)', clean_data):
            clean_data = re.sub(r'(:\s\(\d+)(?=\s\d+,\sdamaged)', r'\1, damaged', clean_data)
        while re.search(r'(\d+,\s)(?=\d+,\sdamaged)', clean_data):
            clean_data = re.sub(r'(\d+,\s)(?=\d+,\sdamaged)', r'\1damaged ', clean_data)

        while re.search(r'(abandoned\s\d+,(?!\s\d+,\s*\d+\s)\d+)', clean_data):
            clean_data = re.sub(r'(abandoned\s\d+,(?!\s\d+,\s*\d+\s)\d+)', r'\1 abandoned', clean_data)
        while re.search(r'(:\s\(\d+)(?=\s\d+,\sabandoned)', clean_data):
            clean_data = re.sub(r'(:\s\(\d+)(?=\s\d+,\sabandoned)', r'\1, abandoned', clean_data)
        while re.search(r'(\d+,\s)(?=\d+,\sabandoned)', clean_data):
            clean_data = re.sub(r'(\d+,\s)(?=\d+,\sabandoned)', r'\1abandoned ', clean_data)

        while re.search(r'(captured\s\d+,)(?=\s\d+)', clean_data):
            clean_data = re.sub(r'(captured\s\d+,)(?=\s\d+)', r'\1 captured', clean_data)
        while re.search(r'(:\s\(\d+)(?=\s\d+,\scaptured)', clean_data):
            clean_data = re.sub(r'(:\s\(\d+)(?=\s\d+,\scaptured)', r'\1, captured', clean_data)
        while re.search(r'(\d+,\s)(?=\d+,\scaptured)', clean_data):
            clean_data = re.sub(r'(\d+,\s)(?=\d+,\scaptured)', r'\1captured ', clean_data)

        clean_data = re.sub(r'(\d+\)\s)(\d+\s)', r'\1\n\2', clean_data)
        clean_data = re.sub(r'(ed\)\s)(\d+\s)', r'\1\n\2', clean_data)

        return(clean_data)

    def write_to_file():
        with open('clean_data_ua_{}.txt'.format(today), 'w') as f1:
            f1.write(cleaning_data())
        with open('Loses_ua_{}.txt'.format(today), 'w') as f2:
            f2.write(summary_losses())
        #with open('vehicles_ua_{}.txt'.format(today), 'w') as f222:  #для траблшутінга неочищених даних
            #f222.write(vehicles)

    write_to_file()

    with open('Loses_ua_{}.txt'.format(today), 'r') as f3, open('Loses_ua_{}.txt'.format(some_day), 'r') as f4:
        input1 = f3.read()
        input2 = f4.read()

    def parse_losses(input_str: str) -> dict[str, list[int]]:
        losses = {}
        lines = input_str.strip().split('\n')
        for line in lines:
            parts = line.split('(')
            vehicle_type = parts[0].strip()
            counts = [int(x.strip()) for x in re.findall(r"(\d+)(?:(?:,|\s)?\w+:)?", parts[1])]
            losses[vehicle_type] = counts
        return losses
    #
    def compare_files(input1, input2):
        # Parse the losses for both inputs
        losses1 = parse_losses(input1)
        losses2 = parse_losses(input2)

        # Check that both inputs have the same types of vehicles
        if losses1.keys() != losses2.keys():
            print("Error: the input files do not have the same types of vehicles. (ua)")
            return

        # Calculate the differences between the two inputs
        diff = {vehicle_type: [0] * 5 for vehicle_type in losses1}

        for vehicle_type in losses1:
            if len(losses1[vehicle_type]) != len(losses2[vehicle_type]):
                print(
                    "Error: the input files do not have the same number of entries (ua) for vehicle type " + vehicle_type + ".")
                continue
            for j in range(5):
                diff[vehicle_type][j] = (losses2[vehicle_type][j] - losses1[vehicle_type][j])*(-1)

        output = ""
        for vehicle_type in diff.keys():
            losses = diff[vehicle_type]
            if sum(losses) == 0:
                output += vehicle_type + ": no recent losses were observed;\n"
            else:
                loss_str = ''
                if losses[0] != 0:
                    loss_str += " +" + str(losses[0]) + ", of which:"
                if losses[1] != 0:
                    loss_str += " +" + str(losses[1]) + " destroyed,"
                if losses[2] != 0:
                    loss_str += " +" + str(losses[2]) + " damaged,"
                if losses[3] != 0:
                    loss_str += " +" + str(losses[3]) + " abandoned,"
                if losses[4] != 0:
                    loss_str += " +" + str(losses[4]) + " captured"
                output += vehicle_type + ":" + loss_str[:] + ";\n"

        output = output.strip()
        output = re.sub(r',;', ';', output)
        output = re.sub(r'\+-', '-', output)
        return output

    with open('diff_total_ua_{}_{}.txt'.format(some_day, today), 'w') as f5:
        f5.write(compare_files(input1, input2))

    def veh_type_loss():
        with open('clean_data_ua_{}.txt'.format(today), 'r') as f6:
            data = f6.read()

        # шукаємо кількість втраченої техніки для кожного типу
        matches = re.findall(r"(\d+) ([a-zA-Z0-9А-Яа-я- ‘’'.()/]+):\s\((.*?)\)", data)

        with open('output_ua.txt', 'w') as f7:   # відкриття файлу для запису
            for match in matches:
                num_lost = int(match[0])
                vehicle_type = match[1]
                lost = match[2].split(') (')
                output_str = f"{num_lost} {vehicle_type}: {lost}\n"
                f7.write(output_str)

    veh_type_loss()

    def final_data():
        with open('output_ua.txt', 'r') as f8:
            infor = f8.read()

        # шаблон для відбору числа перед "destroyed", "damaged", "abandoned" або "captured"
        num_pattern = r'\d+(?=, (?:destroyed|damaged|abandoned|captured))'

        # ітерація по рядках змінної infor
        with open('vehicle_data_ua_{}.txt'.format(today), 'w') as f9:   # відкриття файлу для запису
            lines = []
            for line in infor.split('\n'):
                # відбір числа перед ключовим словом (якщо воно є)
                num = re.findall(num_pattern, line)
                num = int(num[0]) if num else 0

                # відбір ключових слів та підрахунок їх кількості
                destroyed = line.count('destroyed')
                damaged = line.count('damaged')
                abandoned = line.count('abandoned')
                captured = line.count('captured')

                # форматування та додавання рядка до списку
                match = re.match(r'(\d+) ([a-zA-Z0-9А-Яа-я- ‘’\'.()/]+):\s', line)
                location = match.group(0) if match else ''
                final = f"{location}{destroyed} destroyed, {damaged} damaged, {abandoned} abandoned, {captured} captured\n"
                lines.append(final)

            # запис останніх двох рядків до файлу
            f9.writelines(lines[:-1])

    final_data()

    def validation():
        with open('vehicle_data_ua_{}.txt'.format(today), 'r') as f10:
            numbers = f10.read()

        tank_counts = []
        for line in numbers.split('\n'):
            match = re.search(r'^(\d+).+?(\d+) destroyed, (\d+) damaged, (\d+) abandoned, (\d+) captured$', line)
            if match:
                total_tanks = int(match.group(1))
                destroyed = int(match.group(2))
                damaged = int(match.group(3))
                abandoned = int(match.group(4))
                captured = int(match.group(5))

                if total_tanks == destroyed + damaged + abandoned + captured:
                    tank_counts.append(True)
                else:
                    tank_counts.append(False)


        with open('validation_ua.txt', 'w') as f11:
            for i, result in enumerate(tank_counts):
                f11.write('{} {}\n'.format(i+1, result))

    validation()

    with open('vehicle_data_ua_{}.txt'.format(today), 'r') as f12, open('vehicle_data_ua_{}.txt'.format(some_day), 'r') as f13:
        input_veh1 = f12.read()
        input_veh2 = f13.read()

    def parse_veh_losses(input_str: str) -> dict[str, list[int]]:
        losses = {}
        lines = input_str.strip().split('\n')
        for line in lines:
            parts = line.split(':')
            vehicle_type = re.sub(r'^\s*\d+\s*', '', parts[0]).strip()
            counts = [int(x.strip()) for x in re.findall(r"\d+", parts[1])]
            total = sum(counts[:4])
            counts.insert(0, total)
            losses[vehicle_type] = counts
        return losses

    testdata1 = parse_veh_losses(input_veh1)
    testdata2 = parse_veh_losses(input_veh2)

    def update_dictionary(testdata1, testdata2):
        d3 = {}
        for k2 in testdata1:
            d3[k2] = testdata2.get(k2) or [0, 0, 0, 0, 0]
        return d3

    input_veh2 = update_dictionary(testdata1, testdata2)

    def compare_veh_files(input_veh1, input_veh2):
        # Parse the losses for both inputs
        losses_ua1 = parse_veh_losses(input_veh1)
        losses_ua2 = input_veh2

        # Check that both inputs have the same types of vehicles
        if losses_ua1.keys() != losses_ua2.keys():
            print("Error: the input files do not have the same types of vehicles (ua).")
            return

        # Calculate the differences between the two inputs
        diff = {vehicle_type: [0] * 5 for vehicle_type in losses_ua1}

        for vehicle_type in losses_ua1:
            if len(losses_ua1[vehicle_type]) != len(losses_ua2[vehicle_type]):
                print(
                    "Error: the input files do not have the same number of entries (ua) for vehicle type " + vehicle_type + ".")
                continue
            for j in range(5):
                diff[vehicle_type][j] = (losses_ua2[vehicle_type][j] - losses_ua1[vehicle_type][j])*(-1)

        output = ""
        for vehicle_type in diff.keys():
            losses = diff[vehicle_type]
            if sum(losses) == 0:
                output += vehicle_type + ": no recent losses were observed;\n"
            else:
                loss_str = ''
                if losses[1] != 0:
                    loss_str += " +" + str(losses[1]) + " destroyed,"
                if losses[2] != 0:
                    loss_str += " +" + str(losses[2]) + " damaged,"
                if losses[3] != 0:
                    loss_str += " +" + str(losses[3]) + " abandoned,"
                if losses[4] != 0:
                    loss_str += " +" + str(losses[4]) + " captured"
                output += vehicle_type + ":" + loss_str[:] + ";\n"

        output = output.strip()
        output = re.sub(r',;', ';', output)
        output = re.sub(r'\+-', '-', output)
        return output

    def remove_no_losses(text):
        lines = text.split('\n')
        filtered_lines = [line for line in lines if "no recent losses were observed;" not in line]
        filtered_text = '\n'.join(filtered_lines)
        return filtered_text

    remove_no_losses(compare_veh_files(input_veh1, input_veh2))

    with open('diff_veh_ua_{}_{}.txt'.format(some_day, today), 'w') as f14:
        f14.write(remove_no_losses(compare_veh_files(input_veh1, input_veh2)))
ua_losses()
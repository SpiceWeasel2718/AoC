from pathlib import Path
import requests

def prepare_next_day(year=2020, day=None, overwrite=False, just_input=False):
    session='53616c7465645f5f801dbfe283b636aa595d1b71603298bcb117bb17601ea43e4e0baeaf0485b789ee673d9ca26d4b19'
    # AoC page > inspector > application > cookies

    year_dir = Path(str(year))
    if not year_dir.exists():
        year_dir.mkdir()
    inputs_dir = year_dir / 'input_files'
    if not inputs_dir.exists():
        inputs_dir.mkdir()
    
    # create path to .py file
    if day is None:
        for day in range(1,26):
            path = year_dir / f'AoC{year}_day{day:0>2}.py'
            if not path.exists():
                break
        else:
            print('There is already a file for every day this year')
            return
    else:
        path = year_dir / f'AoC{year}_day{day:0>2}.py'
        if path.exists() and not (overwrite or just_input):
            print('File already exists')
            return
    
    input_path = inputs_dir / (path.stem + '_input.txt')
    
    #get input text and make input file
    r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session})
    if r.status_code == 200:
        with open(input_path, 'w') as f:
            f.write(r.text)
            print(f'Input file {input_path.name} created')
    else:
        print('Request failed, error code:', r.status_code)
        print('Reminder to check if session cookie expired')
        return
    
    #make .py file
    if not just_input:
        with open('day_template.txt', 'r') as t:
            template = t.read()
            with open(path, 'w') as f:
                f.write(template.replace('<input_file>', input_path.name).replace('<year>', str(year)))
                print(f'Program file {path.name} created')


if __name__ == '__main__':
    prepare_next_day(year=2020)
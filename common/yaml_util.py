import yaml


def read_yaml(url):
    with open(file=url, mode='r', encoding='utf-8') as f:
        result = yaml.load(f, yaml.FullLoader)
        return result


def write_yaml(data):
    with open('./testdata/save_token.yaml', mode='w', encoding='utf8') as f:
        yaml.dump(data, stream=f, allow_unicode=True)
        # yaml.safe_dump(date, f)


def clear_yaml():
    with open('') as f:
        f.truncate()

import yaml
class readyaml():

    def get_yaml_data(self):
        with open('./data/generate.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        return result
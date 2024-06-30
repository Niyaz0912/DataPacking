class CountryState:
    def __init__(self):
        self.data = {}

    def add_pair(self, country, capital):
        self.data[country] = capital

    def remove_pair(self, country):
        if country in self.data:
            del self.data[country]

    def search_by_key(self, country):
        return self.data.get(country, "Страна не найдена")

    def search_by_capital(self, capital):
        for country, cap in self.data.items():
            if cap == capital:
                return country
        return "Столица не найдена"

    def edit_value(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital

    def save_data(self, file_name):
        with open(file_name, 'w') as file:
            for country, capital in self.data.items():
                file.write(f"{country}:{capital}\n")

    def load_data(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            self.data = {}
            for line in lines:
                country, capital = line.strip().split(':')
                self.data[country] = capital

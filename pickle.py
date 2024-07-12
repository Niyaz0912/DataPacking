import pickle


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

    def search_by_value(self, capital):
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


country_state = CountryState()
country_state.add_pair("Россия", "Москва")
country_state.add_pair("США", "Вашингтон")
country_state.add_pair("Франция", "Париж")

print(country_state.search_by_key("Россия"))
print(country_state.search_by_value("Париж"))

country_state.edit_value("Россия", "Санкт-Петербург")
print(country_state.search_by_key("Россия"))

country_state.save_data("country_state.txt")
country_state.data = {}
country_state.load_data("country_state.txt")
print(country_state.search_by_key("Россия"))

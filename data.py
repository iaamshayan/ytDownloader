import json
class data_handler:
    def __init__(self, file_path='yt_data.txt'):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                # Assuming the file contains a list of strings
            return data
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
            return []
    
    def save_data(self,new_data=None):
        try:
            if new_data:
                self.data.append(new_data)
            else:
                self.data = [self.data]  # Ensure data is a list
            with open(self.file_path, 'w') as file:
                json.dump(self.data, file)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def display_data(self):
        data = self.load_data()
        if data:
            for index, line in enumerate(data,start=1):
                print(f"{index} : Title : {line['Title']} - Views {line['Views']}")
        else:
            print("No data to display.")

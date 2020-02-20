import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('train.csv').values
test_data = pd.read_csv('test.csv').values

class processor:
    def process_data(self, data):
        return data

class predictor:
    def __init__(self, model):
        self.model = model
    def predict(self, data):
        predictions = self.model.predict(data)
        return predictions

Processor = processor()
processed_data = Processor.process_data(data)
#print(processed_data)
model = DecisionTreeClassifier()

print(processed_data[:, 1:3])
#print(processed_data[:, 2].reshape(-1, 1))

model.fit(processed_data[:, 1:3], processed_data[:, 2])

Predictor = predictor(model)

print(Predictor.predict(test_data[:, 1]).reshape(-1, 1))

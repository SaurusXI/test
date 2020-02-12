import pickle


class processor:
    def process_data(self, data):
        return data

class predictor:
    def __init__(self, model):
        self.model = model
    def predict(self, data):
        predictions = self.model.predict(data)
        return predictions

def process(data):
    with open('processor.pickle', 'rb') as f:
        processor = pickle.load(f)

    data = processor.process(data)
    return data

def predict(data):
    with open('predictor.pickle', 'rb') as f:
        predictor = pickle.load(f)

    print(type(predictor))
    predictions = predictor.predict(data)
    return predictions

data = [[2]]
print(predict(data))
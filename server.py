import pickle

def process(data):
    if not isinstance(data, datatype):
        return 'Error'
    with open('processor.pickle', 'rb') as f:
        processor = pickle.load(f)

    data = processor.process(data)
    return data

def predict(data):
    with open('predictor.pickle', 'wb') as f:
        predictor = pickle.load(f)

    predictions = predictor.predict(data)
    return predictions
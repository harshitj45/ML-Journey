# ============================================
# PROGRAM 26: SimpleMLModel Class
# CONCEPTS: class, __init__, instance variable,
#           methods, __str__, return self,
#           @classmethod, @staticmethod
# ============================================

class SimpleMLModel:

    def __init__(self, model_name):
        self.model_name = model_name
        self.is_trained = False    
        self.params     = {}       

    def fit(self, data):
        if not data:
            print("Data is empty ,not fitting!")
            return self
        self.is_trained = True
        self.params["data_size"] = len(data)
        print(f"{self.model_name} trained on {len(data)} samples")
        return self              

    def predict(self, value):
        if not self.is_trained:
            print("firstly fit() data!")
            return None
        print(f"Predicting for: {value}")
        return value * 2     

    def __str__(self):
        return (f"Model: {self.model_name} | "
                f"Trained: {self.is_trained} | "
                f"Params: {self.params}")

    @classmethod
    def create_default(cls):
        return cls("DefaultModel")

    @staticmethod
    def is_valid_data(data):
        return isinstance(data, list) and len(data) > 0


# ── TESTS ──

# Normal creation:
model1 = SimpleMLModel("LinearModel")
print(model1)       

# Predict before fit:
model1.predict(10)  

# Fit then predict:
data = [1, 2, 3, 4, 5]
model1.fit(data).predict(10)    

print(model1)      

# @classmethod use:
model2 = SimpleMLModel.create_default()
print(model2)       

# @staticmethod use:
print(SimpleMLModel.is_valid_data([1, 2, 3]))   
print(SimpleMLModel.is_valid_data([]))           
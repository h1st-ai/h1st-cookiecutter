from h1st.model.ml_model import MLModel


class MyMLModel(MLModel):
    # def __init__(self) -> None:
    #     self.persist('example_ml_model')

    def predict(self, input_data: dict) -> dict:
        if input_data["input_language"] == input_data["output_language"]:
            return {"result": input_data["text"]}
        return {"result": "oopsie daisy! dont know how to translate that"}

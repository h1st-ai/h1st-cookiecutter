import h1st.core as h1


class TranslateModel(h1.RuleBasedModel):
    """
    A rule-based model that "echoes" the input
    """

    def predict(self, data: dict) -> dict:
        if data["input_language"] == data["output_language"]:
            return {"result": data["text"]}
        else:
            return {"result": "oopsie daisy! dont know how to translate that"}

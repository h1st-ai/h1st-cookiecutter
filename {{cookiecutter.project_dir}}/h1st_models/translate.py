"""
h1 model that can translate text in the specified language
"""
import h1st.core as h1


class TranslateModel(h1.RuleBasedModel):
    """
    A rule-based model that "echoes" the input
    """
    def predict(self, input_data: dict) -> dict:
        if input_data["input_language"] == input_data["output_language"]:
            return {"result": input_data["text"]}
        return {"result": "oopsie daisy! dont know how to translate that"}

"""
h1 model that can translate text in the specified language
"""
from h1st.model.rule_based_model import RuleBasedModel


class TranslateModel(RuleBasedModel):
    """
    A rule-based model that "echoes" the input
    """
    def predict(self, input_data: dict) -> dict:
        if input_data["input_language"] == input_data["output_language"]:
            return {"result": input_data["text"]}
        return {"result": "oopsie daisy! dont know how to translate that"}

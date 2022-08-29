from .base_evaluator import BaseEvaluator
import re


class RegexEquals(BaseEvaluator):
    def evaluate(self, evaluator_input, evaluator_data):
        evaluation_result = {"passed": False, "message": "Failed before evaluation."}
        try:
            match = 0
            if type(evaluator_input['value']) == str and type(evaluator_data) == str:
                match = re.match(evaluator_data, evaluator_input['value'])
                if match is None:
                    evaluation_result = {
                        "passed": False,
                        "message": "Input {} does not match regex pattern {}".format(evaluator_input, evaluator_data),
                    }
                else:
                    evaluation_result = {"passed": True, "message": "Input {} matches regex pattern {}".format(
                    evaluator_input, evaluator_data
                )}
            else:
                evaluation_result = {
                    "passed": False,
                    "message": "Input {} does not match regex pattern {}".format(evaluator_input, evaluator_data),
                }
            return evaluation_result
        except Exception as e:
            evaluation_result["message"] = str(e)
            return evaluation_result

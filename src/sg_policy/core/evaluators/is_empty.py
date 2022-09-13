from .base_evaluator import BaseEvaluator

# Checks if input is empty (null, empty list [], empty dict {}, empty str '')

# Args:
#     value (mixed): Value to check.

# Returns:
#     bool: Whether :attr:`value` is empty

# Example:

#     >>> e('')
#     True
#     >>> e("abc")
#     False
#     >>> l([])
#     True

# .. versionadded:: 1.0.0-alpha.1


class IsEmpty(BaseEvaluator):
    def evaluate(self, evaluator_input, evaluator_data=None):
        evaluation_result = {"passed": False, "message": "Not evaluated"}
        try:
            if (isinstance(evaluator_input, str) or isinstance(evaluator_input, list) or isinstance(evaluator_input, dict)) and not evaluator_input:
                evaluation_result["passed"] = True
                evaluation_result["message"] = "{} is empty".format(evaluator_input)
            if not evaluation_result["passed"]:
                evaluation_result["message"] = "{} is not empty".format(evaluator_input)
            return evaluation_result
        except Exception as e:
            evaluation_result["message"] = str(e)
            return evaluation_result

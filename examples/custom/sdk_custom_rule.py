from dingo.io import InputArgs
from dingo.exec import Executor

input_data = {
    "eval_group": "test",
    "input_path": "../../test/data/test_local_json.json",  # local filesystem dataset
    "dataset": "local",
    "data_format": "json",
    "column_content": "prediction",
    "custom_config": {
        "rule_list": ["RuleSpecialCharacter"],
        "rule_config": {
            "RuleSpecialCharacter": {
                "pattern": "sky"
            }
        }
    }
}
input_args = InputArgs(**input_data)
executor = Executor.exec_map["local"](input_args)
result = executor.execute()
print(result)
from dingo.io import InputArgs
from dingo.exec import Executor

input_data = {
    "eval_group": "test",
    "input_path": "../../test/data/test_local_jsonl.jsonl",  # local filesystem dataset
    "save_data": True,
    "save_correct": True,
    "dataset": "local",
    "data_format": "jsonl",
    "column_content": "content",
    "custom_config":
        {
            "prompt_list": ["PromptRepeat"],
            "llm_config":
                {
                    "detect_text_quality":
                        {
                            "key": "",
                            "api_url": "",
                        }
                }
        }
}
input_args = InputArgs(**input_data)
executor = Executor.exec_map["local"](input_args)
result = executor.execute()
print(result)
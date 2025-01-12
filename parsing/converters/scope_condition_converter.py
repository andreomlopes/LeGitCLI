from model.scope_conditions import ScopeCondition
from parsing.converters.base_converter import BaseConverter
from parsing.converters.dynamic import ConcreteScopeConditionParametersConverter


class ScopeConditionConverter(BaseConverter[dict, ScopeCondition]):
    def __init__(self, scope_condition_dict: dict, field_path: list[str]) -> None:
        super().__init__(scope_condition_dict, field_path, dict)

    def convert(self) -> ScopeCondition:
        self._assert_fields(required_field_names={"Type", "Action", "Parameters"})
        scope_type = self.object_to_convert["Type"]
        scope_action = self.object_to_convert["Action"]
        scope_parameters = self.object_to_convert["Parameters"]

        return ConcreteScopeConditionParametersConverter(
            scope_parameters, self.field_path + ["Parameters"], scope_action, scope_type
        ).convert()

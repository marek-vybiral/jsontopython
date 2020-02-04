from typing import Union


class FormattingException(Exception):
	...


def format_data(input: Union[dict, list]) -> str:
	return value_to_string(input, depth=-1)


def value_to_string(v: Union[str, dict, list, str, float, bool, None], depth=0) -> str:
	if isinstance(v, dict):
		return format_dict(v, depth=depth + 1)
	if isinstance(v, list):
		return format_list(v, depth=depth + 1)
	elif isinstance(v, str):
		return "'" + v + "'"
	elif isinstance(v, (float, int)):
		return str(v)
	elif isinstance(v, str):
		return v
	elif isinstance(v, bool):
		return 'True' if v else 'False'
	elif v is None:
		return 'None'
	else:
		raise FormattingException('unsupported type: {}'.format(v.__class__))


def format_dict(input: dict, depth=0) -> str:
	res = '{\n'

	for k, v in input.items():
		res += (depth + 1) * '\t'

		vs = value_to_string(v, depth)

		res += '\'{}\': {}'.format(k, vs)
		res += ',\n'

	res += depth * '\t' + '}'
	return res


def format_list(input: list, depth=0) -> str:
	res = '[\n'

	for v in input:
		res += (depth + 1) * '\t'

		vs = value_to_string(v, depth)

		res += vs + ',\n'

	res += depth * '\t' + ']'
	return res

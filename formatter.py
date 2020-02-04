def format_dict(input: dict, depth=0) -> str:
	res = '{\n'
	depth += 1

	for k, v in input.items():
		res += depth * '\t'

		if isinstance(v, dict):
			vp = format_dict(v, depth=depth)
		elif isinstance(v, str):
			vp = "'" + v + "'"
		elif isinstance(v, float):
			vp = str(v)


		res += '\'{}\': {}'.format(k, vp)
		res += ',\n'

	res += (depth - 1) * '\t' + '}'
	return res
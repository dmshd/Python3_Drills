import pprint

week = [{"id": f"2022_{i}", "text": f"2022 semaine {i}"} for i in range(46, 52)] + [{"id": f"2023_{i}", "text": f"2023 semaine {i}"} for i in range(2, 14)]

pprint.pprint(week)
from operator import itemgetter


def reversescan(**kwargs):
    try:
        # Here we will have a list { 'counter_403': X, 'counter_401': Y ... }
        data = kwargs["app"].config["INSTANCES"].get_metrics("reversescan")
        # Format to fit [{code: 403, count: X}, {code: 401, count: Y} ...]
        format_data = [{"port": int(key.split("_")[1]), "count": int(value)} for key, value in data.items()]
        format_data.sort(key=itemgetter("count"), reverse=True)
        return {"items": format_data}
    except:
        return {"items": []}

from traceback import format_exc


def pre_render(**kwargs):
    try:
        data = kwargs["app"].config["INSTANCES"].get_metrics("greylist")
        return {
            "counter_failed_greylist": {
                "value": data.get("counter_failed_greylist", 0),
                "title": "GREYLIST",
                "subtitle": "request blocked",
                "subtitle_color": "error",
                "svg_color": "red",
            }
        }
    except BaseException:
        print(format_exc(), flush=True)
        return {
            "counter_failed_greylist": {"value": "unknown", "title": "GREYLIST", "subtitle": "request blocked", "subtitle_color": "error", "svg_color": "red"},
            "error": format_exc(),
        }


def greylist(**kwargs):
    pass

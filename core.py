from locust import events
from locust.exception import StopLocust
import time
def wrapSeleniumEvent(request_type, name, func, *args, **kwargs):
    try:
        start_time = time.time()
        result = func(*args, **kwargs)
    except Exception as event_exception:
        total_time = int((time.time() - start_time) * 1000)
        events.request_failure.fire(
            request_type=request_type,
            name=name,
            response_time=total_time,
            exception=event_exception
        )
        raise StopLocust()
    else:
        total_time = int((time.time() - start_time) * 1000)
        events.request_success.fire(
            request_type=request_type,
            name=name,
            response_time=total_time,
            response_length=0
        )
        return result
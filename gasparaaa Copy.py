"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'hola' block
    hola(container=container)

    return

@phantom.playbook_block()
def hola(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("hola() called")

    ################################################################################
    # hola
    ################################################################################

    ################################################################################
    ## Custom Code Start
    ################################################################################

    def check_mv_domain(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
        mv_domain_values = phantom.collect2(container=container, datapath=["artifact:*.cef.mv_domain"])

        has_value = False
        for item in mv_domain_values:
            value = item[0] if item else None
            if value is not None:
                if isinstance(value, str) and value != "":
                    has_value = True
                    break
                elif isinstance(value, list) and len(value) > 0:
                    has_value = True
                    break

        phantom.save_run_data(key="mv_domain_has_value", value=str(has_value))
        return
    
    check_mv_domain()



    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_block_result(key="hola_called", value="True")

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return
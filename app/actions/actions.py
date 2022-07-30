# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from datetime import datetime

# For regex expressions
import re

# Validate Agent Form Inputs
class ValidateAgentForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_agent_form"

    def validate_agent_form_user_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate email address"""
        rgx_email = re.compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        )

        if re.fullmatch(rgx_email, slot_value):
            return {"agent_form_user_email": slot_value}
        else:
            dispatcher.utter_message(text="Please enter a valid email address.")
            return {"agent_form_user_email": None}

    def validate_agent_form_user_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate phone number"""
        if len(slot_value) < 8 or len(slot_value) > 8:
            dispatcher.utter_message(
                text="Please enter a 8-digit phone number that starts with 6, 8 or 9."
            )
            return {"agent_form_user_number": None}

        rgx_phone = re.compile(r"[6,8-9][0-9]{7}")

        if re.fullmatch(rgx_phone, slot_value):
            return {"agent_form_user_number": slot_value}
        else:
            dispatcher.utter_message(
                text="Please enter a 8-digit phone number that starts with 6, 8 or 9."
            )
            return {"agent_form_user_number": None}

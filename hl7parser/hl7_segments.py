# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from hl7parser.hl7_data_types import (
    HL7Datetime,
    HL7_MessageType,
    HL7_ExtendedCompositeId,
    HL7_ExtendedPersonName,
    HL7_ExtendedAddress,
    HL7_CodedWithException,
    HL7_ProcessingType,
    HL7_VersionIdentifier,
)

from hl7parser.hl7_data_types import make_cell_type

segment_maps = {
    'MSH': [
        make_cell_type(
            'encoding_characters',
            options={"required": True}),
        make_cell_type('sending_application'),
        make_cell_type('sending_facility'),
        make_cell_type('receiving_application'),
        make_cell_type('receiving_facility'),
        make_cell_type(
            'message_datetime',
            options={"repeats": True, "type": HL7Datetime}
        ),
        make_cell_type('security'),
        make_cell_type(
            'message_type',
            options={"required": True, "type": HL7_MessageType}
        ),
        make_cell_type('message_control_id', options={"required": True}),
        make_cell_type(
            'processing_id',
            options={"required": True, "type": HL7_ProcessingType}
        ),
        make_cell_type(
            'version_id',
            options={"required": True, "type": HL7_VersionIdentifier}
        ),
        make_cell_type('sequence_number'),
        make_cell_type('accept_acknowledgment_type'),
        make_cell_type('application_acknowledgment_type'),
        make_cell_type('country_code'),
        make_cell_type(
            'character_set',
            options={"repeats": True}
        ),
        make_cell_type(
            'principal_language_of_message',
            options={"type": HL7_CodedWithException}
        ),
        make_cell_type('alternate_character_set_handling_scheme'),
        make_cell_type(
            'message_profile_identifier',
            options={"repeats": True}
        ),
        make_cell_type('sending_responsible_organization'),
        make_cell_type('receiving_responsible_organization'),
        make_cell_type('sending_network_address'),
        make_cell_type('receiving_network_address'),
    ],
    "MSA": [
        make_cell_type('acknowledgement_code'),
        make_cell_type('message_control_id'),
        make_cell_type('text_message'),
    ],
    'EVN': [
        make_cell_type('event_type_code'),
        make_cell_type(
            'recorded_datetime',
            options={"required": True, "type": HL7Datetime}
        ),
        make_cell_type(
            'datetime_planned_event',
            options={"type": HL7Datetime}
        ),
        make_cell_type(
            'event_reason_code',
            options={"type": HL7_CodedWithException}
        ),
        make_cell_type('operator_id', options={"repeats": True}),
        make_cell_type('event_occured'),
        make_cell_type('event_facility'),
    ],
    'PID': [
        # (field name, repeats)
        make_cell_type('set_id_pid'),
        make_cell_type('patient_id'),
        make_cell_type(
            'patient_identifier_list',
            options={
                "required": True,
                "repeats": True,
                "type": HL7_ExtendedCompositeId
            }
        ),
        make_cell_type('alternate_patient_id_pid'),
        make_cell_type(
            'patient_name',
            options={
                "required": True,
                "repeats": True,
                "type": HL7_ExtendedPersonName
            }
        ),
        make_cell_type(
            'mothers_maiden_name',
            options={
                "repeats": True,
                "type": HL7_ExtendedPersonName
            }
        ),
        make_cell_type('datetime_of_birth', options={"type": HL7Datetime}),
        make_cell_type('administrative_sex'),
        make_cell_type('patient_alias'),
        make_cell_type(
            'race',
            options={
                "repeats": True,
                "type": HL7_CodedWithException
            }
        ),
        make_cell_type(
            'patient_address',
            options={
                "required": True,
                "repeats": True,
                "type": HL7_ExtendedAddress,
            }
        ),
        make_cell_type('county_code'),
        make_cell_type('phone_number_home', options={"repeats": True}),
        make_cell_type('phone_number_business', options={"repeats": True}),
        make_cell_type('primary_language'),
        make_cell_type('marital_status'),
        make_cell_type('religion'),
        make_cell_type('patient_account_number'),
        make_cell_type('ssn_number_patient'),
        make_cell_type('drivers_license_number_patient'),
        make_cell_type('mothers_identifier', options={"repeats": True}),
        make_cell_type('ethnic_group', options={"repeats": True}),
        make_cell_type('birth_place'),
        make_cell_type('multiple_birth_indicator'),
        make_cell_type('birth_order'),
        make_cell_type('citizenship', options={"repeats": True}),
        make_cell_type('veterans_military_status'),
        make_cell_type('nationality'),
        make_cell_type('patient_death_date_and_time'),
        make_cell_type('patient_death_indicator'),
        make_cell_type('identity_unknown_indicator'),
        make_cell_type('identity_reliability_code', options={"repeats": True}),
        make_cell_type('last_update_datetime'),
        make_cell_type('last_update_facility'),
        make_cell_type('species_code'),
        make_cell_type('breed_code'),
        make_cell_type('strain'),
        make_cell_type('production_class_code', options={"repeats": True}),
        make_cell_type('tribal_citizenship', options={"repeats": True}),
        make_cell_type(
            'patient_telecommunication_information',
            options={"repeats": True}
        )
    ],
    "MRG": [
        make_cell_type(
            'prior_patient_identifier_list',
            options={
                "required": True,
                "repeats": True,
                "type": HL7_ExtendedCompositeId
            }
        ),
        make_cell_type('prior_alternate_patient_id'),
        make_cell_type('prior_patient_account_number'),
        make_cell_type('prior_patient_id'),
        make_cell_type('prior_visit_number'),
        make_cell_type('prior_alternate_visit_id'),
        make_cell_type(
            'prior_patient_name',
            options={
                "repeats": True,
                "type": HL7_ExtendedPersonName
            }
        ),
    ],
}

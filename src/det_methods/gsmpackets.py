from scapy.all import *

class GSMTap(Packet):
    name = "GSMTap header"
    fields_desc = [XByteField("version", 0),
                   XByteField("header_length", 0),
                   XByteField("payload_type", 0),
                   XByteField("timeslot", 0, ),
                   XShortField("arfcn", 0),
                   XByteField("signal_level", 0), #Returns wrong value, should be signed
                   XByteField("signal_noise_ratio", 0),
                   XIntField("gsm_frame_number", 0),
                   XByteField("channel_type", 0),
                   XByteField("antenna_number", 0),
                   XByteField("sub_slot", 0),
                   XByteField("end_junk", 0)]


    def guess_payload_class(self, payload):
        if self.channel_type == 2:
            return CCCHCommon
        else:
            return Raw

class CCCHCommon(Packet):
    name = "CCCHCommon"
    fields_desc = [XShortField("junk1", 0),
                   XByteField("message_type", 0)]

    def guess_payload_class(self, payload):
        if self.message_type == 63:
            return ImmediateAssignment
        else:
            return Raw

class ImmediateAssignment(Packet):
    name = "ImmediateAssignment"
    fields_desc = [XByteField("junk", 2),
                   XByteField("packet_channel_description", 6) #Extract indivual bits for detailed information
                  ]

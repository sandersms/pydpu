# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bgp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import object_key_pb2 as object__key__pb2
import networktypes_pb2 as networktypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tbgp.proto\x12\x1eopi_api.network.cloud.v1alpha1\x1a\x10object_key.proto\x1a\x12networktypes.proto\"w\n\x03\x42gp\x12\x35\n\x04spec\x18\x01 \x01(\x0b\x32\'.opi_api.network.cloud.v1alpha1.BgpSpec\x12\x39\n\x06status\x18\x02 \x01(\x0b\x32).opi_api.network.cloud.v1alpha1.BgpStatus\"\xa3\x01\n\x07\x42gpSpec\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.opi_api.common.v1.ObjectKey\x12\x11\n\tlocal_asn\x18\x02 \x01(\r\x12\x11\n\trouter_id\x18\x03 \x01(\x07\x12\x12\n\ncluster_id\x18\x04 \x01(\x07\x12\x0f\n\x07\x64isable\x18\x05 \x01(\x08\x12#\n\x1bsuppress_default_resolution\x18\x06 \x01(\x08\"\xbe\x01\n\tBgpStatus\x12@\n\noper_state\x18\x01 \x01(\x0e\x32,.opi_api.network.cloud.v1alpha1.BGPOperState\x12 \n\x18\x61\x64j_rib_out_routes_count\x18\x02 \x01(\x05\x12#\n\x1bpeak_num_adj_rib_out_routes\x18\x03 \x01(\x05\x12\x15\n\rrem_delaytime\x18\x04 \x01(\x05\x12\x11\n\ttable_ver\x18\x05 \x01(\x05\"\x83\x01\n\x07\x42GPPeer\x12\x39\n\x04spec\x18\x01 \x01(\x0b\x32+.opi_api.network.cloud.v1alpha1.BGPPeerSpec\x12=\n\x06status\x18\x02 \x01(\x0b\x32-.opi_api.network.cloud.v1alpha1.BGPPeerStatus\"\x94\x04\n\x0b\x42GPPeerSpec\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.opi_api.common.v1.ObjectKey\x12@\n\x05state\x18\x02 \x01(\x0e\x32\x31.opi_api.network.opinetcommon.v1alpha1.AdminState\x12G\n\rlocal_address\x18\x03 \x01(\x0b\x32\x30.opi_api.network.opinetcommon.v1alpha1.IPAddress\x12\x43\n\tpeer_addr\x18\x04 \x01(\x0b\x32\x30.opi_api.network.opinetcommon.v1alpha1.IPAddress\x12\x12\n\nremote_asn\x18\x05 \x01(\r\x12\x11\n\tsend_comm\x18\x06 \x01(\x08\x12\x15\n\rsend_ext_comm\x18\x07 \x01(\x08\x12\x42\n\trr_client\x18\x08 \x01(\x0e\x32/.opi_api.network.cloud.v1alpha1.BGPPeerRRClient\x12\x15\n\rconnect_retry\x18\t \x01(\x05\x12\x10\n\x08holdtime\x18\n \x01(\x05\x12\x12\n\nkeep_alive\x18\x0b \x01(\x05\x12\x10\n\x08password\x18\x0c \x01(\x0c\x12\x0b\n\x03ttl\x18\r \x01(\x05\x12\x15\n\ridle_holdtime\x18\x0e \x01(\x05\x12\x16\n\x0e\x61llow_local_as\x18\x0f \x01(\x05\"\xe0\x0b\n\rBGPPeerStatus\x12J\n\rsession_state\x18\x01 \x01(\x0e\x32\x33.opi_api.network.cloud.v1alpha1.BGPPeerSessionState\x12O\n\x12prev_session_state\x18\x02 \x01(\x0e\x32\x33.opi_api.network.cloud.v1alpha1.BGPPeerSessionState\x12\x17\n\x0flast_error_rcvd\x18\x03 \x01(\x0c\x12\x17\n\x0flast_error_sent\x18\x04 \x01(\x0c\x12\x44\n\nlocal_addr\x18\x05 \x01(\x0b\x32\x30.opi_api.network.opinetcommon.v1alpha1.IPAddress\x12\x10\n\x08holdtime\x18\x06 \x01(\x05\x12\x11\n\tkeepalive\x18\x07 \x01(\x05\x12\x11\n\tcaps_sent\x18\x08 \x01(\x05\x12\x11\n\tcaps_rcvd\x18\t \x01(\x05\x12\x10\n\x08\x63\x61ps_neg\x18\n \x01(\x05\x12H\n\x13sel_local_addr_type\x18\x0b \x01(\x0e\x32+.opi_api.network.cloud.v1alpha1.BGPAddrType\x12\x1e\n\x16incoming_notifications\x18\x0c \x01(\x05\x12\x1e\n\x16outbound_notifications\x18\r \x01(\x05\x12\x18\n\x10incoming_updates\x18\x0e \x01(\x05\x12\x18\n\x10outgoing_updates\x18\x0f \x01(\x05\x12\x1b\n\x13incoming_keepalives\x18\x10 \x01(\x05\x12\x1b\n\x13outgoing_keepalives\x18\x11 \x01(\x05\x12\x1a\n\x12incoming_refreshes\x18\x12 \x01(\x05\x12\x1a\n\x12outgoing_refreshes\x18\x13 \x01(\x05\x12\x1f\n\x17incoming_total_messages\x18\x14 \x01(\x05\x12\x1f\n\x17outgoing_total_messages\x18\x15 \x01(\x05\x12\x1b\n\x13\x66sm_est_transitions\x18\x16 \x01(\x05\x12\x1b\n\x13\x63onnect_retry_count\x18\x17 \x01(\x05\x12\x0e\n\x06peergr\x18\x18 \x01(\x05\x12\x16\n\x0estale_pathtime\x18\x19 \x01(\x05\x12\x17\n\x0forf_entry_count\x18\x1a \x01(\x05\x12\x19\n\x11rcvd_msg_elpstime\x18\x1b \x01(\x05\x12\x17\n\x0froute_refr_sent\x18\x1c \x01(\x05\x12\x17\n\x0froute_refr_rcvd\x18\x1d \x01(\x05\x12\x17\n\x0fincoming_prfxes\x18\x1e \x01(\x05\x12\x17\n\x0foutgoing_prfxes\x18\x1f \x01(\x05\x12\"\n\x1aoutgoing_prfxes_advertised\x18  \x01(\x05\x12\x19\n\x11\x63onnect_retry_int\x18! \x01(\x05\x12 \n\x18outgoing_update_elpstime\x18\" \x01(\x05\x12\x1e\n\x16outgoing_prfxes_denied\x18# \x01(\x05\x12\x1f\n\x17outgoing_prfxes_imp_wdr\x18$ \x01(\x05\x12\x1f\n\x17outgoing_prfxes_exp_wdr\x18% \x01(\x05\x12\x1f\n\x17incoming_prfxes_imp_wdr\x18& \x01(\x05\x12\x1f\n\x17incoming_prfxes_exp_wdr\x18\' \x01(\x05\x12\x19\n\x11received_holdtime\x18( \x01(\x05\x12\x1b\n\x13\x66sm_establishedtime\x18) \x01(\x05\x12!\n\x19incoming_updates_elpstime\x18* \x01(\x05\x12\x16\n\x0eincoming_opens\x18+ \x01(\x05\x12\x16\n\x0eoutgoing_opens\x18, \x01(\x05\x12\x12\n\npeer_index\x18- \x01(\x05\x12\x0b\n\x03ttl\x18. \x01(\x05\x12@\n\noper_state\x18/ \x01(\x0e\x32,.opi_api.network.cloud.v1alpha1.BGPOperState\"\x88\x01\n\tBGPPeerAf\x12;\n\x04spec\x18\x01 \x01(\x0b\x32-.opi_api.network.cloud.v1alpha1.BGPPeerAfSpec\x12>\n\x05state\x18\x02 \x01(\x0b\x32/.opi_api.network.cloud.v1alpha1.BGPPeerAfStatus\"\xa2\x03\n\rBGPPeerAfSpec\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.opi_api.common.v1.ObjectKey\x12\x44\n\nlocal_addr\x18\x02 \x01(\x0b\x32\x30.opi_api.network.opinetcommon.v1alpha1.IPAddress\x12\x43\n\tpeer_addr\x18\x03 \x01(\x0b\x32\x30.opi_api.network.opinetcommon.v1alpha1.IPAddress\x12\x33\n\x03\x61\x66i\x18\x04 \x01(\x0e\x32&.opi_api.network.cloud.v1alpha1.BGPAfi\x12\x35\n\x04safi\x18\x05 \x01(\x0e\x32\'.opi_api.network.cloud.v1alpha1.BGPSafi\x12\x14\n\x0cnexthop_self\x18\x06 \x01(\x08\x12\x14\n\x0c\x64\x65\x66\x61ult_orig\x18\x07 \x01(\x08\x12\x12\n\nlocal_port\x18\x08 \x01(\x05\x12\x13\n\x0bremote_port\x18\t \x01(\x05\x12\x1b\n\x13local_addr_scope_id\x18\n \x01(\x05\"\xf5\x01\n\x0f\x42GPPeerAfStatus\x12\x14\n\x0cupdate_group\x18\x01 \x01(\x05\x12\x1b\n\x13local_addr_scope_id\x18\x02 \x01(\x05\x12\x15\n\rroute_refresh\x18\x03 \x01(\x08\x12M\n\x10\x61\x64\x64_path_cap_neg\x18\x04 \x01(\x0e\x32\x33.opi_api.network.cloud.v1alpha1.BgpAddPathCapNegCap\x12I\n\x10reflector_client\x18\x05 \x01(\x0e\x32/.opi_api.network.cloud.v1alpha1.BGPPeerRRClient\"\x94\x01\n\rBGPNLRIPrefix\x12?\n\x04spec\x18\x01 \x01(\x0b\x32\x31.opi_api.network.cloud.v1alpha1.BGPNLRIPrefixSpec\x12\x42\n\x05state\x18\x02 \x01(\x0b\x32\x33.opi_api.network.cloud.v1alpha1.BGPNLRIPrefixStatus\"\x8f\x02\n\x11\x42GPNLRIPrefixSpec\x12\x33\n\x03\x61\x66i\x18\x01 \x01(\x0e\x32&.opi_api.network.cloud.v1alpha1.BGPAfi\x12\x35\n\x04safi\x18\x02 \x01(\x0e\x32\'.opi_api.network.cloud.v1alpha1.BGPSafi\x12\x0e\n\x06prefix\x18\x03 \x01(\x0c\x12\x12\n\nprefix_len\x18\x04 \x01(\x05\x12=\n\x0croute_source\x18\x05 \x01(\x0e\x32\'.opi_api.network.cloud.v1alpha1.NLRISrc\x12\x1a\n\x12route_source_index\x18\x06 \x01(\x05\x12\x0f\n\x07path_id\x18\x07 \x01(\x05\"\xbc\x07\n\x13\x42GPNLRIPrefixStatus\x12\x33\n\x03\x61\x66i\x18\x01 \x01(\x0e\x32&.opi_api.network.cloud.v1alpha1.BGPAfi\x12\x35\n\x04safi\x18\x02 \x01(\x0e\x32\'.opi_api.network.cloud.v1alpha1.BGPSafi\x12\x0e\n\x06prefix\x18\x03 \x01(\x0c\x12\x12\n\nprefix_len\x18\x04 \x01(\x05\x12=\n\x0croute_source\x18\x05 \x01(\x0e\x32\'.opi_api.network.cloud.v1alpha1.NLRISrc\x12\x1a\n\x12route_source_index\x18\x06 \x01(\x05\x12\x0f\n\x07path_id\x18\x07 \x01(\x05\x12\x12\n\nbest_route\x18\x08 \x01(\x08\x12\x13\n\x0b\x61s_path_str\x18\t \x01(\x0c\x12\x14\n\x0cpath_orig_id\x18\n \x01(\x0c\x12\x15\n\rnext_hop_addr\x18\x0b \x01(\x0c\x12:\n\x07\x61s_size\x18\x0c \x01(\x0e\x32).opi_api.network.cloud.v1alpha1.BgpAsSize\x12\x12\n\necmp_route\x18\r \x01(\x08\x12\x43\n\tpeer_addr\x18\x0e \x01(\x0b\x32\x30.opi_api.network.opinetcommon.v1alpha1.IPAddress\x12\x1a\n\x12\x66lap_stats_flapcnt\x18\x0f \x01(\x05\x12\x1a\n\x12\x66lap_stats_supprsd\x18\x10 \x01(\x08\x12\x42\n\tis_active\x18\x11 \x01(\x0e\x32/.opi_api.network.cloud.v1alpha1.BgpNlriIsActive\x12\r\n\x05stale\x18\x12 \x01(\x08\x12\x16\n\x0e\x66lap_starttime\x18\x13 \x01(\x05\x12\x46\n\x0freason_not_best\x18\x14 \x01(\x0e\x32-.opi_api.network.cloud.v1alpha1.BGPRsnNotBest\x12\x10\n\x08\x65xt_comm\x18\x15 \x03(\x0c\x12\x0c\n\x04\x63omm\x18\x16 \x03(\x0c\x12\x12\n\nlocal_pref\x18\x17 \x01(\x05\x12=\n\x06origin\x18\x18 \x01(\x0e\x32-.opi_api.network.cloud.v1alpha1.BGPOriginAttr\x12\x13\n\x0bmed_present\x18\x19 \x01(\x08\x12\x0b\n\x03med\x18\x1a \x01(\r\x12>\n\tpeer_type\x18\x1b \x01(\x0e\x32+.opi_api.network.cloud.v1alpha1.BGPPeerType\"\xe1\x01\n\x13\x42GPNLRIPrefixFilter\x12\x10\n\x08\x65xt_comm\x18\x01 \x01(\x0c\x12\x0c\n\x04vnid\x18\x02 \x01(\x05\x12\x12\n\nroute_type\x18\x03 \x01(\x05\x12\x42\n\x08next_hop\x18\x04 \x01(\x0b\x32\x30.opi_api.network.opinetcommon.v1alpha1.IPAddress\x12\x44\n\nip_address\x18\x05 \x01(\x0b\x32\x30.opi_api.network.opinetcommon.v1alpha1.IPAddress\x12\x0c\n\x04\x62\x65st\x18\x06 \x01(\x08\"\x92\x01\n\x0c\x42GPAdjRibOut\x12>\n\x04spec\x18\x01 \x01(\x0b\x32\x30.opi_api.network.cloud.v1alpha1.BGPAdjRibOutSpec\x12\x42\n\x06status\x18\x02 \x01(\x0b\x32\x32.opi_api.network.cloud.v1alpha1.BGPAdjRibOutStatus\"\x12\n\x10\x42GPAdjRibOutSpec\"\xbe\x03\n\x12\x42GPAdjRibOutStatus\x12\x43\n\tpeer_addr\x18\x01 \x01(\x0b\x32\x30.opi_api.network.opinetcommon.v1alpha1.IPAddress\x12\x33\n\x03\x61\x66i\x18\x02 \x01(\x0e\x32&.opi_api.network.cloud.v1alpha1.BGPAfi\x12\x35\n\x04safi\x18\x03 \x01(\x0e\x32\'.opi_api.network.cloud.v1alpha1.BGPSafi\x12\x0e\n\x06prefix\x18\x04 \x01(\x0c\x12\x12\n\nprefix_len\x18\x05 \x01(\x05\x12@\n\x05state\x18\x06 \x01(\x0e\x32\x31.opi_api.network.cloud.v1alpha1.BgpAroAdvertState\x12:\n\x07\x61s_size\x18\x07 \x01(\x0e\x32).opi_api.network.cloud.v1alpha1.BgpAsSize\x12\x13\n\x0b\x61s_path_str\x18\x08 \x01(\x0c\x12\x0c\n\x04\x63omm\x18\t \x03(\x0c\x12\x10\n\x08\x65xt_comm\x18\n \x03(\x0c\x12\x13\n\x0bmed_present\x18\x0b \x01(\x08\x12\x0b\n\x03med\x18\x0c \x01(\r*X\n\x06\x42GPAfi\x12\x17\n\x13\x42GP_AFI_UNSPECIFIED\x10\x00\x12\x10\n\x0c\x42GP_AFI_IPV4\x10\x01\x12\x10\n\x0c\x42GP_AFI_IPV6\x10\x02\x12\x11\n\rBGP_AFI_L2VPN\x10\x19*L\n\x07\x42GPSafi\x12\x18\n\x14\x42GP_SAFI_UNSPECIFIED\x10\x00\x12\x14\n\x10\x42GP_SAFI_UNICAST\x10\x01\x12\x11\n\rBGP_SAFI_EVPN\x10\x46*l\n\x0f\x42GPPeerRRClient\x12\"\n\x1e\x42GP_PEER_RR_CLIENT_UNSPECIFIED\x10\x00\x12\x16\n\x12\x42GP_PEER_RR_CLIENT\x10\x01\x12\x1d\n\x19\x42GP_PEER_RR_MESHED_CLIENT\x10\x02*\x9a\x02\n\x13\x42GPPeerSessionState\x12&\n\"BGP_PEER_SESSION_STATE_UNSPECIFIED\x10\x00\x12\x1f\n\x1b\x42GP_PEER_SESSION_STATE_IDLE\x10\x01\x12\"\n\x1e\x42GP_PEER_SESSION_STATE_CONNECT\x10\x02\x12!\n\x1d\x42GP_PEER_SESSION_STATE_ACTIVE\x10\x03\x12#\n\x1f\x42GP_PEER_SESSION_STATE_OPENSENT\x10\x04\x12&\n\"BGP_PEER_SESSION_STATE_OPENCONFIRM\x10\x05\x12&\n\"BGP_PEER_SESSION_STATE_ESTABLISHED\x10\x06*_\n\tBgpAsSize\x12\x1b\n\x17\x42GP_AS_SIZE_UNSPECIFIED\x10\x00\x12\x19\n\x15\x42GP_AS_SIZE_TWO_OCTET\x10\x01\x12\x1a\n\x16\x42GP_AS_SIZE_FOUR_OCTET\x10\x02*\xd0\x04\n\x0b\x42GPAddrType\x12\x1d\n\x19\x42GP_ADDR_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12\x42GP_ADDR_TYPE_IPV4\x10\x01\x12\x16\n\x12\x42GP_ADDR_TYPE_IPV6\x10\x02\x12\x16\n\x12\x42GP_ADDR_TYPE_NSAP\x10\x03\x12\x16\n\x12\x42GP_ADDR_TYPE_HDLC\x10\x04\x12\x19\n\x15\x42GP_ADDR_TYPE_BBN1822\x10\x05\x12\x19\n\x15\x42GP_ADDR_TYPE_IEEE802\x10\x06\x12\x16\n\x12\x42GP_ADDR_TYPE_E163\x10\x07\x12\x16\n\x12\x42GP_ADDR_TYPE_E164\x10\x08\x12\x15\n\x11\x42GP_ADDR_TYPE_F69\x10\t\x12\x16\n\x12\x42GP_ADDR_TYPE_X121\x10\n\x12\x15\n\x11\x42GP_ADDR_TYPE_IPX\x10\x0b\x12\x1b\n\x17\x42GP_ADDR_TYPE_APPLETALK\x10\x0c\x12\x1a\n\x16\x42GP_ADDR_TYPE_DECNETIV\x10\r\x12\x1b\n\x17\x42GP_ADDR_TYPE_BANYANVIN\x10\x0e\x12\x1b\n\x17\x42GP_ADDR_TYPE_E164_NSAP\x10\x0f\x12\x1a\n\x16\x42GP_ADDR_TYPE_IPV4_TNA\x10\x10\x12\x1a\n\x16\x42GP_ADDR_TYPE_IPV6_TNA\x10\x11\x12\x1a\n\x16\x42GP_ADDR_TYPE_NSAP_TNA\x10\x12\x12\x1a\n\x16\x42GP_ADDR_TYPE_VPN_IPV4\x10\x13\x12\x1a\n\x16\x42GP_ADDR_TYPE_VPN_IPV6\x10\x14\x12\x17\n\x13\x42GP_ADDR_TYPE_L2VPN\x10\x19*\xb9\x01\n\x0c\x42GPOperState\x12\x1e\n\x1a\x42GP_OPER_STATE_UNSPECIFIED\x10\x00\x12\x15\n\x11\x42GP_OPER_STATE_UP\x10\x01\x12\x17\n\x13\x42GP_OPER_STATE_DOWN\x10\x02\x12\x1b\n\x17\x42GP_OPER_STATE_GOING_UP\x10\x03\x12\x1d\n\x19\x42GP_OPER_STATE_GOING_DOWN\x10\x04\x12\x1d\n\x19\x42GP_OPER_STATE_ACT_FAILED\x10\x05*\xbd\x01\n\x13\x42gpAddPathCapNegCap\x12\x1b\n\x17\x42GP_ADD_PATH_SR_DISABLE\x10\x00\x12\x1b\n\x17\x42GP_ADD_PATH_SR_RECEIVE\x10\x01\x12\x18\n\x14\x42GP_ADD_PATH_SR_SEND\x10\x02\x12\x18\n\x14\x42GP_ADD_PATH_SR_BOTH\x10\x03\x12\x1b\n\x17\x42GP_ADD_PATH_SR_INHERIT\x10\x04\x12\x1b\n\x17\x42GP_ADD_PATH_SR_UNKNOWN\x10\x05*\xdc\x01\n\x14\x42GPClearRouteOptions\x12\'\n#BGP_CLEAR_ROUTE_OPTIONS_UNSPECIFIED\x10\x00\x12 \n\x1c\x42GP_CLEAR_ROUTE_OPTIONS_HARD\x10\x01\x12&\n\"BGP_CLEAR_ROUTE_OPTIONS_REFRESH_IN\x10\x02\x12\'\n#BGP_CLEAR_ROUTE_OPTIONS_REFRESH_OUT\x10\x03\x12(\n$BGP_CLEAR_ROUTE_OPTIONS_REFRESH_BOTH\x10\x04*[\n\x07NLRISrc\x12\x18\n\x14NLRI_SRC_UNSPECIFIED\x10\x00\x12\x11\n\rNLRI_SRC_PEER\x10\x01\x12\x10\n\x0cNLRI_SRC_AFM\x10\x02\x12\x11\n\rNLRI_SRC_SELF\x10\x03*\x99\x01\n\x0f\x42gpNlriIsActive\x12\"\n\x1e\x42GP_NLRI_IS_ACTIVE_UNSPECIFIED\x10\x00\x12\"\n\x1e\x42GP_NLRI_IS_ACTIVE_NOT_TRACKED\x10\x01\x12\x1f\n\x1b\x42GP_NLRI_IS_ACTIVE_INACTIVE\x10\x02\x12\x1d\n\x19\x42GP_NLRI_IS_ACTIVE_ACTIVE\x10\x03*\xa6\x04\n\rBGPRsnNotBest\x12\x1d\n\x19\x42GP_REASON_NOT_CONSIDERED\x10\x00\x12\x1c\n\x18\x42GP_REASON_ROUTE_IS_BEST\x10\x01\x12\x15\n\x11\x42GP_REASON_WEIGHT\x10\x02\x12\x19\n\x15\x42GP_REASON_LOCAL_PREF\x10\x03\x12\x1f\n\x1b\x42GP_REASON_LCL_ORIG_PRFRRED\x10\x04\x12\x1a\n\x16\x42GP_REASON_AS_PATH_LEN\x10\x05\x12\x15\n\x11\x42GP_REASON_ORIGIN\x10\x06\x12\x12\n\x0e\x42GP_REASON_MED\x10\x07\x12\x1d\n\x19\x42GP_REASON_LOCAL_ORIG_TIE\x10\x08\x12\x1f\n\x1b\x42GP_REASON_EBGP_V_IBGP_PEER\x10\t\x12\x1d\n\x19\x42GP_REASON_ADMIN_DISTANCE\x10\n\x12\x1f\n\x1b\x42GP_REASON_PATH_TO_NEXT_CST\x10\x0b\x12\x1c\n\x18\x42GP_REASON_PREF_EXISTING\x10\x0c\x12\x19\n\x15\x42GP_REASON_IDENTIFIER\x10\r\x12\x1a\n\x16\x42GP_REASON_CLUSTER_LEN\x10\x0e\x12\x1d\n\x19\x42GP_REASON_PEER_ADDR_TYPE\x10\x0f\x12\x18\n\x14\x42GP_REASON_PEER_ADDR\x10\x10\x12\x18\n\x14\x42GP_REASON_PEER_PORT\x10\x11\x12\x16\n\x12\x42GP_REASON_PATH_ID\x10\x12*\x82\x01\n\rBGPOriginAttr\x12\x1f\n\x1b\x42GP_ORIGIN_ATTR_UNSPECIFIED\x10\x00\x12\x17\n\x13\x42GP_ORIGIN_ATTR_IGP\x10\x01\x12\x17\n\x13\x42GP_ORIGIN_ATTR_EGP\x10\x02\x12\x1e\n\x1a\x42GP_ORIGIN_ATTR_INCOMPLETE\x10\x03*t\n\x0b\x42GPPeerType\x12\x1d\n\x19\x42GP_PEER_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12\x42GP_PEER_TYPE_NONE\x10\x01\x12\x16\n\x12\x42GP_PEER_TYPE_IBGP\x10\x02\x12\x16\n\x12\x42GP_PEER_TYPE_EBGP\x10\x03*\xd4\x01\n\x11\x42gpAroAdvertState\x12$\n BGP_ARO_ADVERT_STATE_UNSPECIFIED\x10\x00\x12#\n\x1f\x42GP_ARO_ADVERT_STATE_ADVERTISED\x10\x01\x12#\n\x1f\x42GP_ARO_ADVERT_STATE_SUPPRESSED\x10\x02\x12+\n\'BGP_ARO_ADVERT_STATE_PENDING_WITHDRAWAL\x10\x03\x12\"\n\x1e\x42GP_ARO_ADVERT_STATE_WITHDRAWN\x10\x04\x42i\n\x1eopi_api.network.cloud.v1alpha1B\x08\x42GPProtoP\x01Z;github.com/opiproject/opi-api/network/cloud/v1alpha1/gen/gob\x06proto3')

_BGPAFI = DESCRIPTOR.enum_types_by_name['BGPAfi']
BGPAfi = enum_type_wrapper.EnumTypeWrapper(_BGPAFI)
_BGPSAFI = DESCRIPTOR.enum_types_by_name['BGPSafi']
BGPSafi = enum_type_wrapper.EnumTypeWrapper(_BGPSAFI)
_BGPPEERRRCLIENT = DESCRIPTOR.enum_types_by_name['BGPPeerRRClient']
BGPPeerRRClient = enum_type_wrapper.EnumTypeWrapper(_BGPPEERRRCLIENT)
_BGPPEERSESSIONSTATE = DESCRIPTOR.enum_types_by_name['BGPPeerSessionState']
BGPPeerSessionState = enum_type_wrapper.EnumTypeWrapper(_BGPPEERSESSIONSTATE)
_BGPASSIZE = DESCRIPTOR.enum_types_by_name['BgpAsSize']
BgpAsSize = enum_type_wrapper.EnumTypeWrapper(_BGPASSIZE)
_BGPADDRTYPE = DESCRIPTOR.enum_types_by_name['BGPAddrType']
BGPAddrType = enum_type_wrapper.EnumTypeWrapper(_BGPADDRTYPE)
_BGPOPERSTATE = DESCRIPTOR.enum_types_by_name['BGPOperState']
BGPOperState = enum_type_wrapper.EnumTypeWrapper(_BGPOPERSTATE)
_BGPADDPATHCAPNEGCAP = DESCRIPTOR.enum_types_by_name['BgpAddPathCapNegCap']
BgpAddPathCapNegCap = enum_type_wrapper.EnumTypeWrapper(_BGPADDPATHCAPNEGCAP)
_BGPCLEARROUTEOPTIONS = DESCRIPTOR.enum_types_by_name['BGPClearRouteOptions']
BGPClearRouteOptions = enum_type_wrapper.EnumTypeWrapper(_BGPCLEARROUTEOPTIONS)
_NLRISRC = DESCRIPTOR.enum_types_by_name['NLRISrc']
NLRISrc = enum_type_wrapper.EnumTypeWrapper(_NLRISRC)
_BGPNLRIISACTIVE = DESCRIPTOR.enum_types_by_name['BgpNlriIsActive']
BgpNlriIsActive = enum_type_wrapper.EnumTypeWrapper(_BGPNLRIISACTIVE)
_BGPRSNNOTBEST = DESCRIPTOR.enum_types_by_name['BGPRsnNotBest']
BGPRsnNotBest = enum_type_wrapper.EnumTypeWrapper(_BGPRSNNOTBEST)
_BGPORIGINATTR = DESCRIPTOR.enum_types_by_name['BGPOriginAttr']
BGPOriginAttr = enum_type_wrapper.EnumTypeWrapper(_BGPORIGINATTR)
_BGPPEERTYPE = DESCRIPTOR.enum_types_by_name['BGPPeerType']
BGPPeerType = enum_type_wrapper.EnumTypeWrapper(_BGPPEERTYPE)
_BGPAROADVERTSTATE = DESCRIPTOR.enum_types_by_name['BgpAroAdvertState']
BgpAroAdvertState = enum_type_wrapper.EnumTypeWrapper(_BGPAROADVERTSTATE)
BGP_AFI_UNSPECIFIED = 0
BGP_AFI_IPV4 = 1
BGP_AFI_IPV6 = 2
BGP_AFI_L2VPN = 25
BGP_SAFI_UNSPECIFIED = 0
BGP_SAFI_UNICAST = 1
BGP_SAFI_EVPN = 70
BGP_PEER_RR_CLIENT_UNSPECIFIED = 0
BGP_PEER_RR_CLIENT = 1
BGP_PEER_RR_MESHED_CLIENT = 2
BGP_PEER_SESSION_STATE_UNSPECIFIED = 0
BGP_PEER_SESSION_STATE_IDLE = 1
BGP_PEER_SESSION_STATE_CONNECT = 2
BGP_PEER_SESSION_STATE_ACTIVE = 3
BGP_PEER_SESSION_STATE_OPENSENT = 4
BGP_PEER_SESSION_STATE_OPENCONFIRM = 5
BGP_PEER_SESSION_STATE_ESTABLISHED = 6
BGP_AS_SIZE_UNSPECIFIED = 0
BGP_AS_SIZE_TWO_OCTET = 1
BGP_AS_SIZE_FOUR_OCTET = 2
BGP_ADDR_TYPE_UNSPECIFIED = 0
BGP_ADDR_TYPE_IPV4 = 1
BGP_ADDR_TYPE_IPV6 = 2
BGP_ADDR_TYPE_NSAP = 3
BGP_ADDR_TYPE_HDLC = 4
BGP_ADDR_TYPE_BBN1822 = 5
BGP_ADDR_TYPE_IEEE802 = 6
BGP_ADDR_TYPE_E163 = 7
BGP_ADDR_TYPE_E164 = 8
BGP_ADDR_TYPE_F69 = 9
BGP_ADDR_TYPE_X121 = 10
BGP_ADDR_TYPE_IPX = 11
BGP_ADDR_TYPE_APPLETALK = 12
BGP_ADDR_TYPE_DECNETIV = 13
BGP_ADDR_TYPE_BANYANVIN = 14
BGP_ADDR_TYPE_E164_NSAP = 15
BGP_ADDR_TYPE_IPV4_TNA = 16
BGP_ADDR_TYPE_IPV6_TNA = 17
BGP_ADDR_TYPE_NSAP_TNA = 18
BGP_ADDR_TYPE_VPN_IPV4 = 19
BGP_ADDR_TYPE_VPN_IPV6 = 20
BGP_ADDR_TYPE_L2VPN = 25
BGP_OPER_STATE_UNSPECIFIED = 0
BGP_OPER_STATE_UP = 1
BGP_OPER_STATE_DOWN = 2
BGP_OPER_STATE_GOING_UP = 3
BGP_OPER_STATE_GOING_DOWN = 4
BGP_OPER_STATE_ACT_FAILED = 5
BGP_ADD_PATH_SR_DISABLE = 0
BGP_ADD_PATH_SR_RECEIVE = 1
BGP_ADD_PATH_SR_SEND = 2
BGP_ADD_PATH_SR_BOTH = 3
BGP_ADD_PATH_SR_INHERIT = 4
BGP_ADD_PATH_SR_UNKNOWN = 5
BGP_CLEAR_ROUTE_OPTIONS_UNSPECIFIED = 0
BGP_CLEAR_ROUTE_OPTIONS_HARD = 1
BGP_CLEAR_ROUTE_OPTIONS_REFRESH_IN = 2
BGP_CLEAR_ROUTE_OPTIONS_REFRESH_OUT = 3
BGP_CLEAR_ROUTE_OPTIONS_REFRESH_BOTH = 4
NLRI_SRC_UNSPECIFIED = 0
NLRI_SRC_PEER = 1
NLRI_SRC_AFM = 2
NLRI_SRC_SELF = 3
BGP_NLRI_IS_ACTIVE_UNSPECIFIED = 0
BGP_NLRI_IS_ACTIVE_NOT_TRACKED = 1
BGP_NLRI_IS_ACTIVE_INACTIVE = 2
BGP_NLRI_IS_ACTIVE_ACTIVE = 3
BGP_REASON_NOT_CONSIDERED = 0
BGP_REASON_ROUTE_IS_BEST = 1
BGP_REASON_WEIGHT = 2
BGP_REASON_LOCAL_PREF = 3
BGP_REASON_LCL_ORIG_PRFRRED = 4
BGP_REASON_AS_PATH_LEN = 5
BGP_REASON_ORIGIN = 6
BGP_REASON_MED = 7
BGP_REASON_LOCAL_ORIG_TIE = 8
BGP_REASON_EBGP_V_IBGP_PEER = 9
BGP_REASON_ADMIN_DISTANCE = 10
BGP_REASON_PATH_TO_NEXT_CST = 11
BGP_REASON_PREF_EXISTING = 12
BGP_REASON_IDENTIFIER = 13
BGP_REASON_CLUSTER_LEN = 14
BGP_REASON_PEER_ADDR_TYPE = 15
BGP_REASON_PEER_ADDR = 16
BGP_REASON_PEER_PORT = 17
BGP_REASON_PATH_ID = 18
BGP_ORIGIN_ATTR_UNSPECIFIED = 0
BGP_ORIGIN_ATTR_IGP = 1
BGP_ORIGIN_ATTR_EGP = 2
BGP_ORIGIN_ATTR_INCOMPLETE = 3
BGP_PEER_TYPE_UNSPECIFIED = 0
BGP_PEER_TYPE_NONE = 1
BGP_PEER_TYPE_IBGP = 2
BGP_PEER_TYPE_EBGP = 3
BGP_ARO_ADVERT_STATE_UNSPECIFIED = 0
BGP_ARO_ADVERT_STATE_ADVERTISED = 1
BGP_ARO_ADVERT_STATE_SUPPRESSED = 2
BGP_ARO_ADVERT_STATE_PENDING_WITHDRAWAL = 3
BGP_ARO_ADVERT_STATE_WITHDRAWN = 4


_BGP = DESCRIPTOR.message_types_by_name['Bgp']
_BGPSPEC = DESCRIPTOR.message_types_by_name['BgpSpec']
_BGPSTATUS = DESCRIPTOR.message_types_by_name['BgpStatus']
_BGPPEER = DESCRIPTOR.message_types_by_name['BGPPeer']
_BGPPEERSPEC = DESCRIPTOR.message_types_by_name['BGPPeerSpec']
_BGPPEERSTATUS = DESCRIPTOR.message_types_by_name['BGPPeerStatus']
_BGPPEERAF = DESCRIPTOR.message_types_by_name['BGPPeerAf']
_BGPPEERAFSPEC = DESCRIPTOR.message_types_by_name['BGPPeerAfSpec']
_BGPPEERAFSTATUS = DESCRIPTOR.message_types_by_name['BGPPeerAfStatus']
_BGPNLRIPREFIX = DESCRIPTOR.message_types_by_name['BGPNLRIPrefix']
_BGPNLRIPREFIXSPEC = DESCRIPTOR.message_types_by_name['BGPNLRIPrefixSpec']
_BGPNLRIPREFIXSTATUS = DESCRIPTOR.message_types_by_name['BGPNLRIPrefixStatus']
_BGPNLRIPREFIXFILTER = DESCRIPTOR.message_types_by_name['BGPNLRIPrefixFilter']
_BGPADJRIBOUT = DESCRIPTOR.message_types_by_name['BGPAdjRibOut']
_BGPADJRIBOUTSPEC = DESCRIPTOR.message_types_by_name['BGPAdjRibOutSpec']
_BGPADJRIBOUTSTATUS = DESCRIPTOR.message_types_by_name['BGPAdjRibOutStatus']
Bgp = _reflection.GeneratedProtocolMessageType('Bgp', (_message.Message,), {
  'DESCRIPTOR' : _BGP,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.Bgp)
  })
_sym_db.RegisterMessage(Bgp)

BgpSpec = _reflection.GeneratedProtocolMessageType('BgpSpec', (_message.Message,), {
  'DESCRIPTOR' : _BGPSPEC,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BgpSpec)
  })
_sym_db.RegisterMessage(BgpSpec)

BgpStatus = _reflection.GeneratedProtocolMessageType('BgpStatus', (_message.Message,), {
  'DESCRIPTOR' : _BGPSTATUS,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BgpStatus)
  })
_sym_db.RegisterMessage(BgpStatus)

BGPPeer = _reflection.GeneratedProtocolMessageType('BGPPeer', (_message.Message,), {
  'DESCRIPTOR' : _BGPPEER,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPPeer)
  })
_sym_db.RegisterMessage(BGPPeer)

BGPPeerSpec = _reflection.GeneratedProtocolMessageType('BGPPeerSpec', (_message.Message,), {
  'DESCRIPTOR' : _BGPPEERSPEC,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPPeerSpec)
  })
_sym_db.RegisterMessage(BGPPeerSpec)

BGPPeerStatus = _reflection.GeneratedProtocolMessageType('BGPPeerStatus', (_message.Message,), {
  'DESCRIPTOR' : _BGPPEERSTATUS,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPPeerStatus)
  })
_sym_db.RegisterMessage(BGPPeerStatus)

BGPPeerAf = _reflection.GeneratedProtocolMessageType('BGPPeerAf', (_message.Message,), {
  'DESCRIPTOR' : _BGPPEERAF,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPPeerAf)
  })
_sym_db.RegisterMessage(BGPPeerAf)

BGPPeerAfSpec = _reflection.GeneratedProtocolMessageType('BGPPeerAfSpec', (_message.Message,), {
  'DESCRIPTOR' : _BGPPEERAFSPEC,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPPeerAfSpec)
  })
_sym_db.RegisterMessage(BGPPeerAfSpec)

BGPPeerAfStatus = _reflection.GeneratedProtocolMessageType('BGPPeerAfStatus', (_message.Message,), {
  'DESCRIPTOR' : _BGPPEERAFSTATUS,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPPeerAfStatus)
  })
_sym_db.RegisterMessage(BGPPeerAfStatus)

BGPNLRIPrefix = _reflection.GeneratedProtocolMessageType('BGPNLRIPrefix', (_message.Message,), {
  'DESCRIPTOR' : _BGPNLRIPREFIX,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPNLRIPrefix)
  })
_sym_db.RegisterMessage(BGPNLRIPrefix)

BGPNLRIPrefixSpec = _reflection.GeneratedProtocolMessageType('BGPNLRIPrefixSpec', (_message.Message,), {
  'DESCRIPTOR' : _BGPNLRIPREFIXSPEC,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPNLRIPrefixSpec)
  })
_sym_db.RegisterMessage(BGPNLRIPrefixSpec)

BGPNLRIPrefixStatus = _reflection.GeneratedProtocolMessageType('BGPNLRIPrefixStatus', (_message.Message,), {
  'DESCRIPTOR' : _BGPNLRIPREFIXSTATUS,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPNLRIPrefixStatus)
  })
_sym_db.RegisterMessage(BGPNLRIPrefixStatus)

BGPNLRIPrefixFilter = _reflection.GeneratedProtocolMessageType('BGPNLRIPrefixFilter', (_message.Message,), {
  'DESCRIPTOR' : _BGPNLRIPREFIXFILTER,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPNLRIPrefixFilter)
  })
_sym_db.RegisterMessage(BGPNLRIPrefixFilter)

BGPAdjRibOut = _reflection.GeneratedProtocolMessageType('BGPAdjRibOut', (_message.Message,), {
  'DESCRIPTOR' : _BGPADJRIBOUT,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPAdjRibOut)
  })
_sym_db.RegisterMessage(BGPAdjRibOut)

BGPAdjRibOutSpec = _reflection.GeneratedProtocolMessageType('BGPAdjRibOutSpec', (_message.Message,), {
  'DESCRIPTOR' : _BGPADJRIBOUTSPEC,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPAdjRibOutSpec)
  })
_sym_db.RegisterMessage(BGPAdjRibOutSpec)

BGPAdjRibOutStatus = _reflection.GeneratedProtocolMessageType('BGPAdjRibOutStatus', (_message.Message,), {
  'DESCRIPTOR' : _BGPADJRIBOUTSTATUS,
  '__module__' : 'bgp_pb2'
  # @@protoc_insertion_point(class_scope:opi_api.network.cloud.v1alpha1.BGPAdjRibOutStatus)
  })
_sym_db.RegisterMessage(BGPAdjRibOutStatus)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036opi_api.network.cloud.v1alpha1B\010BGPProtoP\001Z;github.com/opiproject/opi-api/network/cloud/v1alpha1/gen/go'
  _BGPAFI._serialized_start=5777
  _BGPAFI._serialized_end=5865
  _BGPSAFI._serialized_start=5867
  _BGPSAFI._serialized_end=5943
  _BGPPEERRRCLIENT._serialized_start=5945
  _BGPPEERRRCLIENT._serialized_end=6053
  _BGPPEERSESSIONSTATE._serialized_start=6056
  _BGPPEERSESSIONSTATE._serialized_end=6338
  _BGPASSIZE._serialized_start=6340
  _BGPASSIZE._serialized_end=6435
  _BGPADDRTYPE._serialized_start=6438
  _BGPADDRTYPE._serialized_end=7030
  _BGPOPERSTATE._serialized_start=7033
  _BGPOPERSTATE._serialized_end=7218
  _BGPADDPATHCAPNEGCAP._serialized_start=7221
  _BGPADDPATHCAPNEGCAP._serialized_end=7410
  _BGPCLEARROUTEOPTIONS._serialized_start=7413
  _BGPCLEARROUTEOPTIONS._serialized_end=7633
  _NLRISRC._serialized_start=7635
  _NLRISRC._serialized_end=7726
  _BGPNLRIISACTIVE._serialized_start=7729
  _BGPNLRIISACTIVE._serialized_end=7882
  _BGPRSNNOTBEST._serialized_start=7885
  _BGPRSNNOTBEST._serialized_end=8435
  _BGPORIGINATTR._serialized_start=8438
  _BGPORIGINATTR._serialized_end=8568
  _BGPPEERTYPE._serialized_start=8570
  _BGPPEERTYPE._serialized_end=8686
  _BGPAROADVERTSTATE._serialized_start=8689
  _BGPAROADVERTSTATE._serialized_end=8901
  _BGP._serialized_start=83
  _BGP._serialized_end=202
  _BGPSPEC._serialized_start=205
  _BGPSPEC._serialized_end=368
  _BGPSTATUS._serialized_start=371
  _BGPSTATUS._serialized_end=561
  _BGPPEER._serialized_start=564
  _BGPPEER._serialized_end=695
  _BGPPEERSPEC._serialized_start=698
  _BGPPEERSPEC._serialized_end=1230
  _BGPPEERSTATUS._serialized_start=1233
  _BGPPEERSTATUS._serialized_end=2737
  _BGPPEERAF._serialized_start=2740
  _BGPPEERAF._serialized_end=2876
  _BGPPEERAFSPEC._serialized_start=2879
  _BGPPEERAFSPEC._serialized_end=3297
  _BGPPEERAFSTATUS._serialized_start=3300
  _BGPPEERAFSTATUS._serialized_end=3545
  _BGPNLRIPREFIX._serialized_start=3548
  _BGPNLRIPREFIX._serialized_end=3696
  _BGPNLRIPREFIXSPEC._serialized_start=3699
  _BGPNLRIPREFIXSPEC._serialized_end=3970
  _BGPNLRIPREFIXSTATUS._serialized_start=3973
  _BGPNLRIPREFIXSTATUS._serialized_end=4929
  _BGPNLRIPREFIXFILTER._serialized_start=4932
  _BGPNLRIPREFIXFILTER._serialized_end=5157
  _BGPADJRIBOUT._serialized_start=5160
  _BGPADJRIBOUT._serialized_end=5306
  _BGPADJRIBOUTSPEC._serialized_start=5308
  _BGPADJRIBOUTSPEC._serialized_end=5326
  _BGPADJRIBOUTSTATUS._serialized_start=5329
  _BGPADJRIBOUTSTATUS._serialized_end=5775
# @@protoc_insertion_point(module_scope)

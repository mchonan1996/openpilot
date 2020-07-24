#!/usr/bin/env python3
import os
import time
from cereal import car
from opendbc.can.parser import CANParser
from selfdrive.car.interfaces import RadarInterfaceBase
from selfdrive.car.subaru.values import DBC

def get_eyesight_can_parser(CP):
  signals = [
    # sig_name, sig_address, default
    ("Car_Follow", "ES_DashStatus", 0),
    ("Far_Distance", "ES_DashStatus", 0),

    ("Close_Distance", "ES_Distance", 0),
    ("Distance_Swap", "ES_Distance", 0),
  ]
  checks = [
    # address, frequency
    ("ES_DashStatus", 10),
    ("ES_Distance", 20),
  ]
  return CANParser(DBC[CP.carFingerprint]['pt'], signals, checks, 0)

class RadarInterface(RadarInterfaceBase):
  def __init__(self, CP):
    super().__init__(CP)
    self.canParser = get_eyesight_can_parser(CP)
    self.updated_messages = set()
    self.trigger_msg = 0x221 # 0x221 - ES_Distance 20Hz | 0x321 - ES_DashStatus 10Hz
    self.track_id = 0
    self.radar_off_can = CP.radarOffCan

  def update(self, can_strings):
    if self.radar_off_can:
      if 'NO_RADAR_SLEEP' not in os.environ:
        time.sleep(0.05)  # radard runs on RI updates

      return car.RadarData.new_message()

    vls = self.canParser.update_strings(can_strings)
    self.updated_messages.update(vls)

    if self.trigger_msg not in self.updated_messages:
      return None

    rr = self._update(self.updated_messages)
    print('RI: rr', rr)
    self.updated_messages.clear()

    return rr

  def _update(self, updated_messages):
    ret = car.RadarData.new_message()
    cpt = self.canParser.vl
    errors = []
    if not self.canParser.can_valid:
      errors.append("canError")
    ret.errors = errors

    valid = cpt["ES_DashStatus"]['Car_Follow'] == 1
    print('RI: Valid', valid)
    if valid:
      far_distance = cpt['ES_DashStatus']['Far_Distance']
      print('RI: far_distance', far_distance)
      close_distance = cpt['ES_Distance']['Close_Distance']
      print('RI: close_distance', close_distance)

      for ii in range(2):
        if ii not in self.pts:
          self.pts[ii] = car.RadarData.RadarPoint.new_message()
          self.pts[ii].trackId = self.track_id
          self.track_id += 1
        my_drel = (close_distance * 6 / 255) if close_distance < 255 else (far_distance * 5) # from front of car
        print('RI: my_drel', my_drel)
        self.pts[ii].dRel = my_drel
        self.pts[ii].yRel = 0 # in car frame's y axis, left is negative
        self.pts[ii].vRel = 0
        self.pts[ii].aRel = float('nan')
        self.pts[ii].yvRel = float('nan')
        self.pts[ii].measured = (close_distance < 255)

    ret.points = list(self.pts.values())
    return ret

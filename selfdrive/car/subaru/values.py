from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu

class CAR:
  IMPREZA = "SUBARU IMPREZA LIMITED 2019"

FINGERPRINTS = {
  CAR.IMPREZA: [{
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 544: 8, 545: 8, 546: 8, 552: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1722: 8, 1743: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8, 1809: 8, 1813: 8, 1817: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8
  },
  # Crosstrek 2018 (same platform as Impreza)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 256: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 544: 8, 545: 8, 546: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 811: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8
  }],
}

FW_VERSIONS = {
  CAR.IMPREZA: {
    # Ecu, addr, subaddr: ROM ID
    (Ecu.esp, 0x7b0, None): [b'\x7a\x94\x3f\x90\x00'],
    (Ecu.eps, 0x746, None): [b'\x7a\xc0\x0c\x00'],
    (Ecu.srs, 0x780, None): [b'\x00\x92\x15\x16\x00'],
    (Ecu.fwdCamera, 0x787, None): [b'\x00\x00\x64\xb5\x1f\x40\x20\x0e'],
    (Ecu.engine, 0x7e0, None): [b'\xaa\x61\x66\x73\x07'],
    (Ecu.transmission, 0x7e1, None): [b'\xe3\xe5\x46\x31\x00'],
  },
}


STEER_THRESHOLD = {
  CAR.IMPREZA: 80,
}

ECU_FINGERPRINT = {
  Ecu.fwdCamera: [290, 356],   # steer torque cmd
}

DBC = {
  CAR.IMPREZA: dbc_dict('subaru_global_2017', None),
}

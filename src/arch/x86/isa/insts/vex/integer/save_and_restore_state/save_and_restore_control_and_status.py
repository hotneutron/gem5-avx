microcode = '''
def macroop VEX_VSTMXCSR_M {
    rdval t1, "InstRegIndex(MISCREG_MXCSR)"
    st t1, seg, sib, disp
};

def macroop VEX_VSTMXCSR_P {
    rdval t1, "InstRegIndex(MISCREG_MXCSR)"
    rdip t7
    st t1, seg, riprel, disp
};

def macroop VEX_VLDMXCSR_M {
    ld t1, seg, sib, disp
    wrval "InstRegIndex(MISCREG_MXCSR)", t1
};

def macroop VEX_VLDMXCSR_P {
    rdip t7
    ld t1, seg, riprel, disp
    wrval "InstRegIndex(MISCREG_MXCSR)", t1
};
'''

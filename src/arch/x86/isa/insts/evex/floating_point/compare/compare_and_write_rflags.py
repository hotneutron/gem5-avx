microcode = '''
def macroop EVEX_VUCOMISS_XMM_XMM {
    sse_mcmpf2rf xmm, xmmm, size=4
};

def macroop EVEX_VUCOMISS_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    sse_mcmpf2rf xmm, uvec1, size=4
};

def macroop EVEX_VUCOMISS_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    sse_mcmpf2rf xmm, uvec1, size=4
};

def macroop EVEX_VUCOMISD_XMM_XMM {
    sse_mcmpf2rf xmm, xmmm, size=8
};

def macroop EVEX_VUCOMISD_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    sse_mcmpf2rf xmm, uvec1, size=8
};

def macroop EVEX_VUCOMISD_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    sse_mcmpf2rf xmm, uvec1, size=8
};

def macroop EVEX_VCOMISS_XMM_XMM {
    sse_mcmpf2rf xmm, xmmm, size=4
};

def macroop EVEX_VCOMISS_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    sse_mcmpf2rf xmm, uvec1, size=4
};

def macroop EVEX_VCOMISS_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    sse_mcmpf2rf xmm, uvec1, size=4
};

def macroop EVEX_VCOMISD_XMM_XMM {
    sse_mcmpf2rf xmm, xmmm, size=8
};

def macroop EVEX_VCOMISD_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    sse_mcmpf2rf xmm, uvec1, size=8
};

def macroop EVEX_VCOMISD_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    sse_mcmpf2rf xmm, uvec1, size=8
};

'''
